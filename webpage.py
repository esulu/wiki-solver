# handles all things to do with Wikipedia web pages

import urllib.request
from urllib import error
import re

# link to a random Wikipedia article
random = 'https://en.wikipedia.org/wiki/Special:Random'
# link to the Wikipedia main page
main = 'https://en.wikipedia.org/wiki/Main_Page'


def page(link):  # returns a string of the link; link is a HTTPResponse representation of the actual link
    return link.geturl()


def print_data(path):  # returns a list of the path with the links
    data = []
    for i in path:
        data.append(i)

    return data


def get_url(link):  # returns the HTTPResponse of the link; link is a string representation of a url
    try:
        if link.lower() == 'r':
            url = urllib.request.urlopen(random)
        else:
            url = urllib.request.urlopen(link)
        return url

    except urllib.error.URLError:
        return None
    except ValueError:
        return None


def get_links(link):  # returns a set of all links on that page; link is a string representation of a url
    link = get_url(link)
    source = str(link.read())  # source is a string of the page source

    links = set()
    regex = re.compile('(?:a href=("/wiki/[^:]*?"))')
    path_list = regex.findall(source)

    # iterates through every link on the page
    for i in path_list:
        links.add('https://en.wikipedia.org' + i.split("\"")[1])  # adds the link

    links.discard(main)  # removes all references to the main page

    return links

