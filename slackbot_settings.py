
import os, yaml


with open('config.yml') as f:
    y = yaml.load(f)
    API_TOKEN = y['token']
    WEATHER_API_KEY = y['weather-key']


os.environ['WEATHER_API_KEY'] = WEATHER_API_KEY


DEFAULT_REPLY = "I'm sorry Dave, I'm afraid I can't do that."


ABOUT = 'I am the Knight Industries Two Thousand. You may call me "K.I.T.T."'


PLUGINS = [
    'slackbot.plugins',
    'kittbot.plugins',
]
