import telebot
bot = telebot.TeleBot('1088789624:AAH7fPuPwkFIdst-uu07Nl4X2XSYXWFX6D4')

@bot.message_handler(commands=['start'])
def mes(message):
    msg = bot.send_message(message.chat.id, 'Пришлите маску и количество подсетей через пробел')
    bot.register_next_step_handler(msg, div)

def div(message):
    try:
        import podseti
        divide = podseti.subnet_divide(int(message.text.split()[0]), int(message.text.split()[1]))
        bot.send_message(message.chat.id, "\n".join(divide))
    except:
        bot.send_message(message.chat.id, "Ты еблан??? Написано же маску сука число блять число после слэша")


bot.polling(True)

