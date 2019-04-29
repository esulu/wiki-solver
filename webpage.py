# Handles all things to do with Wikipedia web pages

import urllib.request
from urllib import error
import re


def get_url(source):

    try:
        url = urllib.request.urlopen(source)
        return url

    except urllib.error.URLError:
        return None
    except ValueError:
        return None
