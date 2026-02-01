from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route("/message", methods=["POST"])
def save_message():
    data = request.json
    message = data.get("message", "")
    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]\n{message}\n\n")
    return jsonify({"status": "saved"})


# Password-protected message reading
@app.route("/messages", methods=["POST"])
def read_messages():
    data = request.json
    password = data.get("password")
    if password != os.environ.get("ADMIN_PASSWORD"):
        return jsonify({"error": "Unauthorized"}), 401

    if not os.path.exists("messages.txt"):
        return jsonify({"messages": ""})

    with open("messages.txt", "r", encoding="utf-8") as f:
        content = f.read()

    return jsonify({"messages": content})


# 🔑 IMPORTANT: Use PORT from environment variable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets this automatically
    app.run(host="0.0.0.0", port=port)
