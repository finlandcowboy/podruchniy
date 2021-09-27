import telebot
import schedule
from threading import Thread
import time
bot = telebot.TeleBot('1088789624:AAH7fPuPwkFIdst-uu07Nl4X2XSYXWFX6D4')

@bot.message_handler(commands=['start'])
def mes(message):
    msg = bot.send_message(message.chat.id, 'Пришлите маску и количество подсетей через пробел')
    bot.register_next_step_handler(msg, div)

def div(message):
    import podseti
    divide = podseti.subnet_divide(int(message.text.split()[0]), int(message.text.split()[1]))
    bot.send_message(message.chat.id, "\n".join(divide))


bot.polling(True)

