from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the API
items = [
    {"id": 1, "fullname": "John Doe", "address": "123 Elm Street", "email": "johndoe@example.com"},
    {"id": 2, "fullname": "Jane Smith", "address": "456 Oak Avenue", "email": "janesmith@example.com"},
    {"id": 3, "fullname": "Alice Johnson", "address": "789 Pine Road", "email": "alicej@example.com"},
    {"id": 4, "fullname": "Bob Brown", "address": "101 Maple Lane", "email": "bobbrown@example.com"},
    {"id": 5, "fullname": "Charlie Davis", "address": "202 Birch Boulevard", "email": "charlied@example.com"},
    {"id": 6, "fullname": "Diana White", "address": "303 Cedar Circle", "email": "dianaw@example.com"},
    {"id": 7, "fullname": "Edward Green", "address": "404 Willow Way", "email": "edwardg@example.com"},
    {"id": 8, "fullname": "Fiona Black", "address": "505 Aspen Drive", "email": "fionab@example.com"},
    {"id": 9, "fullname": "George Hill", "address": "606 Magnolia Street", "email": "georgeh@example.com"},
    {"id": 10, "fullname": "Hannah Wright", "address": "707 Palm Place", "email": "hannahw@example.com"},
    {"id": 11, "fullname": "Ivy Scott", "address": "808 Cypress Court", "email": "ivys@example.com"},
    {"id": 12, "fullname": "Jack Turner", "address": "909 Redwood Road", "email": "jackt@example.com"},
    {"id": 13, "fullname": "Kelly Adams", "address": "1010 Fir Lane", "email": "kellya@example.com"},
    {"id": 14, "fullname": "Leo Brown", "address": "1111 Spruce Street", "email": "leob@example.com"},
    {"id": 15, "fullname": "Mia Clark", "address": "1212 Sequoia Avenue", "email": "miac@example.com"}
]

@app.route('/api/users', methods=['GET'])
def get_items():
    return jsonify(items)

# Minimal root route
@app.route('/')
def home():
    return jsonify({"message": "Flask REST API - VP Demo"})
