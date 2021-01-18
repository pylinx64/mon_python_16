import pyttsx3
import webbrowser

tts = pyttsx3.init()

def say_bot(msg):
	print(msg)
	tts.say(msg)					# собирает фразы
	tts.runAndWait()				# говорит их

say_bot('Я ассистент версия 2 0')
say_bot('Как мне вас называть?')
NAME = input('NAME -> ')
while True:
	say_bot('Введите команду ' + NAME)
	command = input('COM -> ')
	if command == 'привет':
		say_bot('Нихао')
	elif command == 'пока':
		say_bot('Гудбай')
	elif command == 'как дела?':
		say_bot('Норм')
	elif command == 'Что умеешь?':
		say_bot('10010001')
		say_bot('01000001')
		say_bot('10000010')
	elif command == 'открой браузер':
		say_bot('Сайт открыт')
		webbrowser.open('www.youtube.com')
	else:
		say_bot('Я пока не знаю такой команды')
	
