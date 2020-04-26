import os
import sys
import requests
from bs4 import BeautifulSoup


def check_url(url):
    if '.' in url:
        return True
    else:
        return False


def save_file(name, page):
    with open(name, 'w', encoding='utf-8') as fi:
        fi.write(page)


def page_load(url):
    if not url.startswith('https:'):
        url = "https://" + url
    r = requests.get(url)
    if r.status_code == 200:
        return True, r.text, url
    else:
        return False, ''


def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    res = []
    for item in soup.body.children:
        if type(item) == type(soup.p):
            res.append(item.get_text(strip=True))
    return '\n'.join(res)


# Create target Directory if don't exist
dir_name = sys.argv[1] if len(sys.argv) > 1 else '.'
if (dir_name != '.') and (not os.path.exists(dir_name)):
    os.mkdir(dir_name)
history = []
user_command = None
while True:
    user_command = input()
    if user_command == 'back':
        if len(history) >= 2:
            history.pop()
            print(history.pop())
        continue
    if user_command == 'exit':
        break
    if check_url(user_command):
        status, page_content, url_p = page_load(user_command)
        if status:
            print(parse_page(page_content))
            name_page_history = url_p[8:].replace('.', '')
            name_file = os.path.join(dir_name, name_page_history)
            save_file(name_file, parse_page(page_content))
            history.append(parse_page(page_content))
            continue
        else:
            print('Error: Incorrect URL')
    else:
        path_to_file = os.path.join(dir_name, user_command)
        if os.path.exists(path_to_file):
            with open(path_to_file, 'r', encoding='utf-8') as f:
                print(parse_page(f.read()))
        else:
            print('Error: Incorrect URL')
