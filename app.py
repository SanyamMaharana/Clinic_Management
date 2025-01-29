from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin@123'
app.config['MYSQL_DB'] = 'clinicdb'

mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('Login_page.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/check_db')
def check_db():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT 1')
        return 'Database is connected!'
    except Exception as e:
        return f'Error: {e}'

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    # Check in doctor table
    cursor.execute('SELECT * FROM doctor WHERE username = %s AND password = %s', (username, password))
    doctor_account = cursor.fetchone()
    
    if doctor_account:
        # Login successful for doctor
        return redirect(url_for('doctor_dashboard'))
    
    # Check in patient table
    cursor.execute('SELECT * FROM patient WHERE username = %s AND password = %s', (username, password))
    patient_account = cursor.fetchone()
    
    if patient_account:
        # Login successful for patient
        return redirect(url_for('patient_dashboard'))
    
    # Login failed
    return 'Invalid username/password'

@app.route('/register', methods=['POST'])
def register_post():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    contact = request.form['contact']
    if password == confirm_password:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO patient (name, username, password, contact_info) VALUES (%s, %s, %s, %s)', (name, username, password, contact))
        mysql.connection.commit()
        return redirect(url_for('login'))
    else:
        return 'Passwords do not match'

@app.route('/doctor_dashboard')
def doctor_dashboard():
    return render_template('doctor_dashboard.html')

@app.route('/patient_dashboard')
def patient_dashboard():
    return render_template('patient_dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)