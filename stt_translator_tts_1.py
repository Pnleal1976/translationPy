# Python Libraries to Install:
# pip install SpeechRecognition
# pip install pyaudio
# pip install googletrans
# pip install pyttsx3

# language='en-US'
# language='en-GB'
# language='pt-BR'

import speech_recognition as sr
from googletrans import Translator, constants
import pyttsx3

    
# 1. FALA PARA TEXT

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário.
    # O reconhecedor de voz da biblioteca, está sendo jogado numa variável
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    # Se não reconhecer o padrão de fala, exibe mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

fala_texto = ouvir_microfone()


# 2. TRADUÇÃO

translator = Translator()
translation = translator.translate(fala_texto)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# 3. TEXTO TRADUZIDO PARA FALA

def convertTexto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

convertTexto(translation.text)
convertTexto("Deixa o like")