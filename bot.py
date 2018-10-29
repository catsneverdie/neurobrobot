#!/usr/bin/env python3
# настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='700733396:AAEUM6LbSwG8YFXMKjfvXYK--BZjOFitwR8')
dispatcher = updater.dispatcher

# обработка событий
# _
# для команды /start
def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет, братан!')

# для любого текстового сообщения
def textMessage(bot, update):
	request = apiai.ApiAI('c9eb73e915e949edaf20338c01c6c020').text_request()	# здесь нужен токен Dialogflow
	request.lang = 'ru'															# язык запроса
	request.session_id = 'neurobrobot'											# ID сессии для Dialogflow
	request.query = update.message.text											# посылаем запрос ИИ с сообщением юзера
	# разбираем JSON
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	# если есть ответ от ИИ - посылаем юзеру, если нет - шаблон "Я не понял"
	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
	else:
		bot.send_message(chat_id=update.message.chat_id, text='Я не совсем врубаюсь, братан!')


# хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)


# поиск обновлений
updater.start_polling(clean='True')
# остановка бота при нажатии ctrl+c
updater.idle()

