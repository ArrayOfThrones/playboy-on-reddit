# -*- coding: utf-8 -*-
from helpers import read_json

import logging
import praw
import os


class Bot:
    """Class responsible for monitoring some Playboy´s r/ and, if something
    new is detected, a repost is made in r/PlayboyOnReddit.

    >>> from bot import Bot
    >>> Bot().__call__()

    """
    def __init__(self):
        self.credentials = read_json('settings.json')
        self.logging_('%(levelname)s: %(asctime)s - %(message)s')

        self.reddit = self.authenticate()

    # used in __init__
    @staticmethod
    def logging_(logging_format):
        """This functions initializes the logging function.

        Parameters
        ----------
        logging_format : str
            log format - type: time - message

        Returns
        -------

        """
        logging.basicConfig(filename='../data/run_log.log',
                            level=logging.INFO, format=logging_format)

    # used in __init__
    def authenticate(self):
        """This function logs in some reddit´s account.

        Returns
        -------

        """
        return praw.Reddit(
            user_agent=self.credentials.get('USER_AGENT'),
            client_id=self.credentials.get('CLIENT_ID'),
            client_secret=self.credentials.get('CLIENT_SECRET'),
            username=self.credentials.get('USERNAME'),
            password=self.credentials.get('PASSWORD')
        )

    # used in monitor
    def process_submission(self, submission):
        """This function process a post - extracts the information from the
        original post (title, url) and calls the post function.

        Parameters
        ----------
        submission : praw.models.reddit.submission.Submission
            A reddit´s submission.

        Returns
        -------

        """
        title = submission.title
        url = submission.url
        x_post = "[r/{}] ".format(submission.subreddit.display_name)
        source_url = 'https://www.reddit.com' + submission.permalink

        new_post_title = x_post + title

        if len(new_post_title) > 293:
            new_post_title = new_post_title[0:290] + '...'

        if submission.over_18:
            new_post_title += ' | NSFW'

        new_post_url = url
        post_to = \
            self.reddit.subreddit(self.credentials.get('SUBREDDIT_TO_POST'))

        self.new_post(post_to, new_post_title, new_post_url, source_url)
        logging.info(new_post_title)

        return new_post_url, new_post_title

    # used in process_submission
    def new_post(self, subreddit, title, url, source_url):
        """This function posts in a subreddit.

        Parameters
        ----------
        subreddit : praw.models.reddit.subreddit.Subreddit
            The subreddit´s intance.
        title : str
            Post´s title.
        url : str
            Post´s url.
        source_url : str
            Original post´s url.

        Returns
        -------

        """
        if self.credentials.get('POST_MODE') == 'direct':
            post = subreddit.submit(title, url=url)
            comment_text = \
                "[Link to original post here]({})".format(source_url)
            post.reply(comment_text).mod.distinguish(sticky=True)
        elif self.credentials.get('POST_MODE') == 'comment':
            subreddit.submit(title, url=source_url)
        else:
            logging.ERROR('Invalid POST_MODE chosen.')

    # used in __call__
    def monitor(self, submissions_found):
        """This function monitor the whitelisted subreddits seeking for new
        posts.

        Parameters
        ----------
        submissions_found : praw.models.reddit.submission.Submission
            A new reddit´s post.

        Returns
        -------

        """
        counter = 0
        for sub_reddit in self.credentials.get('SUBREDDITS_TO_MONITOR'):
            for submission in self.reddit.subreddit(sub_reddit).\
                    hot(limit=self.credentials.get('SEARCH_LIMIT')):
                if (submission.id in submissions_found) or \
                        (submission.id in self.credentials.get('IGNORE_ID')):
                    continue

                if (submission.link_flair_text in
                        self.credentials.get('BLACKLIST')) or \
                        (any([elem in submission.title for elem in
                              self.credentials.get('BLACKLIST')])):
                    continue

                self.process_submission(submission)
                submissions_found.append(submission.id)
                counter += 1

                with open('../data/submissions_processed.txt', 'a') as f:
                    f.write(submission.id + '\n')

                logging.info(str(counter) + ' submission(s) found')

    # used in __call__
    @staticmethod
    def get_submissions_processed():
        """This function reads the submissions file, parses it and return it.

        Returns
        -------
        submissions_processed : list
            A list with the already-processed submissions.

        """
        if not os.path.isfile('../data/submissions_processed.txt'):
            submissions_processed = []
        else:
            with open('../data/submissions_processed.txt', 'r') as f:
                submissions_processed = f.read()
                submissions_processed = submissions_processed.split('\n')
        return submissions_processed

    def __call__(self, *args, **kwargs):
        submissions_found = self.get_submissions_processed()
        try:
            self.monitor(submissions_found)
        except Exception as e:
            logging.warning("Random exception occurred: {}".format(e))


if __name__ == '__main__':
    Bot().__call__()
