import pyttsx3

tts = pyttsx3.init()

tts.say("Hello")					# собирает фразы
tts.runAndWait()				# говорит их
