
import os, yaml


with open('config.yml') as f:
    y = yaml.load(f)
    API_TOKEN = y['token']
    WEATHER_API_KEY = y['weather-key']


os.environ['WEATHER_API_KEY'] = WEATHER_API_KEY


DEFAULT_REPLY = "I'm not sure what you mean.. Let me know if you need a list of available commands."


ABOUT = 'I am the Knight Industries Two Thousand. You may call me "K.I.T.T."'


PLUGINS = [
    'slackbot.plugins',
    'kittbot.plugins',
]
