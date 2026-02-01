from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/message", methods=["POST"])
def save_message():
    data = request.json
    message = data.get("message", "")

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]\n{message}\n\n")

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(port=5000)
