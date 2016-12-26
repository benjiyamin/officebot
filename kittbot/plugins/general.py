
import re
import json

from slackbot_settings import ABOUT
from kittbot.plugins import simple_response
from slackbot.bot import respond_to


simple_response('I love you', 'I love you too!')
simple_response('Thank you', "Don't mention it.")
simple_response('yourself', ABOUT)


@respond_to('commands', re.IGNORECASE)
@respond_to('what can you do', re.IGNORECASE)
@respond_to('what you can do', re.IGNORECASE)
def commands(msg):
    attachments = [
    {
        'author_name': 'See a summary of my valid commands here.',
        'author_link': 'https://github.com/benjiyamin/kittbot#keyword-commands',
        'color': '#59afe1'
    }]
    msg.send_webapi('', json.dumps(attachments))


# @respond_to('github', re.IGNORECASE)
# def github(msg):
#     attachments = [
#     {
#         'fallback': 'Fallback text',
#         'author_name': 'Author',
#         'author_link': 'http://www.github.com',
#         'text': 'Some text',
#         'color': '#59afe1'
#     }]
#     msg.send_webapi('', json.dumps(attachments))
