# handles all things to do with Wikipedia web pages

import urllib.request
from urllib import error
import re

# link to a random Wikipedia article
random = 'https://en.wikipedia.org/wiki/Special:Random'


def get_url(source):

    try:
        if source.lower() == 'r':
            url = urllib.request.urlopen(random)
        else:
            url = urllib.request.urlopen(source)
        return url.geturl()

    except urllib.error.URLError:
        return None
    except ValueError:
        return None
