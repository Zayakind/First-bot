import config
import telebot
from tests import test
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
replica = []
markup = types.ForceReply(selective=False)
count = 1

@bot.message_handler(content_types=['text'])
def start_messages(message):
    global count
    if message.text.lower() == 'вопрос':
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            answer.append()
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    if message.text.lower() == 'rpl':
        bot.send_message(message.chat.id, f'{replica}')


bot.polling()