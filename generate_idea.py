import json
import random
import sys

FILE_WITH_IDEAS = 'ideas.json'


def print_random_ideas():
    with open(FILE_WITH_IDEAS, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, item in data.items():
        if type(item) == list:
            print(f'{key}: {random.choice(item)}; ', end='')
        elif type(item) == dict:
            sub_key = random.choice(list(item.keys()))
            print(f'{key}: {random.choice(item[sub_key])}; ', end='')

    print('')


if __name__=='__main__':
    try:
        times = int(sys.argv[1])
    except IndexError:
        times = 1
        
    for _ in range(times):
        print_random_ideas()