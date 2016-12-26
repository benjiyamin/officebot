
import re

from slackbot.bot import respond_to
from limbo.plugins import google as lg


@respond_to('google (.*)', re.IGNORECASE)
@respond_to('search (.*)', re.IGNORECASE)
@respond_to('search for (.*)', re.IGNORECASE)
@respond_to('look up (.*)', re.IGNORECASE)
def google(msg, query):
    result = lg.google(query)
    msg.send('%s' % result)
