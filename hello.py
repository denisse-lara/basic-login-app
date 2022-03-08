import os
import uuid
import logging

from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    flash,
    make_response,
    session,
)
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"), username=username)
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            flash("Successfully logged in")
            session["username"] = request.form.get("username")
            return redirect(url_for("home", username=request.form.get("username")))
        else:
            error = "Invalid username and password combination"
            app.logger.warning(
                "Incorrect username and password for user (%s)",
                request.form.get("username"),
            )
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/home/<username>")
def home(username=None):
    return render_template("home.html", username=username)


def valid_login(username, password):
    if password == "1234":
        return True

    return False


if __name__ == "__main__":
    host = os.getenv("IP", "0.0.0.0")
    port = int(os.getenv("PORT", 5000))
    app.debug = True
    app.secret_key = os.getenv("KEY")

    # logging
    handler = RotatingFileHandler("error.log", maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.run(host=host, port=port)
