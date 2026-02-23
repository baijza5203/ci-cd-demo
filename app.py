from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

VERSION = "1.0"

@app.route("/")
def home():
    return f"""
    <h2>🚀 CI/CD Demo App</h2>
    <p><b>Version:</b> {VERSION}</p>
    <p><b>Environment:</b> {os.getenv('ENVIRONMENT', 'Not Set')}</p>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Time:</b> {datetime.now()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
