import json
from requests import get
import sys

BASE_URL = 'http://api.datamuse.com/words'
RHYME_ENDPOINT = f'{BASE_URL}?rel_rhy='


def find_rhyme_with(word: str) -> list:
    
    try:
        response = get(f'{RHYME_ENDPOINT}{word}')
    except Exception as error:
        return errors

    if not response.ok:
        return response.status_code

    data = json.loads(response.text)

    return ', '.join([d['word'] for d in data])

if __name__=='__main__':
    for word in sys.argv[1:]:
        if word.isalpha():
            print(f'{word}: {find_rhyme_with(word)}')
        else:
            print(f'{word} is not a string')