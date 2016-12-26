
# OfficeBot

A running SlackBot project for my team's channels at work. It's designed
to provide basic everyday functions. I've used the
[slackbot](https://github.com/lins05/slackbot) framework for some 
structure. In addition, some base functions are extended from the 
[Limbo library](https://github.com/llimllib/limbo), as not to reinvent 
the wheel. 


## Keyword commands
Current plugins and commands include:


* Calculate
    - Solve a mathematical expression. (Extends Limbo).
        * `calc [expression]`
        * `calculate [expression]`
        * `solve [expression]`
* General
    - Show the available list of officebot commands.
        * `commands`
        * `what can you do`
        * `what you can do`
    - Show the bot's description. This should be defined in `config.yml` as `description`.
        * `about yourself` 
    - Show the bot's company. This should be defined in `config.yml` as `company`.
        * `who do you work for` 
    - Show the bot's description. This should be defined in `config.yml` as `name`.
        * `your name` 
* Google
    - Search for something and retrieve the top result. (Extends Limbo).
        * `google [query]` 
        * `look up [query]` 
        * `search [query]` 
        * `search for [query]` 
* Jokes
    - Say a random Chuck Norris joke. Uses the 
    [The Chuck Norris Internet Database](http://api.icndb.com) API.
        * `chuck norris joke` 
    - Say a random Chuck Norris joke, but with a team member's name 
    instead.
        * `make [user] feel better`
        * `cheer [user] up`
        * `cheer up [user]`
    - Say a Horatio Caine style one-liner. If no quote is defined, say a 
    random one.
        * `csi joke [quote 1] [quote 2]`
        * `horatio joke [quote 1] [quote 2]`
        * `horatio caine joke [quote 1] [quote 2]`
* Map
    - Show a map of an area. (Extends Limbo).
        * `map [query]` 
        * `show me [query]` 
        * `where is [query]` 
* Podcasts
    - Retrieves the name of a Random podcast from the iTunes Top 100. Uses the 
    [Apple iTunes](https://itunes.apple.com/) API.
        * `podcast` 
* Random
    - Choose a random team member.
        * `random member`
        * `random person`
        * `random team member`
        * `random user`
    - Flip a coin.
        * `coin flip`
        * `flip a coin`
* Wikipedia
    - Retrieves some information from 
    [Wikipedia](https://www.wikipedia.org/). (Extends Limbo).
        * `what do you know about [query]` 
        * `wiki [query]` 
        * `wikipedia [query]`


## Installation

1. Fork it!

2. Create a local clone of your fork.
    
        $ git clone https://github.com/YOUR-USERNAME/officebot

3. Set up a clean working environment, using virtualenv.

        $ virtualenv venv -p python3
        $ source venv/bin/activate
        $ pip install -r requirements/development.txt
      
4. For the bot to work properly, a `config.yml` file must be created. 
You can get this from your Bot's API token from its page upon creation. 
Add the following line and format to `config.yml`.

        api-key-bot-token: 'YOUR-BOT-API-KEY'

5. In order to run office bot, execute the main script. 

        `$ python run.py`.


## TODOs

* Unit tests
