#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys
    reps = requests.get(sys.argv[1])
    if (reps.ok):
        print(reps.text)
    else:
        print(f"Error code: {reps.status_code}")
