
import re
import random

from slackbot.bot import respond_to

from kittbot.plugins import request_dict


@respond_to('random podcast', re.IGNORECASE)
def random_podcast(msg):
    response = request_dict('https://itunes.apple.com/us/rss/toppodcasts/limit=100/json')
    if response:
        entries = response['feed']['entry']
        entry = random.choice(entries)
        title = entry['title']['label']
        msg.reply('Have you heard of the podcast "%s"?' % (title))
