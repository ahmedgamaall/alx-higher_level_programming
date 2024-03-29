#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    val = ""
    if len(sys.argv) > 1:
        val = sys.argv[1]
    q_data = {"q": val}
    resp = requests.post("http://0.0.0.0:5000/search_user", q_data=q_data)
    try:
        json_resp = resp.json()
        if json_resp:
            print("[{}] {}".format(json_resp.get("id"),
                                   json_resp.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
