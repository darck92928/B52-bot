
import telebot

bot = telebot.TeleBot("6552995612:AAGpPJPmKHJBKeSbzNJPxjxM3-8HDXa_rec")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "سلاو,بەخیرهاتی بۆ بۆتی پایثۆن.")

@bot.message_handler(commands=["help"])
def send_help(message):
  bot.send_message(message.chat.id, "چۆن یارمەتیت بەدەم؟")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

