
import re, json, random

from slackbot.bot import respond_to


@respond_to('motivate', re.IGNORECASE)
@respond_to('motivation', re.IGNORECASE)
@respond_to('motivational', re.IGNORECASE)
@respond_to('khaled', re.IGNORECASE)
def dj_khaled(msg):
    with open('./officebot/resources/khaled.json') as data_file:
        quotes = json.load(data_file)
    quote = random.choice(quotes)
    content = quote['quote_content']
    if 'key' in content:
        content += ' :key:'
    author = quote['author']
    response = '"%s"\n- %s' % (content, author)
    msg.send(response)
