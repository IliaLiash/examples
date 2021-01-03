import re
import random
import telebot
import requests
import datetime
from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot(###)

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Пишем приветствие
    bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
    # Готовим кнопки
    keyboard = types.InlineKeyboardMarkup()     
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_oven = types.InlineKeyboardButton(text='Овен', callback_data='aries')
    # И добавляем кнопку на экран
    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text='Телец', callback_data='taurus')
    keyboard.add(key_telec)
    key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='gemini')
    keyboard.add(key_bliznecy)
    key_rak = types.InlineKeyboardButton(text='Рак', callback_data='cancer')
    keyboard.add(key_rak)
    key_lev = types.InlineKeyboardButton(text='Лев', callback_data='leo')
    keyboard.add(key_lev)
    key_deva = types.InlineKeyboardButton(text='Дева', callback_data='virgo')
    keyboard.add(key_deva)
    key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='libra')
    keyboard.add(key_vesy)
    key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpio')
    keyboard.add(key_scorpion)
    key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='sagitarius')
    keyboard.add(key_strelec)
    key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='capricorn')
    keyboard.add(key_kozerog)
    key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='aquarius')
    keyboard.add(key_vodoley)
    key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='pisces')
    keyboard.add(key_ryby)
    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    url = "http://horo.mail.ru/prediction/{0}/today/".format(call.data)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")      
    # Формируем гороскоп
    date = datetime.date.today().strftime("%d-%m-%Y")
    msg = soup.find_all("p")
    # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, 'Гороскоп на {0}:\n\n{1}'.format(date,msg))
        
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
