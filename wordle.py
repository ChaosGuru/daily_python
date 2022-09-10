import os
import random


def create_five_word_dict(path_to_dict, path_to_file):
    if os.path.exists(path_to_file):
        return

    # len 6 to take newline character into account
    with open(path_to_dict, 'r', encoding='utf-8') as f:
        text = ''.join(filter(lambda x: len(x)==6, f.readlines()))

    with open(path_to_file, 'w', encoding='utf-8') as f:
        f.write(text)


def choose_random_word_from_dict(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        dict_ = list(map(lambda x: x[:-1], f.readlines()))
        word = random.choice(dict_)

    return word, dict_


def start_a_game(word, dict_):
    print('***WORDLE***')

    tries = 0

    while True:

        if tries == 6:
            print(f'You did not guess word in {tries} tries. The word is {word}.')
            return

        user_word = input(f'TRY {tries+1} > ')

        if user_word == word:
            print('***CONGRATULATIONS***')
            return

        if len(user_word) != 5:
            print('Your word should have 5 letters')
            continue

        if user_word not in dict_:
            print('You word should be in dict')
            continue

        answer = ''
        for i in range(5):
            if user_word[i] == word[i]:
                answer += '='
            elif user_word[i] in word:
                answer += '+'
            else:
                answer += '-'

        print(answer)
        tries += 1


def main():
    create_five_word_dict('english_dictionary.txt', 'english_five_letter_words.txt')

    word, dict_ = choose_random_word_from_dict('english_five_letter_words.txt')
    start_a_game(word, dict_)


if __name__=='__main__':
    main()