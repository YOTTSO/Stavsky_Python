import os
import time

while True:
    print('Type \'exit\' to quit')
    user_input = input('Enter 7, John or numeric array')
    if user_input == 'exit':
        exit()
    try:
        if int(user_input) > 7:
            print('Hello')
    except ValueError:
        try:
            if user_input == 'John':
                print('Hello, John')
        except ValueError:
            print('There is no such name')
        try:
            numbers = list(map(int, user_input.split(",")))
            specific_list = [x for x in numbers if x % 3 == 0]
            print(f'{specific_list}')
        except ValueError:
            pass
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
