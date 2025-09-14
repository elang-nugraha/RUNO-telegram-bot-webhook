from flask import Flask, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, Flask! 🚀")

@app.route("/webhook")
def webhook():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "test"
    b = os.getenv("BOT_NAME")

    return jsonify(message=a+b)

if __name__ == '__main__':
    app.run(debug=True)