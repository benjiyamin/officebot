
import re
import random

from slackbot.bot import respond_to

from slackbot_settings import ABOUT
from kittbot.plugins import simple_response
from run import slack_client


simple_response('I love you', 'I love you too!')
simple_response('Thank you', "Don't mention it.")
simple_response('yourself', ABOUT)


@respond_to('random person', re.IGNORECASE)
def random_person(msg):
    response = slack_client.users.list()
    users = response.body['members']
    user = random.choice(users)
    username = '<@'+ user['name'] +'>'
    msg.reply('Hmmmm.. I choose %s!' % (username))
