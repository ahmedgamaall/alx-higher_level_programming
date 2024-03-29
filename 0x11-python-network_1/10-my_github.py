#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id"""

if __name__ == "__main__":
    import requests
    import sys
    headers = {
        'Authorization': f'Bearer {sys.argv[2]}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Accept': 'application/vnd.github+json'
        }

    web_url = 'https://api.github.com/user'
    reps = requests.get(web_url, headers=headers)
    print(reps.json().get('id'))
