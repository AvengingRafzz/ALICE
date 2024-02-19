# File to give ALICE ears

# Import necessary modules
import ai_speak
import speech_recognition as sr


# Define a function to listen for voice input
def listen():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Print and speak a message to indicate listening for voice input
        print("Listening... waiting for voice input")
        ai_speak.speak("Listening... waiting for voice input")

        # Set the pause threshold for recognizer
        recognizer.pause_threshold = 1

        # Listen for audio input from the microphone
        audio = recognizer.listen(source)

        try:
            # Print and speak a message to indicate recognizing the voice
            print("Recognizing voice...")
            query = recognizer.recognize_google(audio)
            print(f"Rafan: {query}")
            return query

        except Exception as e:
            # Print and speak a message if there is an error or if the input couldn't be recognized
            print(e)
            print("Say that again please...")
            ai_speak.speak("Say that again please...")

            # Call the listen() function recursively to listen again
            listen()
