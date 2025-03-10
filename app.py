from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# API Key (Replace with your secure key)
API_KEY = "mysecureapikey123"

# Open Access Endpoint
@app.route('/open-data', methods=['GET'])
def open_data():
    return jsonify({"message": "This is open access data", "status": "success"})

# Protected Endpoint (Requires API Key)
@app.route('/secure-data', methods=['GET'])
def secure_data():
    key = request.headers.get("x-api-key")  # Read API key from header
    if key == API_KEY:
        return jsonify({"message": "This is protected data", "status": "success"})
    else:
        return jsonify({"error": "Unauthorized, invalid API key"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
