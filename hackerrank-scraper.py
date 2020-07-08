import os
import time
import requests

HEADER = {
    'cookie': '_hrank_session=5b84erandom0c3ff722563random9fe3be39ac9random2e226d569f56erandom5d79920e1d3ccrandomc3a4d88389brandom15e38f69a4217arandom1aed9338;',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

def get_ext(language):
    if language.find('cpp') != -1:
        return 'cpp'
    if language.find('python') != -1:
        return 'py'
    return ''

def get_valid_filename(s):
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_')
    while filename.find('__') != -1:
        filename = filename.replace('__', '_')
    return filename

path = './HackerRank/'
os.makedirs(path, exist_ok=True)

challenges = None
while True:
    # api = 'https://www.hackerrank.com/rest/hackers/Abhishek_G0YAL/recent_challenges?limit=221&response_version=v1'
    api = 'https://www.hackerrank.com/rest/hackers/Abhishek_G0YAL/recent_challenges?limit={limit}&response_version={version}&cursor={cursor}'
    r = requests.get(api.format(limit=16, version='v2', cursor= challenges['cursor'] if challenges else ''), headers=HEADER)
    challenges = r.json()
    for challenge in challenges['models']:
        api = 'https://www.hackerrank.com/rest/contests/master/challenges/{ch_slug}/submissions/?&offset={offset}&limit={limit}'
        r = requests.get(api.format(ch_slug=challenge['ch_slug'], offset=0, limit=12), headers=HEADER)
        submissions = r.json()
        submission_to_save = submissions['models'][0]
        for submission in submissions['models']:
            if float(submission['score']) > float(submission_to_save['score']):
                submission_to_save = submission
        submission_content = False
        while not submission_content:
            api = 'https://www.hackerrank.com/rest/contests/master/challenges/{ch_slug}/submissions/{submission_id}'
            r = requests.get(api.format(ch_slug=submission_to_save['challenge']['slug'], submission_id=submission_to_save['id']), headers=HEADER)
            print(api.format(ch_slug=submission_to_save['challenge']['slug'], submission_id=submission_to_save['id']))
            submission_content = r.json()['model']
            if not submission_content:
                time.sleep(15)
        file_name = get_valid_filename(submission_to_save['challenge']['name'].replace('-', '_')) + '.' + get_ext(submission_content['language'])
        print(file_name)
        with open(path + file_name, 'w') as f:
            f.write(f'// https://www.hackerrank.com/challenges/{challenge["ch_slug"]}/problem\n' \
                + '// ' + submission_content['status'] + '\n\n' + submission_content['code'])
    if challenges['last_page']:
        break