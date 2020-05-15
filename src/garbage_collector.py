# -*- coding: utf-8 -*-
import logging


def log_cleaner():
    """This function cleans out the run_log.log file. This function is meant
    to run once per month.

    Returns
    -------

    """
    open('../data/run_log.log', 'w')


def submissions_cleaner():
    """This function cleans out the submissions_processed.txt file. This
    function is meant to run once per month.

    Returns
    -------

    """
    submission_file = \
        open('../data/submissions_processed.txt', 'r').read().split('\n')

    last_20 = '\n'.join(submission_file[-21:-1])
    open('../data/submissions_processed.txt', 'w')
    open('../data/submissions_processed.txt', 'a').write(
        last_20
    )


if __name__ == '__main__':
    logging.basicConfig(filename='../data/run_log.log', level=logging.INFO,
                        format='%(levelname)s: %(asctime)s - %(message)s')
    log_cleaner()
    logging.info('Logs file cleaned')

    submissions_cleaner()
    logging.info('Submissions file cleaned')
