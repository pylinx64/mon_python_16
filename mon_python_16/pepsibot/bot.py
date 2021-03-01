import telebot
import random 

bot = telebot.TeleBot('1615084228:AAH7ZYVsJMNhv15_6HL1yq2-B8TGZL3VRbs') 	# сюда токен

#--------------------------start----------------------------------------
@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	bot.send_message(message.chat.id, 'Ну привет!')
	#print(message.chat.first_name, message.text)
#--------------------------start----------------------------------------

#--------------------------text-----------------------------------------
@bot.message_handler(content_types=['text'])
def message_text(message):
	bot.send_message(message.chat.id, 'ФОТО!')
	'''Принимает текст и отвечает на него'''
	print(message.chat.first_name, message.text)
	if 'дела' in message.text.lower():
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA')
		bot.send_message(message.chat.id, 'норм') # бот отправляет сообщение 
	elif 'привет' in message.text.lower():
		bot.send_message(message.chat.id, '''
		да да да
		нет нет нет
		ок ок ок
		''') 
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю')
#--------------------------text-----------------------------------------

#--------------------------sticker--------------------------------------
@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
	stickers = ['CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA', 
	'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA', 
	'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA']
	#bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA')
	print(message.sticker.file_id)
#--------------------------sticker--------------------------------------

print('#run bot...')
bot.polling()
