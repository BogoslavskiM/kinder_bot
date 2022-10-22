from tbot import *

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.info(e)