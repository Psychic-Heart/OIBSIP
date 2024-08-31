import speech_recognition as s
from gtts import gTTS
from pydub import AudioSegment
from google.colab import files
import time
recognize = s.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    display(Audio("response.mp3", autoplay=True))

def convert_m4a_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file, format="m4a")
    wav_file = "audio.wav"
    audio.export(wav_file, format="wav")
    return wav_file

def listen(audio_file):
    wav_file = convert_m4a_to_wav(audio_file)
    with s.AudioFile(wav_file) as source:
        audio = recognize.record(source)
        try:
            return recognize.recognize_google(audio)
        except s.UnknownValueError:
            return "Could not understand audio"
        except s.RequestError as e:
            return f"Could not request results; {e}"

def voiceAssistant():
    speak("Hello! I'm your Voice Assistant. Please upload an audio file.")

    uploaded = files.upload()

    if uploaded:
        audio_file = list(uploaded.keys())[0]  # Get the first uploaded file
        display(Audio("audio.wav", autoplay=True))
        command = listen(audio_file).lower()
        time.sleep(3)
        if "hello" in command:
            speak("Hello!")
        elif "how are you" in command:
            speak("I am fine, thank you!")
        elif "who are you" in command:
            speak("I am your voice assistant.")
        elif "stop" in command:
            speak("Goodbye!")
        else:
            speak("I did not understand that command.")
    else:
        speak("No file was uploaded.")

voiceAssistant()
