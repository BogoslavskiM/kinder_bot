from turtle import st
from settings import *
from data import *


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text=messages['hello'])


@bot.message_handler(content_types=['text'])
def resend(message):
    try:
        bot.forward_message(chat_id=sovet, from_chat_id=int(message.chat.id), message_id=message.id)
    except Exception as e:
        print(e)
        mes = f'''
    user_data 
    name: {message.from_user.name}
    last_name: {message.from_user.last_name}
    user_id: {message.from_user.id}
    user_name: @{message.from_user.username}

    text: {message.text}'''
        bot.send_message(sovet, mes)
        

    bot.send_message(message.chat.id, messages['reply_data'])
    bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAMfY1QEX7wTP6OY-nOvjsA_d4cp1jsAAmUAA8A2TxMTo2UohLerHioE')

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAMfY1QEX7wTP6OY-nOvjsA_d4cp1jsAAmUAA8A2TxMTo2UohLerHioE')
