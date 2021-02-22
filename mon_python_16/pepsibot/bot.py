import telebot

bot = telebot.TeleBot('1615084228:AAH7ZYVsJMNhv15_6HL1yq2-B8TGZL3VRbs') 	# сюда токен

@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	bot.send_message(message.chat.id, 'Ну привет!')
	#print(message.chat.first_name, message.text)

@bot.message_handler(content_types=['text'])
def message_text(message):
	'''Принимает текст и отвечает на него'''
	print(message.chat.first_name, message.text)
	if 'дела' in message.text.lower():
		bot.send_message(message.chat.id, 'норм') # бот отправляет сообщение 
	elif 'привет' in message.text.lower():
		bot.send_message(message.chat.id, '''
		да да да
		нет нет нет
		ок ок ок
		''') 
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю')


print('#run bot...')
bot.polling()
