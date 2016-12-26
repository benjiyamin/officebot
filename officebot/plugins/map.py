
import re

from slackbot.bot import respond_to
from limbo.plugins import map as lm


@respond_to('where is (.*)', re.IGNORECASE)
@respond_to('show me (.*)', re.IGNORECASE)
@respond_to('map (.*)', re.IGNORECASE)
def google(msg, query):
    result = lm.makemap(query)
    msg.send('%s' % result)
