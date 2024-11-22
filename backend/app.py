from flask import Flask, request, jsonify
import os
import time
import math

app = Flask(__name__)

LOG_FILE = '/app-data/log.txt'

@app.route('/write/<data>', methods=['POST'])
def write(data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(data + '\n')
    return "Data written successfully.\n"

@app.route('/read', methods=['GET'])
def read():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return f.read()
    return "No data found.\n"

@app.route('/compute', methods=['GET'])
def compute():
    start_time = time.time()
    result = sum(math.sin(i) * math.cos(i) for i in range(1, 10000000))
    execution_time = time.time() - start_time
    return f"Computation result: {result}, executed in {execution_time:.2f} seconds\n"

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "healthy", "uptime": time.time()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3402)
