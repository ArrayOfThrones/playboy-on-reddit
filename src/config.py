# Bot user agent
USER_AGENT = 'A bot that runs r/PlayboyOnReddit.'

# Subreddit where the bot will post
SUBREDDIT_TO_POST = 'PlayboyOnReddit'

# Expressions to monitor for
EXPRESSIONS_TO_MONITOR = ['playboy', 'playboy international', 'playboy us']

# Subreddits to monitor for (+ to monitor multiple subreddits; - to exclude a subreddit)
SUBREDDITS_TO_MONITOR = '+playboy+Playboy_Albuns'

# Number of submissions to check in each run
SEARCH_LIMIT = 8000

# Blacklist, dssconsider posts that contains all of the words of a index
BLACKLIST = []

# Wait time between runs (in minutes)
WAIT_TIME = 15

# Post mode (choose 'direct' or 'comment')
# 'direct' will make the bot post the direct link of the source submission
# 'comment' will make the bot post the link to the comment section of the source submission
POST_MODE = 'comment'

# Required score to cross-post a submission found by search when setting up your subreddit
REQUIRED_SCORE = 500
