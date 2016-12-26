
import re

from slackbot.bot import respond_to
from limbo.plugins import wiki as lw


@respond_to('wiki (.*)', re.IGNORECASE)
@respond_to('wikipedia (.*)', re.IGNORECASE)
@respond_to('tell us about (.*)', re.IGNORECASE)
@respond_to('tell me about (.*)', re.IGNORECASE)
@respond_to('what do you know about (.*)?', re.IGNORECASE)
def wikipedia(msg, query):
    result = lw.wiki(query)
    msg.reply('%s' % result)
