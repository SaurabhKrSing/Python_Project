import random

again = True

while again:
    number = random.randint(1, 6)
    print('Roll the Dice (y/n): ')
    if again == 'y' or again == 'Y' or again == 'Yes':
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

    # x = input("Press 'Y' to roll again and 'N' to exit:")
    # print("\n")

    # if x == 'N':
    #     break
