from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "Docker Week 1 Capstone",
        "hostname": socket.gethostname(),
        "time": str(datetime.now())
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)