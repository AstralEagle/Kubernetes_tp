from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BACKEND_URL = 'http://backend:3402'

@app.route('/write/<data>', methods=['GET'])
def write(data):
    response = requests.post(f"{BACKEND_URL}/write/{data}")
    return response.text

@app.route('/read', methods=['GET'])
def read():
    response = requests.get(f"{BACKEND_URL}/read")
    return response.text

@app.route('/compute', methods=['GET'])
def compute():
    response = requests.get(f"{BACKEND_URL}/compute")
    return response.text

@app.route('/status', methods=['GET'])
def status():
    response = requests.get(f"{BACKEND_URL}/status")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3403)
