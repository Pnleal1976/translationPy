from googletrans import Translator
import os
import speech_recognition as sr
from Translator import MyTranslator, Translator
from SpeechToText import SpeechToText

def main():
    while True:
        print("Menu:")
        print("Type '1' to choose an audiofile.")
        print("Type '2' to start microphone and voice recorder.")
        print("Type '3' to Exit.")

        choice = input("Choose an option: ")

        if choice == "1":
            audiofile_path = "Teste2.wav"
            if os.path.isfile(audiofile_path):
                # Do the audio file processing here
                print(f"You chose to insert the file: {audiofile_path}")

                # Audio transcription1.
                stt = SpeechToText()
                text = stt.convert_audiofile_to_text("Teste2.wav")
                print("Recognized text: ", text)
            else:
                print("File Not Found!")
                break

        elif choice == "2":
            stt = SpeechToText()
            audioText = stt.convert_speech_to_text(microphone_input=True)
            # Do the processing of the recorded audio here
            

            # Translation here.
            translator = Translator()  # Create an instance of the Translator class
            translated_text = translator.translate(audioText, src='pt', dest='en')  # Use the method to translate
            print(f"Original text: {audioText}")
            print(f"Translated text: {translated_text}")
            break
           


        elif choice == "3":
            print("Ending Program.")
            break
        else:
            print("Invalid option! Try again.")

        


if __name__ == "__main__":
    main()