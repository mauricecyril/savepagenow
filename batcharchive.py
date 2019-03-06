import savepagenow
import time

# Add entries to dictionary. Key = Name, Value = Phone Number
websitelist = {"www.example.com",
               "www.example2.com",
                }

for k in websitelist.items():
    archive_url = savepagenow.capture_or_cache(k)
    print archive_url

    # Run the script every 30 seconds
    time.sleep(30)
