import telebot
from config import token
from random import choice


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Это бот, который может реагировать на Ваши сообщения и распознавать форматы сообщений! 🧠')


@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(
        message, 'Это бот, созданный при помощи telebot! Рад тому, что Вы пользуетесь моим ботом! 💻')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, 'Вы отправили фото! 📸')


@bot.message_handler(func=lambda message: message.text.lower() == 'как дела' or message.text.lower() == 'как дела?')
def how_are_you(message):
    available = ['хорошо', 'неплохо', 'отлично']
    bot.reply_to(message, f'У меня все {choice(available)} ⚡️')


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, 'Ух-ты, голосовое сообщение.. рад слышать! 🎤')


@bot.message_handler(content_types=['document'])
def handle_document(message):
    bot.reply_to(message, 'Вы какой-то занятой, раз скидываете документы 🧐')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    sent_message = bot.send_message(
        message.chat.id, 'Это сообщение будет изменено ✍️')
    message_id = sent_message.message_id

    bot.edit_message_text(chat_id=message.chat.id,
                          message_id=message_id, text='Это измененное сообщение 📝')


bot.infinity_polling()
