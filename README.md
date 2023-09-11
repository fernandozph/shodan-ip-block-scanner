# shodan-ip-block-scanner
Get shodan's results for a block of IP addresses.
Pre-set for a class B IP. Originally used for Vassar College's IP range.

* Error handling for IPs with no data and throttle requests from shodan, basic error message for other errors and saves IP in file
* 1 request per second due to throttling
* Needs API key
* To use, input shodan API key and apropriate digits for IP. If not a /16 IP block, adjust for loops as necessary

Disclaimer: This is very slow, so I recommend you use other tools such as nmap or smap, which scans the shodan database at a much faster rate. But I had fun writing it :)
