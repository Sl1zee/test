import telebot
from telebot import types

bot = telebot.TeleBot('7755671157:AAHExiIbMIPXBTHGCWYMBzRK4wUsev7OZTo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать.")
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("test")
    markup.row(btn1)
    bot.send_message(message.chat.id, "Выберите интересующие вас действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'test':
        bot.send_photo(message.chat.id, open('sos.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup()
        btn2 = types.KeyboardButton("bsd")
        markup.row(btn2)
        bot.send_message(message.chat.id, "Выберите интересующие вас действие:", reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "bsd":
        markup = types.ReplyKeyboardMarkup()
        btn2 = types.KeyboardButton("nice")
        markup.row(btn2)
        bot.send_message(message.chat.id, "Выберите интересующие вас действие:", reply_markup=markup)
        bot.register_next_step_handler(message, on_click1)

def on_click1(message):
    if message.text == "nice":
        markup = types.ReplyKeyboardMarkup()
        btn2 = types.KeyboardButton("good")
        markup.row(btn2)
        bot.send_message(message.chat.id, "Выберите интересующие вас действие:", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
