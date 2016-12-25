
import re
import urllib.request
import json

from slackbot.bot import respond_to


def request_dict(request_url):
    response = urllib.request.urlopen(request_url)
    str_response = response.read().decode('utf-8')
    return json.loads(str_response)


def simple_response(message, response):
    @respond_to(message, re.IGNORECASE)
    def love(msg):
        msg.reply(response)
