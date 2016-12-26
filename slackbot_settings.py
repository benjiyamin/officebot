
import os, yaml


with open('config.yml') as f:
    y = yaml.load(f)
    API_KEY_BOT_TOKEN = y['api-key-bot-token']
    API_KEY_WEATHER = y['api-key-weather']
    NAME = y['name']
    DESCRIPTION = y['description']
    COMPANY = y['company']
    DEFAULT_REPLY = y['default-reply']


# Need this for the Limbo weather plugin to work properly
os.environ['WEATHER_API_KEY'] = API_KEY_WEATHER


# Need this for the Slackbot framework to work correctly
API_TOKEN = API_KEY_BOT_TOKEN


PLUGINS = [
    'slackbot.plugins',
    'officebot.plugins',
]
