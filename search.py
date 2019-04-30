# Uses breadth-first search to determine the lowest amount of clicks required for traversal
# WIP

import webpage
from collections import deque
from queue import *


def shortest_path(start_page, end_page):
    queue = Queue()             # queue of the current path
    shortest = {}               # set of shortest path
    visited = {}                # set of all previously visited pages
    path = []                   # path of the current iteration
    length = 0                  # length of the current path
    min_length = float('inf')   # length of the shortest path

    visited[start_page] = None

    # start and end are the same
    if webpage.page(start_page) == webpage.page(end_page):
        return [webpage.page(start_page), webpage.page(end_page)], length

    # marks the sources node as visited and enqueues it
    queue.put(start_page)

    while queue:

        # de-queue a vertex from the queue
        current = queue.get()
        length += 1
        print("Current url: {}".format(webpage.page(current)))

        # current length is greater than previous lowest length
        if length >= min_length:
            return visited  # dip to next iteration?

        # iterate through all adjacent vertices (web pages)
        for i in webpage.get_links(current):

            # end page is found
            if webpage.page(i) == webpage.page(end_page):
                visited[i] = current
                path = complete_path(visited, current)  # adds the current and the previous pages to the path
                return path, length

    return shortest, min_length


# makes a list of the entire path, iterating through the visited vertices
def complete_path(visited_page, end_page):
    path = [end_page]
    i = end_page

    while visited_page[i] is not None:
        path.append(visited_page[i])
        i = visited_page[i]

    path.reverse()

    return path

