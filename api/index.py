from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask API on Vercel!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": [1, 2, 3, 4, 5]})

# Remove the `app.run()` statement, which isn't needed in serverless deployment
def handler(req, res):
    # Flask app serves as a callable function
    with app.app_context():
        return app.full_dispatch_request()
