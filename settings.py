import telebot
import logging

logger = logging.getLogger('telegram')
handler = logging.FileHandler('telegram.txt')
handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.addFilter(lambda x: True)

token = '5440634030:AAEi5e9Egp5Uy2i6UR0UoXrcVXF9FyiyaD8'

bot = telebot.TeleBot(token)
sovet = '-1001199599857'
reserve = ''
