from googletrans import Translator

class MyTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_pt_to_en(self, portuguese_text):
        try:
            translation = self.translator.translate(portuguese_text, src='pt', dest='en')
            if hasattr(translation, 'text'):
                return translation.text
            else:
                return "Translation failed. The 'text' attribute is not available."
        except Exception as e:
            return f"Translation error: {str(e)}"
