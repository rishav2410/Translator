from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
LANGUAGES = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',
    'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be',
    'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'chinese simplified': 'zh-cn', 'chinese traditional': 'zh-tw',
    'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl',
    'english': 'en', 'french': 'fr', 'german': 'de', 'greek': 'el',
    'gujarati': 'gu', 'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is',
    'italian': 'it', 'japanese': 'ja', 'kannada': 'kn', 'korean': 'ko',
    'latin': 'la', 'malayalam': 'ml', 'marathi': 'mr', 'nepali': 'ne',
    'norwegian': 'no', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
    'romanian': 'ro', 'russian': 'ru', 'sanskrit': 'sa', 'serbian': 'sr',
    'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'spanish': 'es',
    'swahili': 'sw', 'swedish': 'sv', 'tamil': 'ta', 'telugu': 'te',
    'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur',
    'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi',
    'yoruba': 'yo', 'zulu': 'zu'
}
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Sorry, could not understand. Please say again...")
        return "None"
    return query.lower()
def destination_language():
    print("Enter the language you want to convert into (e.g. Hindi, French, Spanish):")
    lang = takecommand()
    while lang == "None":
        lang = takecommand()
    return lang.lower()
query = takecommand()
while query == "None":
    query = takecommand()
to_lang = destination_language()
while to_lang not in LANGUAGES:
    print("Language not available, please try again...")
    to_lang = destination_language()
lang_code = LANGUAGES[to_lang]
translator = Translator()
translation = translator.translate(query, dest=lang_code)
text = translation.text
tts = gTTS(text=text, lang=lang_code, slow=False)
tts.save("captured_voice.mp3")
playsound("captured_voice.mp3")
os.remove("captured_voice.mp3")
print(f"Translated Text ({to_lang.title()}): {text}")