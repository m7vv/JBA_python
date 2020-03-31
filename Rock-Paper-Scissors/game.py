import random


class Game:
    file_name = 'rating.txt'
    default_options = 'scissors,rock,paper'

    def __init__(self):
        self.user_name = None
        self.states = None
        self.user_rating = None
        self.beats = None

    def set_user_name(self):
        self.user_name = input('Enter your name:')

    def show_greeting(self):
        print(f'Hello, {self.user_name}')

    def find_rating(self):
        with open(Game.file_name, 'r') as f:
            self.user_rating = 0
            for line in f:
                name_f, rating_f = line.split()
                if self.user_name == name_f:
                    self.user_rating = int(rating_f)
                    break

    def get_states(self):
        states_from_user = input()
        if states_from_user == '':
            states_from_user = Game.default_options
        self.states = states_from_user.split(',')

    def set_beats(self):
        n = len(self.states) - 1  # number of options without choosen
        self.beats = {}
        for i, item in enumerate(self.states):
            options = self.states[i + 1:] + self.states[:i]
            self.beats[item] = options[:n // 2]
        print("Okay, let's start")

    def play(self):
        while True:
            user_choose = input()
            if user_choose == '!exit':
                break
            if user_choose == '!rating':
                print(f'Your rating: {self.user_rating}')
                continue
            if user_choose not in self.states:
                print('Invalid input')
                continue
            comp_choose = random.choice(self.states)
            if user_choose == comp_choose:
                print(f'There is a draw ({user_choose})')
                self.user_rating += 50
            elif comp_choose in self.beats[user_choose]:
                print(f'Sorry, but computer chose {comp_choose}')
            else:
                print(f'Well done. Computer chose {comp_choose} and failed')
                self.user_rating += 100
        print('Bye!')


g = Game()
g.set_user_name()
g.show_greeting()
g.find_rating()
g.get_states()
g.set_beats()
g.play()
