
from slackbot.bot import Bot
from slacker import Slacker

from slackbot_settings import ABOUT, API_TOKEN


slack_client = Slacker(API_TOKEN)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print(ABOUT)
    main()

