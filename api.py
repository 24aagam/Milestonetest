# 44.How would you create a RESTful API endpoint in Flask that returns JSON data?

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data to return as JSON
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# When you run this script and visit http://127.0.0.1:5000/api/data in your web browser or a tool like Postman.