
# import re
#
# from slackbot.bot import respond_to
# from limbo.plugins import weather as lw
#
#
# @respond_to('weather$', re.IGNORECASE)
# @respond_to('weather by (.*)', re.IGNORECASE)
# @respond_to('weather at (.*)', re.IGNORECASE)
# @respond_to('weather near (.*)', re.IGNORECASE)
# def weather(msg, location=32256):
#     result = lw.weather(str(location))
#     msg.reply('%s' % result)
