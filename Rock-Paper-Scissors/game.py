import random

# beats = {"scissors": "rock", "paper": "scissors", "rock": "paper"}
# state = [i for i in beats.keys()]
name = input('Enter your name:')
print(f'Hello, {name}')
holder = open('rating.txt', 'r')
score = 0
for line in holder:
    name_f, score_f = line.split()
    if name == name_f:
        score = int(score_f)
holder.close()
from_user = input()
if from_user == '':
    from_user = 'scissors,rock,paper'
state = from_user.split(',')
n = len(state) - 1  # number of options
beats = {}
for i, item in enumerate(state):
    options = state[i + 1:] + state[:i]
    beats[item] = options[:n // 2]
print("Okay, let's start")
while True:
    user_choose = input()
    if user_choose == '!exit':
        break
    if user_choose == '!rating':
        print(f'Your rating: {score}')
        continue
    if user_choose not in state:
        print('Invalid input')
        continue
    comp_choose = random.choice(state)
    if user_choose == comp_choose:
        print(f'There is a draw ({user_choose})')
        score += 50
    elif comp_choose in beats[user_choose]:
        print(f'Sorry, but computer chose {comp_choose}')
    else:
        print(f'Well done. Computer chose {comp_choose} and failed')
        score += 100
print('Bye!')
