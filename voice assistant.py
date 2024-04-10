import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def greet_user():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        engine.say("Good Morning!")
    elif 12 <= current_hour < 18:
        engine.say("Good Afternoon!")
    else:
        engine.say("Good Evening!")
    engine.say("I'm your Python Voice Assistant. How can I help you today?")
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            print("You said:", command)
            return command.lower()  # Convert command to lowercase
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that. Could you repeat?")
        return listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


def respond(text):
    engine.say(text)
    engine.runAndWait()


def get_weather():
   
    print("Sorry, weather information is not implemented yet.")
    respond("Sorry, I can't provide weather information yet, but I'm still learning!")

def search_web(query):
    webbrowser.open("https://www.google.com/search?q=" + query)
    respond("Opening " + query + " in your web browser.")

def play_music():
   
    print("Sorry, music playback is not implemented yet.")
    respond("Sorry, I can't play music yet, but I'm still learning!")

def open_app(app_name):
    
    print("Sorry, opening applications is not implemented yet.")
    respond("Sorry, I can't open applications yet, but I'm still learning!")

def tell_joke():
    
    print("Sorry, joke telling is not implemented yet.")
    respond("Sorry, I can't tell jokes yet, but I'm still learning!")


greet_user()
while True:
    command = listen()
    if 'exit' in command:
        respond("Goodbye!")
        break
    elif 'weather' in command:
        get_weather()
    elif 'search web for' in command:
        search_term = command.split('for')[-1]
        search_web(search_term)
    elif 'play music' in command:
        play_music()
    elif 'open' in command:
        app_name = command.split('open')[-1]
        open_app(app_name)
    elif 'tell me a joke' in command:
        tell_joke()
    else:
        
        wikipedia_search = wikipedia.summary(command, sentences=2)
        respond(wikipedia_search)


