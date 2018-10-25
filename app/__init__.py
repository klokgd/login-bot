from flask import Flask, request
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN, threaded=False)
server = Flask(__name__)
server.config.from_object(Config)
db = SQLAlchemy(server)
migrate = Migrate(server, db)

from app import models, routes

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Регистрация", callback_data="register")
    item2 = types.InlineKeyboardButton("Вход", callback_data="login")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, reply_markup=markup, text="Приветствую вас! Выберите пункт меню.")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "login":
        register(call)
    elif call.data == "register":
        login(call)

def register(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='111')
def login(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='666')


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='' + config.TOKEN)
    return "!", 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
