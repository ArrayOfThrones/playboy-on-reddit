## PlayboyOnReddit

Optimized for python 3.6

Bot for monitoring hot posts in some playboy´s subreddits. 
Once a new post is found, a repost is made at [r/PlayboyOnReddit](https://www.reddit.com/r/playboyonreddit/).

Posts on [r/PlayboyOnReddit](https://www.reddit.com/r/PlayboyOnReddit/) are meant to be made only by this bot. 

----------------------

### Dependencies

For installing the requirements, in your ___venv___ or ___anaconda env___, 
just run the following command:

```shell script
pip install -r requirements.txt
```

----------------

### Project's Structure

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
    │   └── bot.py
    ├── tests
    │   └── unittests
    │       ├── data
    │       └── __init__.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

#### Directory description

- __docs:__ The documentation dir.
- __src:__ The scripts & source code dir.
- __tests:__ The unittests dir.

-----------------------

### Usage Notes

Section aimed on clarifying some running issues.

#### Running

For running it, at the `~/src` directory just run the follow command:

```shell script
python bot.py
``` 

#### JSON Structure

````json
{
  "USER_AGENT": "Created by u/brnpaes.",
  "USERNAME": "username",
  "PASSWORD": "password",
  "CLIENT_ID": "client_id",
  "CLIENT_SECRET": "client_secret",
  "SUBREDDIT_TO_POST": "PlayboyOnReddit",
  "SUBREDDITS_TO_MONITOR" : [
    "playboy", 
    "Playboy_Albums"
  ],
  "SEARCH_LIMIT": 1,
  "WAIT_TIME": 3,
  "POST_MODE": "direct"
}
````
---------------

#### Monitored r/

- [r/Playboy](https://www.reddit.com/r/playboy)
- [r/Playboy_Albums](https://www.reddit.com/r/playboy_albums)

---------------
