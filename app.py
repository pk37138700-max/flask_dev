from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask_login"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def index():
    return render_template('home.html')


# Home Page
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

# Login/Register Page
@app.route('/signin')
def signin():
    return render_template('login_register.html')


# Register Route
@app.route('/register', methods=['POST'])
def register():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)

    cursor.execute(sql, values)
    db.commit()

    return "Registration Successful"


# Login Route
@app.route('/login', methods=['POST'])
def login():

    name= request.form['name']
    password = request.form['password']

    sql = "SELECT * FROM users WHERE name=%s AND password=%s"
    values = (name, password)

    cursor.execute(sql, values)

    user = cursor.fetchone()

    if user:
        return "Login Successful"
    else:
        return "Invalid name or Password"


# Run App
if __name__ == '__main__':
    app.run(debug=True)