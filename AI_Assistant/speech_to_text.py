import speech_recognition as sr 
from requests_html import HTMLSession
import text_to_speech


def speech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source) # methord 
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        return voice_data

      except sr.UnknownValueError:
             text_to_speech.text_to_speech("sorry")
      except sr.RequestError:
            text_to_speech.text_to_speech('No internet connect please turn on you internet')  



     