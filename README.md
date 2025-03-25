# 🤖 Sistema de Assistência Virtual

## 📌 Descrição do Projeto
Este projeto tem como objetivo desenvolver um **Sistema de Assistência Virtual** utilizando **PLN (Processamento de Linguagem Natural)** e bibliotecas do curso. O assistente será capaz de **converter texto em fala (Text-to-Speech) e fala em texto (Speech-to-Text)**, além de realizar ações automatizadas com comandos de voz. 🎙️🔊

## 🎯 Funcionalidades
✅ **Text-to-Speech (TTS)**: Transforma texto digitado em áudio. 🔊  
✅ **Speech-to-Text (STT)**: Converte fala em texto, permitindo interação por comandos de voz. 🗣️➡️📝  
✅ **Automação por Comando de Voz**: Possibilidade de abrir **Wikipedia**, **YouTube** e localizar farmácias próximas. 🌍📍  

## 🛠 Tecnologias Utilizadas
O projeto utiliza as seguintes bibliotecas em **Python**:

🔹 `speech_recognition` – Para reconhecimento de voz. 🎤  
🔹 `pyttsx3` – Para síntese de voz (Text-to-Speech). 🔈  
🔹 `wikipedia-api` – Para pesquisas automáticas na Wikipedia. 📖  
🔹 `geopy` – Para localização de estabelecimentos próximos. 🌍  
🔹 `webbrowser` – Para abrir sites automaticamente. 🌐  

## 📌 Exemplos Disponíveis
O projeto conta com dois exemplos para facilitar a implementação:

### 🎙 Speech-to-Text (Fala para Texto)

```python
#import section
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer

#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Sorry, the service is not available")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#function to respond to commands
def respond(text):
    print("Text from get audio " + text)
    if 'youtube' in text:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on youtube")
    elif 'search' in text:
        speak("What do you want to search for?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

while True:
    print("I am listening...")
    text = get_audio()
    respond(text)
```

### 🔊 Text-to-Speech (Texto para Fala)

```python
# Instalar a biblioteca gTTS !pip install gTTS
from gtts import gTTS

text_to_say = "God bless you"

language = "en"

gtts_object = gTTS(text = text_to_say, lang = language, slow = False)
gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")

text_to_say = "Dio vi benedica"

language = "it"

gtts_object = gTTS(text = text_to_say, lang = language, slow = False)
gtts_object.save("/content/gtts.wav")

Audio("/content/gtts.wav")
```

## 📌 Conclusão
Este projeto demonstrou como é possível criar um **assistente virtual** utilizando **Processamento de Linguagem Natural** e bibliotecas do Python. O sistema permite transformar texto em áudio e reconhecer comandos de voz para realizar ações automatizadas.

Essas funcionalidades podem ser úteis para diversas aplicações, como assistentes pessoais, acessibilidade para pessoas com deficiência visual e integração com sistemas de automação residencial. Além disso, o código pode ser aprimorado para suportar novos comandos e interações mais avançadas. 🚀🎙️

#Python #AssistenteVirtual #InteligênciaArtificial #PLN #SpeechRecognition #Automação

