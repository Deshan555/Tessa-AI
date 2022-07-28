import webbrowser

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

from neuralintents import GenericAssistant

import Carbon_Value

import Events

import Human_Names

import Humidity

import IMDB

import News

import Screen_Shot

import Social

import Switchs

import Temperature

import Weather

import Wikipedia_Find

import Youtube_Py

import music

import Google

import Speak

import datetime

import Send_Weather

import Send_News

import Identification_Name

import Math_Slover

text: str = ''


def time_now():

    strTime = datetime.datetime.now().strftime('%I:%M %p')

    Speak.Speak(f"Sir, the time is {strTime}")


def insta():

    name = Human_Names.name_recognizer(text)

    if name == 'none':

        base_url = "https://www.instagram.com"

    else:
        base_url = "https://www.instagram.com/"+name+"/"

        base_url = base_url.replace(" ", "")

    webbrowser.open(base_url, new=2)


def voice_Text():

    recognition = Recognizer()

    mic = Microphone()

    with mic:

        recognition.adjust_for_ambient_noise(mic, duration=0.2)

        print("Talk")

        audio = recognition.record(mic, 5)

    try:
        recognized = recognition.recognize_google(audio)

        print('You Said : ', recognized)

        return recognized

    except UnknownValueError:

        print('Unable to Recognize audio')

        return 'None'

    except RequestError as error:

        print('Error Detected : ', error)

        return 'None'

    return recognized


mappings = {'weather': Weather.get_Weather,

            'screenshot': Screen_Shot.screen_shot,

            'music': music.music_picker,

            'google': Google.search_it,

            'time': time_now,

            'news': News.get_news,

            'wikipedia': Wikipedia_Find.wiki,

            'youtube': Youtube_Py.py_youtube,

            'on_sprinkler': Switchs.sprinkler_on,

            'off_sprinkler': Switchs.sprinkler_off,

            'on_pump': Switchs.Water_on,

            'off_pump': Switchs.Water_off,

            'send_news': Send_News.send_news,

            'send_weather': Send_Weather.get_Weather,

            'humidity': Humidity.get_humidity,

            'temperature': Temperature.get_temperature,

            'carbon': Carbon_Value.get_CarbonValue,

            'events': Events.get_event,

            'my_name': Identification_Name.name_operations,

            'math': Math_Slover.Running_Math,

            'instagram': insta,

            'IMDB': IMDB.talk


            }

Assistant = GenericAssistant('intents.json', intent_methods=mappings)

Assistant.train_model()

#Assistant.save_model()

#Assistant.load_model()


while True:

    text = voice_Text()

    Assistant.request(text)