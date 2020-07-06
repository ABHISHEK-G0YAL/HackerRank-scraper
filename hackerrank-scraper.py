import time
import requests
import datetime
# import cPickle as pickle
from bs4 import BeautifulSoup

LOGIN = 'abhishek252167@gmail.com'
PASSWD = ''
ORIGIN = 'https://www.hackerrank.com'
LOGIN_URL = 'https://www.hackerrank.com/auth/login'
POST_URL = 'https://www.hackerrank.com/rest/auth/login'

# now = datetime.datetime.now()
header = {
    # 'accept': 'application/json',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en',
    # 'cache-control': 'no-cache',
    # 'content-type': 'application/json',
    # 'dnt': '1',
    # 'origin': 'https://www.hackerrank.com',
    # 'pragma': 'no-cache',
    # 'referer': 'https://www.hackerrank.com/auth/login',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
session = requests.session()
r = session.get(LOGIN_URL, headers=header)
# cookie_string = '; '.join([str(x) + '=' + str(y) for x, y in session.cookies.items()])
# csrf_token = BeautifulSoup(r.text, 'lxml').find(id='csrf-token')['content']
header.update({
    # 'cookie': cookie_string,
    # 'x-csrf-token': csrf_token
})
print(header)
login_data = {'login': LOGIN, 'password': PASSWD, 'remember_me': True, 'fallback': False}
session.post(POST_URL, data=login_data, headers=header)
api = 'https://www.hackerrank.com/rest/hackers/Abhishek_G0YAL/recent_challenges?limit=1&response_version=v1'
# api = 'https://www.hackerrank.com/rest/contests/master/challenges/jim-and-the-orders/submissions/135878037'
r = session.get(api, headers=header)
print(r.text)
