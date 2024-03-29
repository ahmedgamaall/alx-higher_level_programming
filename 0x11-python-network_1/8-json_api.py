#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    from requests import post
    from sys import argv

    q_data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post('http://0.0.0.0:5000/search_user', q_data)

    type_resp = response.headers['content-type']

    if type_resp == 'application/json':
        resp = response.json()
        id = resp.get('id')
        name = resp.get('name')
        if (resp != {} and id and name):
            print("[{}] {}".format(id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
