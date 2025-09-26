from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

from model.user import User

from telegram import Bot
TOKEN = os.getenv("TELEGRAM_KEY2")
bot = Bot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    # will be used for static web(maybe)
    return jsonify(message="Hello, Flask! 🚀")

# registered telegram route
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    # construct user
    user = User(update)
    print(user.getId())
    print(user.getName())

    # user handling
        # access user database
        # access user Id state or env status (conv)

    # message handling
        # command message
        # based on env status (conv)

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

if __name__ == "__main__":
    app.run(debug=True)
    