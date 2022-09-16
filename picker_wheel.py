import random
import sys
import time


def main(items):
    chosen_item = random.choice(items)
    delay = 0.01
    final_delay = 0.5

    while True:
        print(' '.join(items), end='\r')

        if items[0] == chosen_item and delay >= final_delay:
            break

        items = items[1:] + items[:1]
        time.sleep(delay)
        delay += 0.01

    print(f'\n*** {chosen_item} ***')


if __name__=='__main__':
    main(list(map(str.upper, sys.argv[1:])))