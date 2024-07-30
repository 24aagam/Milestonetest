# 49. Make a fully functional web application using flask, Mangodb. Signup,Signin page.And after successfully login .Say hello Geeks message at webpage.

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a real secret key

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flaskdb'  # Update with your MongoDB URI
mongo = PyMongo(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if mongo.db.users.find_one({'username': username}):
            flash('Username already exists!')
            return redirect(url_for('signup'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        mongo.db.users.insert_one({'username': username, 'password': hashed_password})
        flash('Signup successful!')
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!')
    
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
