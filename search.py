# Uses breadth-first search to determine the lowest amount of clicks required for traversal

import webpage
from queue import *


def shortest_path(start_page, end_page):
    queue = Queue()             # queue of the current path
    shortest = {}               # set of shortest path
    visited = {}                # set of all previously visited pages
    order = []                  # path of the current iteration
    length = 0                  # length of the current path
    min_length = float('inf')   # length of the shortest path

    visited[start_page] = None

    # start and end are the same
    if start_page == end_page:
        return [start_page, end_page]

    # marks the sources node as visited and enqueues it
    queue.put(start_page)

    while queue:

        # de-queue a vertex from the queue
        current = queue.get()
        length += 1
        print("Current url: " + current)

        # current length is greater than previous lowest length
        if length >= min_length:
            continue

        # iterate through all adjacent vertices (web pages) note: i is a link in string form
        for i in webpage.get_links(current):

            print("Current adjacent: " + i)

            # end page is found to be adjacent to the current page
            if i == end_page:
                print("\nPAGE FOUND")
                visited[i] = current
                path = complete_path(visited, i)  # adds the current and the previous pages to the path
                shortest = set_shortest(shortest, path)
                return path  # remove the return statement? might be shorter one still

            # adjacent vertex is already in the current shortest path
            # adds the rest of the adjacent vertex path to the defined shortest path
            elif i in shortest:
                visited[i] = current
                path = complete_path(visited, i)
                path_tail = complete_path(shortest, i)
                path_tail.reverse()
                path_tail.remove(i)
                order = path + path_tail
                min_length = len(order) - 1

            # add as a marked vertex if it is not already marked
            else:
                if i not in visited:
                    visited[i] = current
                    queue.put(i)

    return shortest


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
