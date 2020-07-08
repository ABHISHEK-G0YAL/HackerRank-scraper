# all solved problems
# https://www.hackerrank.com/rest/hackers/Abhishek_G0YAL/recent_challenges?limit=221&response_version=v1
# submissions of a specific challenge
# https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/?offset=0&limit=10
# a specific submission of a specific challenge
# https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/135878037

import requests

HEADER = {
    'cookie': '_hrank_session=zzz40c18c2b5f6692f5e6fa1q230fd953200f9random620ffq4be6b9bdb07e61ee4605d9efa0e8df420re0dc35ec7aa0d20d35f17a2b9d5aa378fool3a95cf7de23;'
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
api = 'https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/135878037'
r = session.get(api, headers=HEADER)
print(r.text)