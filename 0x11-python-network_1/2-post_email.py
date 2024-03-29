#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    post_date = urllib.parse.urlencode({"email": sys.argv[2]})
    post_date = post_date.encode('ascii')
    reps = urllib.request.Request(sys.argv[1], post_date)
    with urllib.request.urlopen(reps) as response:
        print(response.read().decode())
