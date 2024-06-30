from googletrans import Translator

def translate(text, languageDest):
    translator = Translator()
    translation = translator.translate(text, dest=languageDest).text
    
    return translation