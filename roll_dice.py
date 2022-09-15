import sys
import random


def print_roll(dice: int) -> None:
    print(f'Dice {dice} = {random.randint(1, dice)}')


if __name__=='__main__':
    for dice in sys.argv[1:]:
        print_roll(int(dice))