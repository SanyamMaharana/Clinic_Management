from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('Login_page.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    # Add your login logic here
    return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    # Add your registration logic here
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)