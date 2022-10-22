import telebot
import logging

logger = logging.getLogger('telegram')
handler = logging.FileHandler('telegram.txt')
handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.addFilter(lambda x: True)

token = '5626060457:AAF0FWPCXDqB6Q3H9I3KnM2U5J4lvH3xGDM'

bot = telebot.TeleBot(token)
sovet = '-1001199599857'
reserve = ''
