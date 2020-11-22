import config
import telebot
from tests import test
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
replica = []
markup = types.ForceReply(selective=False)
count = 0


@bot.message_handler(commands=['start', 'info'])
def start_messages(message):
    global count
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'You start Test! Good luck!')
        count = 1
    if count == 1:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
    if message.text.lower() == '/info':
        bot.send_message(message.chat.id, 'Этот тест, является проверкой ваших знаний предмета Тестирование. Для того чтобы начать наберите /start')

# handler для теста
@bot.message_handler(content_types=['text'])
def test_start(message):
    global count
    if message.text.lower() != 'вопрос' and message.text.lower() != 'rpl':
        replica.append(message.text)
    if message.text.lower() == 'rpl':
        bot.send_message(message.chat.id, f'{replica}')
    if count == 2:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 3:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 4:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 5:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 6:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 7:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 8:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 9:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}')
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0
    elif count == 10:
        if count <= len(test):
            bot.send_message(message.chat.id, f'{test[count]}')
            count += 1
        else:
            bot.send_message(message.chat.id, f'Вопросы кончились, тест пройден!')
            count = 0


bot.polling()