import telebot
from telebot import types
import requests


TOKEN = '' #токен вашего бота

bot = telebot.TeleBot(TOKEN)
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json() #json для реальной валюты
response = requests.get('https://blockchain.info/ru/ticker').json() #json для криптовалюты
 


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Курс криптовалюты')
    item2 = types.KeyboardButton('Курс валют')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Курс чего вы бы хотели узнать?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == 'Курс валют':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
        item1 = types.KeyboardButton('Узнать курс доллара')
        item2 = types.KeyboardButton('Узнать курс евро')
        item3 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Курс какой валюты хотите узнать?', reply_markup=markup)
    elif message.text == 'Узнать курс доллара':
        bot.send_message(message.chat.id,'Курс доллара: ' + str(data['Valute']['USD']['Value']))
    elif message.text == 'Узнать курс евро':
        bot.send_message(message.chat.id,'Курс евро: ' + str(data['Valute']['EUR']['Value']))
    elif message.text == 'Назад':
        start(message)
    elif message.text == 'Курс криптовалюты':
        bot.send_message(message.chat.id, 'Курс биткоина: ' + str(response['RUB']['last']))
        start(message)


if __name__ == "__main__":   
    bot.polling(non_stop=True)

