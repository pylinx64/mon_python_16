import telebot
import random 
import bs4
import requests
from telebot import types

bot = telebot.TeleBot('1615084228:AAH7ZYVsJMNhv15_6HL1yq2-B8TGZL3VRbs') 	# сюда токен

#--------------------------parser---------------------------------------
def parser_gif(search):
	'''Функция которая парсит ссылки с гифками'''
	
	# подключаемся к сайту
	res = requests.get('https://tenor.com/search/'+search+'-gifs')
	
	# проверка на ошибки
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text)
	
	# здесь хранятся гифки
	gifElem = soup.select('img[src]')
	
	gif_list = []
	
	for i in gifElem:
        # достает только ссылки
		url = i.get('src')
        # добавляет ссылки в список
		gif_list.append(url)
	
    # достает рандомную гифку из списка
	gif_random = random.choice(gif_list)
	return gif_random
#--------------------------parser---------------------------------------

#--------------------------start----------------------------------------
@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	# кнпопки
	button = types.ReplyKeyboardMarkup()
	button.row('привет', "✨")
	button.row('error')
	bot.send_message(message.chat.id, 'Ну привет! Поиск по гифкам на англиском языке!', reply_markup=button)
	#print(message.chat.first_name, message.text)
#--------------------------start----------------------------------------

#--------------------------text-----------------------------------------
@bot.message_handler(content_types=['text'])
def message_text(message):
	#bot.send_message(message.chat.id, 'ФОТО!')
	'''Принимает текст и отвечает на него'''
	print(message.chat.first_name, message.text)
	if 'дела' in message.text.lower():
		#bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA')
		bot.send_message(message.chat.id, 'норм') # бот отправляет сообщение 
	elif 'привет' in message.text.lower():
		bot.send_message(message.chat.id, '''
		да да да
		нет нет нет
		ок ок ок
		''') 	
	else:
		bot.send_message(message.chat.id, parser_gif(message.text))
#--------------------------text-----------------------------------------

#--------------------------sticker--------------------------------------
@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
	stickers = ['CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA', 
	'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA', 
	'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA']
	bot.send_sticker(message.chat.id, random.choice(stickers))
	print(message.sticker.file_id)
#--------------------------sticker--------------------------------------

print('#run bot...')
bot.polling()
