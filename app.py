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

loop = asyncio.new_event_loop()

@app.route("/")
def home():
    # will be used for static web(maybe)
    return jsonify(message="Hello, Flask! 🚀")

# registered telegram route
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()

    user = User(update)
    print(user.getId())
    print(user.getName())

    # # user handling
    #     # access user database
    #     # access user Id state or env status (conv)

    # message = update.get("message").get("text")
    # message = message.strip()
    botCommands = "BOT Commands\n\n" \
        "/userRegistration \n " \
        "/openRegistration \n " \
        "/closeRegistration \n" \
        "/addItem \n" \
        "/updateStock \n" \
        "/getStock \n" \
        "/addTransaction"
    message = "/start"
    if (message == "/start" ):
        print(sendMessageByBot("Hello Welcome to ", 100))
        print(sendMessageByBot(botCommands, 100))
    else:
        print(sendMessageByBot(botCommands, 100))
        print(sendMessageByBot("Ask admin for use commands", 100))
    # message handling
        # command message
        # based on env status (conv)

    return {"ok": True}

def sendMessageByBot(message  : str, id : int):
    id = os.getenv("ADMIN")
    # if loop.is_running():
    #     loop.create_task(bot.send_message(bot.send_message(id, message)))
    # else:
    #     loop.run_until_complete(bot.send_message(id, message))
    return id

# using manually constructed response (api post)
# @app.route("/v1/webhook/")
# def sendMessageByRequest():
#     a = os.getenv("BOT_NAME")
#     os.environ["BOT_NAME"] = "this is manually response"
#     b = os.getenv("BOT_NAME")

#     return jsonify(message=a+b)

if __name__ == "__main__":
    app.run(debug=True)
    