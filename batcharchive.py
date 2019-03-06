import savepagenow
import time

# Add entries to a list of websites
websitelist = ["www.example.com",
               "www.example2.com",
              ]

for k in websitelist:
    archive_url = savepagenow.capture_or_cache(k)
    print(archive_url)

    # Run each capture every 5 seconds
    time.sleep(5)
