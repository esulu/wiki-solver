# Uses breadth-first search to determine the lowest amount of clicks required for traversal

import webpage
from queue import Queue


def shortest_path(start_page, end_page):

    queue = Queue()             # queue of the current path
    shortest = []               # list of shortest path
    visited = {}                # set of all previously visited pages
    length = 0                  # length of the current path
    min_length = float('inf')   # length of the shortest path

    visited[start_page] = None

    # start and end are the same
    if webpage.page(start_page) == webpage.page(end_page):
        return [webpage.page(start_page), webpage.page(end_page)], length

    return shortest, min_length


