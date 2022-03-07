import os

from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    # import pdb; pdb.set_trace()
    return '<a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            return redirect(url_for('home', username=request.form.get('username')))
        else:
            error = 'Invalid username and password combination'
    return render_template('login.html', error=error)

@app.route('/home/<username>')
def home(username=None):
    return render_template('home.html', username=username)

def valid_login(username, password):
    if password == "1234":
        return True
    
    return False

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = os.getenv('KEY')
    app.run(host=host, port=port)
