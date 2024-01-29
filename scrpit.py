import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the properties of the engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Define a function to listen to the microphone and repeat what you say
def listen_and_repeat():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

    try:
        # Use the recognizer to convert speech to text
        said = r.recognize_google(audio)

        # Use the engine to say what you said
        engine.say(f"You said: {said}")
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the function to listen to the microphone and repeat what you say
listen_and_repeat()
