import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def check_url(url):
    if '.' in url:
        return True
    else:
        return False


def save_file(name, page):
    with open(name, 'w') as fi:
        fi.write(page)


# Create target Directory if don't exist
dir_name = sys.argv[1] if len(sys.argv) > 1 else None
if (dir_name is not None) and (not os.path.exists(dir_name)):
    os.mkdir(dir_name)
history = []
user_command = None
while True:
    user_command = input()
    if user_command == 'back':
        if len(history)>=2:
            history.pop()
            print(history.pop())
        continue
    if user_command == 'exit':
        break
    if check_url(user_command):
        if user_command == 'bloomberg.com':
            print(bloomberg_com)
            name_file = f'{dir_name}\\bloomberg'
            save_file(name_file, bloomberg_com)
            history.append(bloomberg_com)
            continue
        elif user_command == 'nytimes.com':
            print(nytimes_com)
            name_file = f'{dir_name}\\nytimes'
            save_file(name_file, nytimes_com)
            history.append(nytimes_com)
            continue
        else:
            print('Error: Incorrect URL')
    else:
        path_to_file = f'{dir_name}\\{user_command}'
        if os.path.exists(path_to_file):
            with open(path_to_file, 'r') as f:
                print(f.read())
        else:
            print('Error: Incorrect URL')
