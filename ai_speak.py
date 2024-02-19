# File to give ALICE voice

# Import the pyttsx3 module for text-to-speech conversion
import pyttsx3

# Initialize the voice engine with "sapi5" speech API
voice_engine = pyttsx3.init("sapi5")

# Set the speaking rate to 150 words per minute
voice_engine.setProperty("rate", 150)

# Set the volume level to maximum (1.0)
voice_engine.setProperty("volume", 1)

# Get the available voices and set the voice to the second one (index 1)
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voices[1].id)


# Define a function to speak the given audio
def speak(audio):
    # Use the voice engine to say the given audio
    voice_engine.say(audio)

    # Run the voice engine to wait until the speech is completed
    voice_engine.runAndWait()
