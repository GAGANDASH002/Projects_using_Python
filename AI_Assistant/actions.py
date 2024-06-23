import time
import text_to_speech 
import datetime
import webbrowser
import weather


def Actions(send):
    
    user_data = send.lower()

    if "what is your name" in user_data or "who are you" in user_data:
        text_to_speech.text_to_speech("Hello! This is Jarvis")
        return "Hello! This is Jarvis"

    elif "hello" in user_data or "hi" in user_data :
        text_to_speech.text_to_speech("Hey boss , how can I help You")
        return "Hey boss , how can I help You"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning boss , have a good day")
        return "Good Morning boss , have a good day"
    
    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("Good Afternoon boss , have a good day")
        return "Good Afternoon boss , have a good day"
    
    elif "good evening" in user_data:
        text_to_speech.text_to_speech("Good Evening boss , have a good day")
        return "Good Evening boss , have a good day"
    
    elif "good night" in user_data:
        text_to_speech.text_to_speech("Good night boss , see you tomorrow")
        return "Good night boss , see you tomorrow"
    
    elif "who made you" in user_data or "who developed you" in user_data or "who is your creator" in user_data:
        text_to_speech.text_to_speech("I am Jarvis AI Assistant and I was developed by Gagan Dash")
        return "I am Jarvis AI Assitant and I was developed by Gagan Dash"
    
    elif "time now" in user_data or "what is the time now" in user_data or "what is the current time"  in user_data:
        curr_time = datetime.datetime.now()
        time_hr = curr_time.strftime("%H")
        time_min = curr_time.strftime("%M")
        Time = f"the current time is : {time_hr} hours {time_min} minutes"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data or "bye" in user_data:
        text_to_speech.text_to_speech("Ok boss , glad i could help")
        return "Ok boss , glad i could help"
    
    elif "thank you" in user_data or "thanks" in user_data or "thanks jarvis" in user_data or "thank you jarvis" in user_data:
        text_to_speech.text_to_speech("My Pleasure , have a good day")
        return "My Pleasure , have a good day"
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is ready to play your favorite songs")
        return "gaana.com is ready to play your favorite songs"
    
    elif "open google" in user_data or "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google is ready for you to browse")
        return "google is ready for you to browse"
    
    elif "open youtube" in user_data or "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube is ready for you to surf")
        return "youtube is ready for you to surf"

    elif "weather" in user_data or "weather today" in user_data or "what is the weather" in user_data or "tell me today's weather" in user_data or "today's weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech("Today's weather conditions in your area are"+ans)
        return "Today's weather conditions in your area are"+ans
    
    else:
        text_to_speech.text_to_speech("I am Unable to understand , will get back to u asap")
        return "I am Unable to understand , will get back to u asap"