Voice Translator (Speech to Speech)
This Python script lets you speak in English, translates your speech to another language, and speaks it back using Google Text-to-Speech.

•Features:-
Voice input using your microphone
Translate to over 50 languages
Translated text is spoken aloud
Simple command-line interface

•Requirements:-
Install the necessary Python packages:
        pip uninstall googletrans googletrans-py -y
        pip install googletrans==4.0.0-rc1
        pip install pyaudio
        pip install googletrans
        pip install Translator
        pip install playsound==1.2.2
        pip install speechrecognition
        #You may need to install pyaudio manually depending on your system.

•How to Use
Run the script:
Speak a sentence in Any language 
Say the language you want to translate to (e.g., “Hindi”, “Spanish”).
The translated sentence will be spoken aloud.

•Supported Languages
Examples: Hindi, French, Spanish, Japanese, Arabic, Chinese, German, etc.
(Full list is included in the code.)

•Notes

Requires internet connection.
Make sure your microphone is connected and working.
Temporary .mp3 file is deleted after playback.
