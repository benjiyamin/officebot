
# import re
#
# from slackbot.bot import respond_to
# from limbo.plugins import google as lg
#
#
# @respond_to('lunch$', re.IGNORECASE)
# @respond_to('restaurants$', re.IGNORECASE)
# @respond_to('food$', re.IGNORECASE)
# @respond_to('lunch by (.*)', re.IGNORECASE)
# @respond_to('restaurants by (.*)', re.IGNORECASE)
# @respond_to('food by (.*)', re.IGNORECASE)
# @respond_to('lunch at (.*)', re.IGNORECASE)
# @respond_to('restaurants at (.*)', re.IGNORECASE)
# @respond_to('food at (.*)', re.IGNORECASE)
# @respond_to('lunch near (.*)', re.IGNORECASE)
# @respond_to('restaurants near (.*)', re.IGNORECASE)
# @respond_to('food near (.*)', re.IGNORECASE)
# def yelp(msg, location=32256):
#     result = lg.google('food near %s' % location)
#     msg.reply('%s' % result)
