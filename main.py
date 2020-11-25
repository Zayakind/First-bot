import config
import telebot
from tests import Junior, Middle, Senior
from telebot import types
from send_mail import send_messege

#обьявляем бота, кнопку и нужные переменные для работы.
bot = telebot.TeleBot(config.TOKEN)
replica = {}
markup = types.ForceReply(selective=False)
count = 0
test = {}
Usrs = []

# Команды для начала и информации
@bot.message_handler(commands=['start', 'info'])
def start_messages(message):
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Напишите предпочтительный уровень теста: Junior, Middle, Senior')
    if message.text.lower() == '/info':
        bot.send_message(message.chat.id, 'Этот тест, является проверкой ваших знаний предмета Тестирование. Для того чтобы начать наберите /start')


# handler для теста
@bot.message_handler(content_types=['text'])
def test_start(message):
    global count
    global test
    global Junior
    global Middle
    global Senior
    global Usrs
    #Записывание ответов в словарь 
    if message.text.lower() != 'start' and message.text.lower() != 'info' and message.text.lower() != 'junior' and message.text.lower() != 'middle' and message.text.lower() != 'senior':
        replica[count-1] = message.text
    #Присваивание тестам вариант который выбирает пользователь, запуск теста и запись в список какой пользователь выбрал тест
    if message.text.lower() == 'junior' or message.text.lower() == 'middle' or message.text.lower() == 'senior':
        if message.text.lower() == 'junior':
            test = Junior
            Usrs.append(message.chat.first_name + ' ' + message.chat.last_name + ' Junior')
            count = 1
        elif message.text.lower() == 'middle':
            test = Middle
            Usrs.append(message.chat.first_name + ' ' + message.chat.last_name + ' Middle')
            count = 1
        elif message.text.lower() == 'senior':
            test = Senior
            Usrs.append(message.chat.first_name + ' ' + message.chat.last_name + ' Senior')
            count = 1
        if count == 1:
            bot.send_message(message.chat.id, f'{test[count]}', reply_markup=markup)
            count += 1
    # Вопросы для теста
    elif count == 2:
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
            send_messege(Usrs, replica)
            replica.clear()
            Usrs.clear()



bot.polling()