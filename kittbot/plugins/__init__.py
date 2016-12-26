
import re
import requests

from slackbot.bot import respond_to


def request_dict(url):
    return requests.get(url).json()


def simple_response(message, response):
    @respond_to(message, re.IGNORECASE)
    def love(msg):
        msg.reply(response)
