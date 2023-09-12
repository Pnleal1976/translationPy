from entities.SpeechToText  import SpeechToText
from entities.TextTranslation import TextTranslator

stt = SpeechToText()
text = stt.convert_speech_to_text(microphone_input=True)
print("Recognized text: ", text)

translator = TextTranslator()
translated_text = translator.translate(text, src_lang='pt', dest_lang='en')
print(f"Original text: {text}")
print(f"Translated text: {translated_text}")