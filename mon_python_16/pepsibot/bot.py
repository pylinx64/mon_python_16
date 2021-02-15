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
	# бот отправляет сообщение 
	bot.send_message(message.chat.id, 'Как поживаешь?')
	bot.send_message(message.chat.id, '🦶')


print('#run bot...')
bot.polling()
