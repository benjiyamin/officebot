
import re
import random

from slackbot.bot import respond_to

from run import slack_client


@respond_to('random user', re.IGNORECASE)
@respond_to('random member', re.IGNORECASE)
@respond_to('random team member', re.IGNORECASE)
@respond_to('random person', re.IGNORECASE)
def random_member(msg):
    response = slack_client.users.list()
    users = response.body['members']
    user = random.choice(users)
    username = '<@'+ user['name'] +'>'
    msg.reply('Hmmmm.. I choose %s!' % (username))


@respond_to('flip a coin', re.IGNORECASE)
@respond_to('coin flip', re.IGNORECASE)
def coin_flip(msg):
    options = (
        'heads',
        'tails',
    )
    side = random.choice(options)
    msg.reply("Hmmmm.. Looks like it's %s!" % (side))
