import os
import torchaudio
import streamlit as st
from tortoise.api import TextToSpeech

# Initialize Tortoise TTS
tts = TextToSpeech()

# Function to generate speech from text
def text_to_speech(text, preset="fast"):
    st.write("Generating speech... This may take a while.")
    
    # Generate speech using the Tortoise TTS API
    generated = tts.tts_with_preset(text, preset=preset)
    
    # Save the generated audio as a wav file using torchaudio
    output_path = "output.wav"
    torchaudio.save(output_path, generated.squeeze(0).cpu(), sample_rate=24000)
    return output_path

# Streamlit interface
st.title("Text to Speech Converter")

# Take user input as text
text = st.text_input("Enter text you want to convert to speech", "Hello, welcome to the Tortoise TTS text-to-speech demonstration.")

# Button to generate speech
if st.button("Generate Speech"):
    output_path = text_to_speech(text)

    # Read and play the audio file in the Streamlit app
    audio_file = open(output_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
