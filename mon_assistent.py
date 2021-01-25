# Библиотеки для ассистента
import pyttsx3
import webbrowser
from datetime import datetime, date, time
import pyautogui
import time 


# Настройки для ассистента
tts = pyttsx3.init()
tts.setProperty('rate', 150)		# скорость говорения


# Команды для ассистента
def say_bot(msg):
	print(msg)
	tts.say(msg)					# собирает фразы
	tts.runAndWait()				# говорит их
	
def send_to_program():
	pyautogui.click(360, 940, duration=1)
	pyautogui.click(750, 750, duration=1)


say_bot('Я ассистент версия 2 0')
say_bot('Как мне вас называть?')
NAME = input('NAME -> ')
#-------ОСНОВНОЙ КОД АССИСТЕНТА--------------
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
	elif command == 'quit':
		break
	elif command == 'время':
		time_check = datetime.now()
		h = time_check.hour
		m = time_check.minute
		say_bot(str(h) + ':'+ str(m))
	elif command == 'открой программу':
		send_to_program()
		say_bot('Программа открыта')
	else:
		say_bot('Я пока не знаю такой команды')
	
