#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    resp = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(resp) as response:
        resp_cnt = response.read()
        print("Body response:")
        print(f"\t- type: {type(resp_cnt)}")
        print(f"\t- content: {resp_cnt}")
        print(f"\t- utf8 content: {resp_cnt.decode()}")
