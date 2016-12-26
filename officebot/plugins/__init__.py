
import re
import requests

from slackbot.bot import respond_to


def request_dict(url):
    return requests.get(url).json()


def simple_send(message, response):
    @respond_to(message, re.IGNORECASE)
    def res(msg):
        msg.send(response)
