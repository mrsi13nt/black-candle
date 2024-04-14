# black-candle
a basic web scanner for developers

# Black Candle Usage

| Option          | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| usage           | `usage: python3 black_candle.py [options] arg`                                |
| --data          | Data string to be sent through POST (e.g. "data=1")                          |
| --cookie        | HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")                      |
| -p, --payload   | You can add custom payload                                                   |
| -hh             | Run host header injection scanner                                             |
| --host          | Add custom host header (e.g. --host "www.ping.com")                          |
| -js             | Scan all java script files of full website from api keys and more...         |
| -w              | Using simple WAF detector and trying to bypass it                            |
| -rf             | Scan for reflected XSS                                                        |
| -d              | Scan for DOM XSS                                                             |
| -b              | Scan for blind xss                                                            |
| -o              | File to write output to                                                      |
| -u, --url       | Target URL (e.g. "http://www.site.com/vuln.php?id=1")                         |
| -l, --list      | Target list of urls                                                          |