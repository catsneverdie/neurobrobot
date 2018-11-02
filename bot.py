#!/usr/bin/env python3
# настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json, awsmpg
updater = Updater(token='700733396:AAEUM6LbSwG8YFXMKjfvXYK--BZjOFitwR8')
dispatcher = updater.dispatcher

# обработка событий
# _
# для команды /start
def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет, я - твой Нейробратан. Я пока что не очень умный, но ты можешь попробовать пообщаться со мной :)')

# для любого текстового сообщения
def textMessage(bot, update):
	request = apiai.ApiAI('e4587e9b8d1442f882c7a6d744bf2210').text_request()	# здесь нужен токен Dialogflow
	request.lang = 'ru'															# язык запроса
	request.session_id = 'neurobrobot'											# ID сессии для Dialogflow
	request.query = update.message.text											# посылаем запрос ИИ с сообщением юзера
	# разбираем JSON
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	# если есть ответ от ИИ - посылаем юзеру
	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
# /sayhello
def sayHello(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет! Кликни на это сообщение и нажми "Ответить", чтобы поговорить со мной.')

# /postverse
# отправляет сообщением случайно сгенерированное четверостишие
def postPoem(bot, update):
	poem = awsmpg.makePoem()
	bot.send_message(chat_id=update.message.chat_id, text=poem)


# хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
sayhello_handler = CommandHandler('sayhello', sayHello)
postverse_handler = CommandHandler('postverse', postPoem)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(sayhello_handler)
dispatcher.add_handler(postverse_handler)

# поиск обновлений
updater.start_polling(clean='True')
# остановка бота при нажатии ctrl+c
updater.idle()

