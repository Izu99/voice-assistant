import time
from features.dateTime import *
from features.openSite import *
from features.openApp import *
from features.accessSite import *
from features.calculator import *
from features.temperature import *
from features.joke import *
from features.searchWeb import *


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the properties of the engine
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)


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
# Define a function to execute commands based on user input
def process_input(problem, command):
    problem = problem.lower()  # Convert the input to lowercase for case-insensitive comparison
    if "time" in problem:
        return get_current_time()
    elif "date" in problem:
        return get_current_date()
    elif "play youtube" in problem:
        song_name = problem.replace("play youtube", "").strip()
        return play_youtube_video(song_name)
    elif "play youtube audio" in problem:
        song_name = problem.replace("play youtube audio", "").strip()
        return play_youtube_audio(song_name)
    elif "stack overflow" in problem:
        song_name = problem.replace("play youtube audio", "").strip()
        return open_stackoverflow()
    elif "wikipedia search" in command or "search wikipedia" in command:
        topic = command.replace("wikipedia search", "").replace("search wikipedia", "").strip()
        return get_wikipedia_summary(topic)
    elif "tired" in command or "playlist" in command:
        topic = command.replace("tired", "").replace("playlist", "").strip()
        return play_youtube_playlist("https://www.youtube.com/watch?v=blqSGfjiYQQ&list=PLAhHu9jhoG-ZnecB4AZnMegbqrs6uh1H_")
    elif "calculate" in command:
        return Calc(command)
    elif "temperature" in command:
        return find_temperature(command)
    elif "joke" in command:
        return get_joke()
    elif "search youtube" in command:
        search = command.replace("search youtube", "")
        return search_youtube(search)
    else:
        # Check if any recognized keyword is in the problem statement
        for keyword in [
            "youtube",
            "wikipedia",
            "google",
            "github",
            "stackoverflow",
            "facebook",
            "instagram",
            "twitter",
            "linkedin",
            "reddit",
            "edge",
            "explorer",
            "store",
            "idm",
            "vscode",
            "music",
            "anime",
        ]:
            if keyword in problem:
                open_function = globals()[
                    "open_" + keyword
                ]  # Get the corresponding function dynamically
                open_function()  # Call the function
                return f"Opening {keyword.capitalize()}..."
    return f"You said: {problem.capitalize()}"

# Define a function to speak
def speak(text):
    print(text)  # Print the response in text format
    engine.say(text)
    engine.runAndWait()
    
# Main function to orchestrate the conversation
def main():
    while True:
        problem = get_voice_input()  # Get the user's problem
        if "stop" in problem:
            speak("Goodbye!")
            break  # Exit the loop and end the program
        command = problem
        response = process_input(problem, command)  # Process the problem
        speak(response)  # Speak the response


if __name__ == "__main__":
    main()
