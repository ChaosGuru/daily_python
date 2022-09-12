import sys
import random


def main():

    choices = ('paper', 'rock', 'scissors')

    combinations = {
        ('paper', 'paper'): 'DRAW',
        ('paper', 'rock'): 'WIN',
        ('paper', 'scissors'): 'LOSS',
        ('rock', 'paper'): 'LOSS',
        ('rock', 'rock'): 'DRAW',
        ('rock', 'scissors'): 'WIN',
        ('scissors', 'paper'): 'WIN',
        ('scissors', 'rock'): 'LOSS',
        ('scissors', 'scissors'): 'DRAW',
    }

    while True:
        user_ipnut = input('> ')

        if user_ipnut == 'q':
            break
        
        if user_ipnut not in choices:
            print('Bad input')
            continue

        print(combinations[(user_ipnut, random.choice(choices))])


if __name__=='__main__':
    main()