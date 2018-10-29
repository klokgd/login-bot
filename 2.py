import config
import telebot
from telebot import types, apihelper

apihelper.proxy = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}

bot = telebot.TeleBot(config.TOKEN, threaded=False)


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


if __name__ == '__main__':
    bot.polling(none_stop=True)
