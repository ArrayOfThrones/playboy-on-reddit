# -*- coding: utf-8 -*-
import json


def read_json(path):
    """This function opens a json file and parses it content into a python
     dict.

    Parameters
    ----------
    path : str
        The json file path.

    Returns
    -------
    json.load : dict
        The json content parsed into a python dict.

    """
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e.args[-1])


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

    last_10 = '\n'.join(submission_file[-11:-1])
    open('../data/submissions_processed.txt', 'w')
    open('../data/submissions_processed.txt', 'a').write(
        last_10
    )
