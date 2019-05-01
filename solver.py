# Wikipedia game solver main class

import webpage
import search

print("Welcome to the Wikipedia solver! To begin, enter start/end pages, or type \"r\" for random Wikipedia pages")

# user entry
while True:
    start_page = webpage.get_url(input("Starting wikipedia page: "))
    end_page = webpage.get_url(input("Ending wikipedia page: "))

    if not start_page or not end_page:  # either start or end pages (or both) are invalid
        print("Invalid entry\n")
    else:
        break

print("\nEntry Complete\n")


path = search.shortest_path(webpage.page(start_page), webpage.page(end_page))
length = 0

for i in path:
    length += 1

print(webpage.print_data(path))
print("Clicks Required: " + str(length-1))
print("end of program")
