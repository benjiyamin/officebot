
import re, shlex, random

from slackbot.bot import respond_to

from kittbot.plugins import request_dict


@respond_to('chuck norris joke', re.IGNORECASE)
def chuck_norris(msg):
    response = request_dict('http://api.icndb.com/jokes/random?escape=javascript')
    joke = response['value']['joke']
    msg.reply(joke)


@respond_to('make (.*) feel better', re.IGNORECASE)
@respond_to('cheer (.*) up', re.IGNORECASE)
def chuck_norris(msg, username):
    response = request_dict('http://api.icndb.com/jokes/random?escape=javascript')
    if response['type'] == 'success':
        joke = response['value']['joke']
        joke = joke.replace('Chuck Norris', username)
        msg.reply(joke)


RANDOM_LINES = (
    ('The victim was found at the end of the road. It looks like', 'it was a dead end'),
    ('The band was killed during the concert. It looks like', "it wasn't a live performance"),
    ('He was killed with a shovel. It looks like another case', 'to dig up'),
)


@respond_to('csi joke$', re.IGNORECASE)
@respond_to('csi joke (.*)', re.IGNORECASE)
@respond_to('horatio joke$', re.IGNORECASE)
@respond_to('horatio joke (.*)', re.IGNORECASE)
@respond_to('horatio caine joke$', re.IGNORECASE)
@respond_to('horatio caine joke (.*)', re.IGNORECASE)
def csi(msg, expr=None):
    set_up, punchline = random.choice(RANDOM_LINES)
    if expr:
        command_list = shlex.split(expr)
        if len(command_list) == 1:
            set_up = 'I guess you could say'
            punchline = command_list[0]
        elif len(command_list) == 2:
            set_up = command_list[0]
            punchline = command_list[1]
    response = '%s.. \n ( •__•)    ( •__•)>⌐■--■    (⌐■__■) \n ..*%s*' % (set_up, punchline)
    msg.reply(str(response))
