
import os


API_TOKEN = os.environ.get('KITT_BOT_TOKEN')


DEFAULT_REPLY = "I'm sorry Dave, I'm afraid I can't do that."


ABOUT = 'I am the Knight Industries Three Thousand. You may call me "K.I.T.T."'


PLUGINS = [
    'slackbot.plugins',
    'kittbot.plugins',
]
