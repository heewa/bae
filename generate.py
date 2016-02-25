#!/usr/bin/env python

import re

import requests

EMOJI_JSON_URL = 'https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json'

ENV_VAR_PATTERN = re.compile('[^a-zA-Z0-9_]+')

def to_env(name):
    """Turn an emoji alias into a valid env var.
    """
    # Replace a few chars that aren't valid in env vars, but that mean something
    name = name.strip().replace('+1', 'plus_1').replace('-1', 'minus_1')

    # Everything else turns into underscores, globbing multiple together into 1
    return ENV_VAR_PATTERN.sub('_', name).upper().encode('utf8')

if __name__ == '__main__':
    for data in requests.get(EMOJI_JSON_URL, verify=True).json():
        emoji = data.get('emoji', '').encode('utf8')

        if emoji:
            for alias in data['aliases']:
                print "E_%s='%s'" % (to_env(alias), emoji)
