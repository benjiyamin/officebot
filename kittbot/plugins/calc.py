
import re

from slackbot.bot import respond_to
from limbo.plugins import calc as lc


@respond_to('calc (.*)', re.IGNORECASE)
@respond_to('calculate (.*)', re.IGNORECASE)
@respond_to('solve (.*)', re.IGNORECASE)
def calculate(msg, eq):
    result = lc.calc(eq)
    msg.reply('%s' % result)
