
import re
from urllib import parse

from slackbot.bot import respond_to

from kittbot.plugins import request_dict


@respond_to('tell me about (.*)', re.IGNORECASE)
def tell_me_about(msg, search):
    search_safe = parse.quote_plus(search)
    response = request_dict(
        'https://en.wikipedia.org/w/api.php?action=opensearch&search=%s&limit=1&namespace=0&format=json' % search_safe
    )
    if response:
        description = response[2][0]
        # link = response[3][0]
        # msg.reply('%s.\n Find out more at %s' % (description, link))
        msg.reply('%s' % (description))
