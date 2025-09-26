from flask import Flask, jsonify, request
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from telegram import Bot
TOKEN = os.getenv("TELEGRAM_KEY")
bot = Bot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, Flask! 🚀")

# registered telegram route
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()

    print(update)
    print(type(update))
    for i in update:
        print(i)

    return {"ok": True}

# using manually constructed response (api post)
@app.route("/v1/webhook/")
def sendMessageByRequest():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "this is manually response"
    b = os.getenv("BOT_NAME")

    return jsonify(message=a+b)

# wil be used bot variable 
@app.route("/v2/webhook/")
def sendMessageByBot():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "this is using bot library response"
    b = os.getenv("BOT_NAME")

    asyncio.run(bot.sendMessage(int(os.getenv("ADMIN")), f"Hellooo admin"))

    return jsonify(message=a+b)

if __name__ == '__main__':
    app.run(debug=True)
    