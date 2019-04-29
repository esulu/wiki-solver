# Wikipedia game solver main class

import webpage

print("Welcome to the Wikipedia solver! To begin, enter start/end pages, or type \"r\" for random Wikipedia pages")

# user entry
while True:
    start_page = webpage.get_url(input("Starting wikipedia page: "))
    end_page = webpage.get_url(input("Ending wikipedia page: "))

    if not start_page or not end_page:  # either start or end pages (or both) are invalid
        print("Invalid entry\n")
    else:
        break
        
# TEST CODE BELOW

print("\nEntry Complete\n")

print(webpage.page(start_page))
print(webpage.get_links(start_page))

print("\n" + webpage.page(end_page))
print(webpage.get_links(end_page))
