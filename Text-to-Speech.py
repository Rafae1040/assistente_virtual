# Instalar a biblioteca gTTS !pip install gTTS
from gtts import gTTS

text_to_say = "God bless you"

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")

from gtts import gTTS

text_to_say = "Dio vi benedica"

language = "it"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")