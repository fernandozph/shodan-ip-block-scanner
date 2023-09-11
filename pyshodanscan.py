import shodan
import time

SHODAN_API_KEY = "YOUR_API_KEY_HERE"
api = shodan.Shodan(SHODAN_API_KEY)


dumpfile = open("filename.format", "a")


for i in range(8):
    j = 0
    while j < 256:
        search_ip = "xxx.xxx." + str(i) + "." + str(j) # Assuming /16 class B ip xxx.xxx.0.0/16, replace x's with IP
        try:
            dumpfile.write(str(api.host(search_ip)))
        except shodan.exception.APIError as error:
            if error == "Rate limit reached. Please throttle your requests to 1 request per second.":
                time.sleep(1) # slow requests to 1 per second
                i -= 1 # reset loop
            elif str(error)  != "No information available for that IP.": #if its not just blanket nothing found error
                dumpfile.write("Unknown error while searching IP: " + search_ip + "\n")
        j += 1
