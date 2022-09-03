import time
from threading import Thread


def print_by_letter(str_: str) -> None:
    for s in str_:
        print(s)
        time.sleep(1)


if __name__=='__main__':
    strings = ['Hello', 'World', '!', '123456789']

    threads = [Thread(target=print_by_letter, args=(s,)) for s in strings]

    for t in threads:
        t.start()