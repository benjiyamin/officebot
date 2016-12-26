
from slackbot.bot import Bot
from slacker import Slacker

from slackbot_settings import DESCRIPTION, API_KEY_BOT_TOKEN


slack_client = Slacker(API_KEY_BOT_TOKEN)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print(DESCRIPTION)
    main()

