from flask import Flask, jsonify
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

@app.route("/webhook")
def webhook():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "test"
    b = os.getenv("BOT_NAME")

    return a+b

# using manually constructed response (api post)
@app.route("/v1/webhook/")
def sendMessageByRequest():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "this is manually response"
    b = os.getenv("BOT_NAME")

    return jsonify(message=a+b)

# wil be used bot variable 
def botSendingMessage(): 
    bot.sendMessage(int(os.getenv("ADMIN")), f"Hellooo admin")

@app.route("/v2/webhook/")
def sendMessageByBot():
    a = os.getenv("BOT_NAME")
    os.environ["BOT_NAME"] = "this is using bot library response"
    b = os.getenv("BOT_NAME")

    asyncio.run(botSendingMessage())

    return jsonify(message=a+b)

if __name__ == '__main__':
    app.run(debug=True)
    