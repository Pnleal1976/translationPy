from googletrans import Translator, constants

from SpeechToText import SpeechToText

class Translator:
    def __init__(self):
        self.translator = Translator()    

    def translate_from_portuguese_to_english(self, portuguese_text):
        try:
            translation = self.translator.translate(portuguese_text, src='pt', dest='en')
            return translation.text
        except Exception as e:
            return f"Translation error: {str(e)}"

        