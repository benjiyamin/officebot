
# KittBot 3000

A running SlackBot project for my team's channels at work. It's inspired by K.I.T.T 3000
from the hit 80s TV show [Knight Rider](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series))


## Keyword commands
Current plugins and commands include:

* General
    - `random person`: Chooses a random team member.
* Jokes
    - `chuck norris joke`: Says a random Chuck Norris joke. 
    Uses the [The Chuck Norris Internet Database](http://api.icndb.com) API.
    - `csi joke [quote 1] [quote 2]`: Constructs a Horatio Caine style one-liner. 
    If no quote is defined, say a random one. 
* Math
    - `solve [expression]`: Solves a mathematical expression. Uses the [mathjs.org]() API.
* Podcasts
    - `random podcast`: Retrieves the name of a Random podcast from the iTunes Top 100. 
    Uses the [Apple iTunes](https://itunes.apple.com/) API.
* Wikipedia
    - `tell me about [search terms]`: Retrieves some information from [Wikipedia](https://www.wikipedia.org/) about something. 
    Uses the [MediaWiki](https://www.mediawiki.org/wiki/API:Main_page) API.


## Installation

1. Fork it!

2. Create a local clone of your fork.
    
        $ git clone https://github.com/YOUR-USERNAME/kittbot

3. Set up a clean working environment, using virtualenv.

        $ virtualenv venv -p python3
        $ source venv/bin/activate
        $ pip install -r requirements/development.txt
      
4. For the bot to work properly, the system variable `KITT_BOT_TOKEN` must be defined. You can get this from your Bot's 
page when you create one for your group.

        $ export KITT_BOT_TOKEN='YOUR-BOT-API-KEY'


## TODOs

* Unit tests
