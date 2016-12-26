
import re
import random
import json

from slackbot.bot import respond_to, listen_to

from officebot.plugins import request_dict


@respond_to('podcast', re.IGNORECASE)
def random_podcast(msg):
    response = request_dict('https://itunes.apple.com/us/rss/toppodcasts/limit=100/json')
    if response:
        entries = response['feed']['entry']
        entry = random.choice(entries)
        title = entry['title']['label']
        artist = entry['im:artist']['label']
        summary = entry['summary']['label']
        image = entry['im:image'][2]['label']
        attachments = [
            {
                "color": "#59afe1",
                "pretext": 'Have you heard of "%s"?' % (title),
                # "author_name": artist,
                "thumb_url": image,
                # "title": title,
                "fields": [
                    {
                        "title": "Title",
                        "value": title,
                        "short": False
                    },
                    {
                        "title": "Artist",
                        "value": artist,
                        "short": False
                    },
                    {
                        "title": "Summary",
                        "value": summary,
                        "short": False
                    }
                ]
            }
        ]
        msg.send_webapi('', json.dumps(attachments))


@listen_to('podcast', re.IGNORECASE)
def podcast(msg):
    msg.send('Did somebody say "podcast"? Just ask me if you want a random suggestion.')
