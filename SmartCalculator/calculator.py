while True:
    user_input = input().split()
    if len(user_input) == 2:
        print(int(user_input[0]) + int(user_input[1]))
    if len(user_input) == 1:
        if user_input[0] == r'/exit':
            print('Bye!')
            break
        print(user_input[0])
