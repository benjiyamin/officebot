
import re
import json

from slackbot_settings import DESCRIPTION, NAME, COMPANY
from officebot.plugins import simple_send
from slackbot.bot import respond_to


# General responses
simple_send('i love you', 'I love you too!')
simple_send('thank you', "Don't mention it.")


# Bot Info
simple_send('about yourself', DESCRIPTION)
simple_send('who do you work for', 'I work for ' + COMPANY)
simple_send('your name', 'My name is ' + NAME)


@respond_to('commands', re.IGNORECASE)
@respond_to('what can you do', re.IGNORECASE)
@respond_to('what you can do', re.IGNORECASE)
def commands(msg):
    attachments = [
    {
        'author_name': 'See a summary of my valid commands here.',
        'author_link': 'https://github.com/benjiyamin/officebot#keyword-commands',
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
