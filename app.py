from flask import Flask, jsonify
from uuid import uuid4

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    # Define a simple JSON response
    data = {
        'message': 'Hello, World!'
    }
    # Return JSON response with Content-Type header set to application/json
    return jsonify(data), 200, {'Content-Type': 'application/json'}

# Define a route for the root URL
@app.route('/healthz')
def healthz():
    # Define a simple JSON response
    data = {
        'status': 200,
        'message': 'OK'
    }
    # Return JSON response with Content-Type header set to application/json
    print('health=========>', data)
    return jsonify(data), 200, {'Content-Type': 'application/json'}

@app.route('/uuid')
def uuid():
    data = {
        'uuid': uuid4()
    }
    return jsonify(data), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)