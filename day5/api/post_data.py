"""This is a client side request that we're sending to the Flask application to post data to the route /data with id=1"""

import requests
res = requests.post('http://127.0.0.1:5000/data/1', json={"user_name":"daniel"})
if res.ok:
    print(res.json())