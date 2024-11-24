from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the API
items = [
    {"id": 1, "name": "Item One", "description": "This is the first item."},
    {"id": 2, "name": "Item Two", "description": "This is the second item."},
    {"id": 3, "name": "Item Three", "description": "This is the third item."}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Minimal root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Simple Items API!"})
