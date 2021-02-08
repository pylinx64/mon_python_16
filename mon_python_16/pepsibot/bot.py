import telebot

bot = telebot.TeleBot('1615084228:AAH7ZYVsJMNhv15_6HL1yq2-B8TGZL3VRbs') 	# сюда токен

@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	bot.send_message(message.chat.id, 'Ну привет!')


bot.polling()
