
import re
import random

from slackbot.bot import respond_to, listen_to

from officebot.plugins import request_dict


@respond_to('random podcast', re.IGNORECASE)
def random_podcast(msg):
    response = request_dict('https://itunes.apple.com/us/rss/toppodcasts/limit=100/json')
    if response:
        entries = response['feed']['entry']
        entry = random.choice(entries)
        title = entry['title']['label']
        msg.send('Have you heard of "%s"?' % (title))


@listen_to('podcast', re.IGNORECASE)
def podcast(msg):
    msg.send('Did somebody say "podcast"? Just ask me if you want a random suggestion.')
