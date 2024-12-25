import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
            return command
    except Exception as e:
        print("Error:", e)
        return ""
def run_alexa():
    command = take_command()
    print("Command:", command)

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'goodbye' in command:
        talk('Goodbye! Have a nice day!')
        exit()  
    else:
        talk('Please say the command again.')
while True:
    run_alexa()
