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
            return visited, length  # dip to next iteration?

        # iterate through all adjacent vertices (web pages) note: i is a link in string form
        for i in webpage.get_links(current):
            print("Current adjacent: {}".format(webpage.page(webpage.get_url(i))))
            # end page is found to be adjacent to the current page
            if i == webpage.page(end_page):
                print("\nPAGE FOUND")
                visited[i] = current
                path = complete_path(visited, i)  # adds the current and the previous pages to the path
                shortest = set_shortest(shortest, path)
                return path, length  # remove the return statement? might be shorter one still

            # adjacent vertex is already in the current shortest path
            elif i in shortest:
                visited[i] = current
                print("Found shortcut")
                path = complete_path(visited, i)
                path_rest = complete_path(shortest, i)

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


# current path is the shortest path if it is shorter than the previous one
def set_shortest(prev_shortest, current_shortest):
    shortest = prev_shortest

    if len(current_shortest) < len(prev_shortest):
        shortest = current_shortest

    return shortest
