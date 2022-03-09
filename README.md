# basic-login-app

## running the app

1. Install the requirements
```
pip install -r requirements.txt
```
2. Setup a mysql db with a user table.
```
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| userid   | int         | NO   | PRI | NULL    | auto_increment |
| username | varchar(64) | NO   |     | NULL    |                |
| password | varchar(64) | NO   |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
```
3. Insert a user.
```
insert into user values(0, 'username', 'password');
```
4. Set the environmental variables in a .env file.
```
# DATABASE
DBHOST="you_db_host"
DBNAME="your_db_name"
DBPASSWORD="your_db_password"
DBUSER="your_db_user"

SECRET_KEY="your_secret_key"
```
5. Run app to test login.
```
python hello.py
```
