#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    reps = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(reps) as response:
            print(response.read().decode())
    except urllib.error.URLError as error:
        print(f"Error code: {error.code}")
