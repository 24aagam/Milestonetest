# 41.Write a Flask route that accepts a parameter in the URL and displays it on the page.

from flask import Flask

url = Flask(__name__)

@url.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    url.run(debug=True)

# When you navigate to http://127.0.0.1:5000/greet/Aagam, the page will display "Hello, Aagam!"