# PlayboyOnReddit: Reddit´s BOT

<small>_Optimized for python 3.6_</small>

Bot for monitoring hot posts in some playboy´s subreddits. 
Once a new post is found, a repost is made at 
[r/PlayboyOnReddit](https://www.reddit.com/r/playboyonreddit/).

Posts on [r/PlayboyOnReddit](https://www.reddit.com/r/PlayboyOnReddit/) are
 meant to be made only by this bot. 

----------------------

## Dependencies

For installing the requirements, in your ___venv___ or ___anaconda env___, 
just run the following command:

```shell script
pip install -r requirements.txt
```

----------------

## Server's CRON

__Bot's cron:__
```shell script
0-59/1 * * * * sh /home/ec2-user/PlayboyOnReddit/src/run_bot.sh
```

__Garbage Collector's cron:__
```shell script
00 00 01 * * sh /home/ec2-user/PlayboyOnReddit/src/run_garbage_collectors.sh
```

----------------

## Project's Structure

```bash 
.
└── PlayboyOnReddit
    ├── data
    │   └── submissions_processed.txt
    ├── docs
    │   ├── reference_articles
    │   ├── ...
    │   └── CREDITS
    ├── src
    │   ├── __init__.py
    │   ├── bot.py
    │   ├── helpers.py
    │   ├── run_bot.sh
    │   ├── run_garbage_collectors.sh
    │   └── settings.json
    ├── tests
    │   └── unittests
    │       ├── data
    │       └── __init__.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

### Directory description

- __data:__ The data dir. Group of non-script support files.
- __docs:__ The documentation dir.
- __src:__ The scripts & source code dir.
- __tests:__ The unittests dir.

-----------------------

## Usage Notes

Section aimed on clarifying some running issues.

### Running

For running it, at the `~/src` directory just run:

```shell script
python bot.py
``` 

or, if importing it as a module, just run:
````python
from bot import Bot

if __name__ == '__main__':
    Bot().__call__()
````

### JSON structure

````json
{
  "USER_AGENT": "Created by u/PlayboyOnReddit.",
  "USERNAME": "username",
  "PASSWORD": "password",
  "CLIENT_ID": "client_id",
  "CLIENT_SECRET": "client_secret",
  "SUBREDDIT_TO_POST": "PlayboyOnReddit",
  "SUBREDDITS_TO_MONITOR" : [
    "playboy",
    "Playboy_Albums",
    "playboy_playmates"
  ],
  "BLACKLIST": [
    "Request",
    "Discussion"
  ],
  "SEARCH_LIMIT": 6,
  "POST_MODE": "direct"
}
````

_obs: in order to run this application you must have a json file at `~/src/settings.json`. This json must follow the structure above._

---------------

### Monitored r/

- [r/Playboy](https://www.reddit.com/r/playboy)
- [r/Playboy_Albums](https://www.reddit.com/r/playboy_albums)

<small>_obs: If you know of any sub that should be being monitored, 
please send a direct to moderators or make a commentary on this_ 
[_post_](https://www.reddit.com/r/PlayboyOnReddit/comments/flh4i0/whats_rplayboyonreddit/). </small>

---------------
