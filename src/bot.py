from helpers import read_json

import logging
import time
import praw
import os


class Bot:
    def __init__(self):
        self.credentials = read_json('settings.json')
        self.logging_('%(levelname)s: %(asctime)s - %(message)s')

        self.reddit = self.authenticate()

    @staticmethod
    def logging_(logging_format):
        logging.basicConfig(level=logging.INFO, format=logging_format)

    def authenticate(self):
        logging.info("Authenticating...")
        reddit = praw.Reddit(user_agent=self.credentials.get('USER_AGENT'),
                             client_id=self.credentials.get('CLIENT_ID'),
                             client_secret=self.credentials.get('CLIENT_SECRET'))
        logging.info("Authenticated as {}".format(reddit.user.me()))

        return reddit

    def process_submission(self, submission):
        title = submission.title
        url = submission.url
        x_post = "[r/{}] ".format(submission.subreddit.display_name)
        source_url = 'https://www.reddit.com' + submission.permalink

        new_post_title = x_post + title

        if len(
                new_post_title) > 293:
            new_post_title = new_post_title[0:290] + '...'

        if submission.over_18:
            new_post_title += ' | NSFW'

        new_post_url = url
        post_to = \
            self.reddit.subreddit(self.credentials.get('SUBREDDIT_TO_POST'))

        self.new_post(post_to, new_post_title, new_post_url, source_url)
        logging.info(new_post_title)

    def new_post(self, subreddit, title, url, source_url):
        if self.credentials.get('POST_MODE') == 'direct':
            post = subreddit.submit(title, url=url)
            comment_text = \
                "[Link to original post here]({})".format(source_url)
            post.reply(comment_text).mod.distinguish(sticky=True)
        elif self.credentials.get('POST_MODE') == 'comment':
            subreddit.submit(title, url=source_url)
        else:
            logging.ERROR(
                'Invalid POST_MODE chosen. Select "direct" or "comment".')

    def is_blacklisted(self, title):
        is_black = False

        for ignored in self.credentials.get('BLACKLISTED'):
            ignored_words = ignored.split('-')

            if all(word in title for word in ignored_words):
                is_black = True

        return is_black

    def monitor(self, submissions_found):
        counter = 0
        for submission in self.reddit.subreddit(
                self.credentials.get('SUBREDDITS_TO_MONITOR')).\
                hot(limit=self.credentials.get('SEARCH_LIMIT')):
            for expression in self.credentials.get('EXPRESSIONS_TO_MONITOR'):
                if (expression in submission.title.lower()) and \
                        (submission.id not in submissions_found):
                    ignore_submission = \
                        self.is_blacklisted(submission.title.lower())

                    if not ignore_submission:
                        self.process_submission(submission)
                        submissions_found.append(submission.id)
                        counter += 1

                        with open('submissions_processed.txt', 'a') as f:
                            f.write(submission.id + '\n')

        logging.info(str(counter) + ' submission(s) found')

        logging.info('Waiting...')
        time.sleep(self.credentials.get('WAIT_TIME') * 60)

    @staticmethod
    def get_submissions_processed():
        if not os.path.isfile('submissions_processed.txt'):
            submissions_processed = []
        else:
            with open('submissions_processed.txt', 'r') as f:
                submissions_processed = f.read()
                submissions_processed = submissions_processed.split('\n')

        return submissions_processed

    def __call__(self, *args, **kwargs):
        logging.info('Reddit bot running...')
        submissions_found = self.get_submissions_processed()
        while True:
            try:
                self.monitor(submissions_found)
            except Exception as e:
                logging.warning("Random exception occurred: {}".format(e))
                time.sleep(self.credentials.get('WAIT_TIME'))


if __name__ == '__main__':
    Bot().__call__()
