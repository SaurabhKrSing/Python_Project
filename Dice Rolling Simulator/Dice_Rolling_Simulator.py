import random


while True:
    print('Roll the Dice (y/n): ')
    user = input()
    if user == 'y' or user == 'Y' or user == 'Yes' or user == 'yes':
        number = random.randint(1, 6)
        if number == 1:
            print('''
            ┌─────────┐
            │         │
            │    ●    │
            │         │
            └─────────┘
            ''')

        if number == 2:

            print('''
            ┌─────────┐
            │    ●    │
            │         │
            │    ●    │
            └─────────┘
            ''')

        if number == 3:

            print('''
            ┌─────────┐  
            │ ●       │  
            │    ●    │  
            │       ● │  
            └─────────┘  
            ''')

        if number == 4:

            print('''
            ┌─────────┐  
            │ ●     ● │  
            │         │  
            │ ●     ● │  
            └─────────┘
            ''')

        if number == 5:

            print('''
            ┌─────────┐  
            │ ●     ● │  
            │    ●    │  
            │ ●     ● │  
            └─────────┘
            ''')

        if number == 6:

            print('''
            ┌─────────┐  
            │ ●     ● │  
            │ ●     ● │  
            │ ●     ● │  
            └─────────┘
            ''')
    else:
        break
