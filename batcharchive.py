import savepagenow
import archiveis
import time

# Add entries to a list of websites
#websitelist = ["www.example.com",
 #              "www.example2.com",
#              ]

# Or create a textfile called websitefile.txt
# and put a seperate url on each line. Then
# save the text file to the same path as this
# python script.
#
# Open a text file with the list in Read Mode
websitefile = open("websitefile.txt", "r").read().splitlines()

# if using the text file method, replace "websitelist" in
# the following loop to "websitefile"
for k in websitefile:
    archive_url = savepagenow.capture_or_cache(k)
    print(archive_url)
    archiveis_url = archiveis.capture(k)
    print(archiveis_url)

    # Run each capture every 5 seconds
    time.sleep(1)
