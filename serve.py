from flask import Flask
from subprocess import Popen
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run stress_cpu.py as a separate process
    Popen(["python3", "stress_cpu.py"])
    return 'CPU stress test started', 200

@app.route('/', methods=['GET'])
def get_ip():
    # Get the private IP address of the EC2 instance
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
