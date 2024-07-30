# 39.How would you create a basic Flask route that displays "Hello, World!" on the homepage?

from flask import Flask

basic = Flask(__name__)

@basic.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    basic.run(debug=True)

# Access the homepage: Open your web browser and navigate to http://127.0.0.1:5000/. You should see "Hello, World!" displayed on the homepage.