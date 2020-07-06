# all solved problems
# https://www.hackerrank.com/rest/hackers/Abhishek_G0YAL/recent_challenges?limit=221&response_version=v1
# submissions of a specific challenge
# https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/?offset=0&limit=10
# a specific submission of a specific challenge
# https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/135878037

import requests

LOGIN_DATA = {
    'login': 'abhishek252167@gmail.com',
    'password': '',
    'remember_me': True,
    'fallback': False
}
LOGIN_URL = 'https://www.hackerrank.com/auth/login'
POST_URL = 'https://www.hackerrank.com/rest/auth/login'

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
session = requests.session()
session.get(LOGIN_URL, headers=HEADER)
# cookie_string = '; '.join([str(x) + '=' + str(y) for x, y in session.cookies.items()])
HEADER['cookie'] = f'_hrank_session={session.cookies.get_dict()["_hrank_session"]};'
login = session.post(LOGIN_URL, data=LOGIN_DATA, headers=HEADER)
print(login.text)
# HEADER['x-csrf-token'] = login.json()['csrf_token']