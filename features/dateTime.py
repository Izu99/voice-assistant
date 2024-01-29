import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the properties of the engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Define a function to accept voice input with a timeout
def get_voice_input(timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        with sr.Microphone() as source:
            print("Speak now!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            # Use the recognizer to convert speech to text
            return r.recognize_google(audio)
        
        except sr.UnknownValueError:
            pass
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    
    print("Sorry, no voice input detected. Please type your problem.")
    return input("Type your problem: ")

# Define a function to execute commands based on user input
def process_input(problem):
    if "time" in problem:
        current_time = get_current_time()
        return current_time
    elif "date" in problem:
        current_date = get_current_date()
        return current_date
    else:
        return problem

# Define a function to speak
def speak(text):
    print(text)  # Print the response in text format
    engine.say(text)
    engine.runAndWait()

# Define a function to get the current time
def get_current_time():
    current_time = datetime.now().strftime("%I:%M %p")  # Get current time
    return f"The current time is {current_time}"

# Define a function to get the current date
def get_current_date():
    current_date = datetime.now().strftime("%A, %B %d, %Y")  # Get current date
    return f"Today is {current_date}"