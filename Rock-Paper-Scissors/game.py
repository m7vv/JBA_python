import random
beats = {"scissors": "rock", "paper": "scissors", "rock": "paper"}
state = [i for i in beats.keys()]
user_choose = input()
comp_choose = random.choice(state)
if user_choose == comp_choose:
    print(f'There is a draw ({user_choose})')
elif comp_choose == beats[user_choose]:
    print(f'Sorry, but computer chose {comp_choose}')
else:
    print(f'Well done. Computer chose {comp_choose} and failed')
