import random


class NegativeError(Exception):
    def __str__(self):
        return "The number can't be negative!"


class DelimiterError(Exception):
    def __str__(self):
        return "Invalid input! The number can't be bigger than 1000000."


class Robogotchi:

    def __init__(self):
        self.user_won = 0
        self.robot_won = 0
        self.draws = 0

    def game_numbers(self):
        while True:
            chosen_number = random.randint(0, 10 ** 6)
            robot_number = random.randint(0, 10 ** 6)
            user_input = input("What is your number?\n")
            if user_input == 'exit game':
                self.end_game()
                break
            try:
                user_number = int(user_input)
                if user_number < 0:
                    raise NegativeError
                if user_number > 10 ** 6:
                    raise DelimiterError
            except ValueError:
                print('A string is not a valid input!')
            except NegativeError as e:
                print(e)
            except DelimiterError as e:
                print(e)
            else:
                dist_user = abs(chosen_number - user_number)
                dist_robot = abs(robot_number - user_number)
                if dist_user == dist_robot:
                    self.draws += 1
                    turn_result = 'It\'s a draw!'
                elif dist_robot > dist_user:
                    self.user_won += 1
                    turn_result = 'You won!'
                elif dist_robot < dist_user:
                    self.robot_won += 1
                    turn_result = 'The robot won!'
                print(f"The robot entered the number {robot_number}.")
                print(f"The goal number is {chosen_number}.")
                print(turn_result)

    def end_game(self):
        print(f"You won: {self.user_won},")
        print(f"The robot won: {self.robot_won},")
        print(f"Draws: {self.draws}.")


robot = Robogotchi()
robot.game_numbers()
