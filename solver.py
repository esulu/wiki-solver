# Wikipedia game solver main class

import webpage

# User entry
while True:
    start_page = webpage.get_url(input("Starting wikipedia page: "))
    end_page = webpage.get_url(input("Ending wikipedia page: "))

    if not start_page or not end_page:  # either start or end pages (or both) are invalid
        print("Invalid entry\n")
    else:
        break

print("done")
