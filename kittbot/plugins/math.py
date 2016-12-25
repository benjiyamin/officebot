
import re
from urllib import parse

from slackbot.bot import respond_to

from kittbot.plugins import request_dict


@respond_to('solve (.*)', re.IGNORECASE)
def solve(msg, expr):
    expr_safe = parse.quote_plus(expr)
    response = request_dict('http://api.mathjs.org/v1/?expr=%s' % expr_safe)
    msg.reply(str(response))
