
import os, yaml


# API_TOKEN = os.environ.get('KITT_BOT_TOKEN')
with open('config.yml') as f:
    API_TOKEN = yaml.load(f)['token']


DEFAULT_REPLY = "I'm sorry Dave, I'm afraid I can't do that."


ABOUT = 'I am the Knight Industries Two Thousand. You may call me "K.I.T.T."'


PLUGINS = [
    'slackbot.plugins',
    'kittbot.plugins',
]
