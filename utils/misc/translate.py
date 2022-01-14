from deep_translator import GoogleTranslator, single_detection
from data.config import DETECT_KEY
from loader import db

def Translator(text):
    #lang = db.select_user()
    translated = GoogleTranslator(source=lang[5], target=lang[6]).translate(text=text)
    return translated

def AutoTranslator(text):
    lang = single_detection(text, DETECT_KEY)
    translated = GoogleTranslator(source=lang, target="uz").translate(text=text)
    return translated

