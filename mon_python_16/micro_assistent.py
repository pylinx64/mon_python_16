import speech_recognition as sr
# теперь вместо command = input() -> command = human_speech(r)

# Функция служит для отслеживания микрофона(запись речи)
def human_speech(rec):
        with sr.Microphone() as source:
                status_rec = 1
                print('REC:')
                rec.pause_threshold = 1
                rec.adjust_for_ambient_noise(source, duration=1)
                print('STOP')
                audio = rec.listen(source)
        try:
                message = rec.recognize_google(audio, language="ru_RU").lower()
        except sr.UnknownValueError:
                message = None
        return message

r = sr.Recognizer()
command = human_speech(r) # input меняете на human_speech(r) 
