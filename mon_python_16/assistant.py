import pyttsx3

tts = pyttsx3.init()			# запуск голосового движка

tts.setProperty('voice', 'ru')  # Наш голос по умолчанию

tts.say('Привет')				# бот собирает фразы 
tts.runAndWait()				# бот говорит фразы
