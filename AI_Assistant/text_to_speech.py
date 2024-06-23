import pyttsx3 

def text_to_speech(text):
    engine = pyttsx3.init()
    speaking_rate = engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()

