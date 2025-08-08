@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = api_client.register_user(username, password)
        if response.status_code == 200:
            flash('User registered successfully!')
            return redirect(url_for('login'))
        else:
            flash('Registration failed! Please try again.')
    return render_template('user_register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = api_client.login_user(username, password)
        if response.status_code == 200:
            token = response.json().get('access_token')
            flash('Login successful!')
            # Store token in session or cookie as needed
            return redirect(url_for('index'))
        else:
            flash('Login failed! Invalid credentials.')
    return render_template('login.html')
from flask import Flask, render_template, request, redirect, url_for, flash
from frontend.models.api_client import APIClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'
api_client = APIClient()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
