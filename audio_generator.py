import pyttsx3
from pydub import AudioSegment
import re
import os

def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

def text_to_speech(text, voice_id, filename):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.save_to_file(text, filename)
    engine.runAndWait()

def split_script(script_text):
    pattern = r'(\w+):\s*(.+)'
    return re.findall(pattern, script_text)

def generate_dual_voice_audio(script_text, output_filename="podcast.wav"):
    voices = get_voices()
    if len(voices) < 2:
        raise RuntimeError("Less than 2 voices found. Please install more voices on your system.")

    voice_mike = voices[0].id
    voice_emma = voices[1].id

    segments = split_script(script_text)
    temp_files = []

    for idx, (speaker, line) in enumerate(segments):
        print(f"Generating audio for {speaker}: {line[:30]}...")
        voice = voice_mike if speaker.lower() == 'mike' else voice_emma
        temp_file = f"temp_segment_{idx}.wav"
        text_to_speech(line, voice, temp_file)
        temp_files.append(temp_file)

    combined_audio = AudioSegment.empty()
    for f in temp_files:
        seg = AudioSegment.from_wav(f)
        combined_audio += seg + AudioSegment.silent(duration=400)  

    combined_audio.export(output_filename, format='wav')
    print(f"Saved combined audio as {output_filename}")

    for f in temp_files:
        os.remove(f)
