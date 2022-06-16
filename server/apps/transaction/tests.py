import json

import requests

web_url = "http://127.0.0.1:7788"

def test_login():
    url = "{}/login/".format(web_url)
    data = {
        "username": "test",
        "password": "test",
    }
    res = requests.post(url, json=data)
    print(json.loads(res.text))


if __name__ == "__main__":
    test_login()
