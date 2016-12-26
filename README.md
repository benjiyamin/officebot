
# KittBot 2000

A running SlackBot project for my team's channels at work. It's inspired by K.I.T.T 2000
from the hit 80s TV show [Knight Rider](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series)).
Some base functions are extended from the [Limbo library](https://github.com/llimllib/limbo), as not to reinvent the wheel. 


## Keyword commands
Current plugins and commands include:


* Calculate
    - Solve a mathematical expression. (Extends Limbo).
        * `calc [expression]`
        * `calculate [expression]`
        * `solve [expression]`
* Google
    - Search for something and retrieve the top result.(Extends Limbo).
        * `google [search terms]` 
        * `look up [search terms]` 
        * `search [search terms]` 
        * `search for [search terms]` 
* Jokes
    - Say a random Chuck Norris joke. Uses the 
    [The Chuck Norris Internet Database](http://api.icndb.com) API.
        * `chuck norris joke` 
    - Say a random Chuck Norris joke, but with a team member's name instead.
        * `make [user] feel better`
        * `cheer [user] up`
    - Say a Horatio Caine style one-liner. If no quote is defined, say a random one.
        * `csi joke [quote 1] [quote 2]`
        * `horatio joke [quote 1] [quote 2]`
        * `horatio caine joke [quote 1] [quote 2]`
* Podcasts
    - Retrieves the name of a Random podcast from the iTunes Top 100. Uses the 
    [Apple iTunes](https://itunes.apple.com/) API.
        * `random podcast` 
* Random
    - Choose a random team member
        * `random member`
        * `random person`
        * `random team member`
        * `random user`
* Wikipedia
    - Retrieves some information from [Wikipedia](https://www.wikipedia.org/). (Extends Limbo).
        * `tell me about [search terms]` 
        * `tell us about [search terms]` 
        * `what do you know about [search terms]` 
        * `wiki [search terms]` 
        * `wikipedia [search terms]`


## Installation

1. Fork it!

2. Create a local clone of your fork.
    
        $ git clone https://github.com/YOUR-USERNAME/kittbot

3. Set up a clean working environment, using virtualenv.

        $ virtualenv venv -p python3
        $ source venv/bin/activate
        $ pip install -r requirements/development.txt
      
4. For the bot to work properly, a `config.yml` file must be created. You can get this from your Bot's API token from its page upon creation. Add the following line and format to `config.yml`.

        token: 'YOUR-BOT-API-KEY'


## TODOs

* Unit tests
