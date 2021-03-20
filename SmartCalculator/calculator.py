while True:
    user_input = input().split()
    if len(user_input) >= 2:
        print(sum((int(number) for number in user_input)))
    if len(user_input) == 1:
        if user_input[0] == r'/exit':
            print('Bye!')
            break
        if user_input[0] == r'/help':
            print('The program calculates the sum of numbers')
        print(user_input[0])
