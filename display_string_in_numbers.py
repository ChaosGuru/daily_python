import optparse
import sys


def str_to_num(str_: str, bin_: bool = False) -> None:
    func = bin if bin_ else str
    return ' '.join(map(lambda x: func(ord(x)), str_))


if __name__=='__main__':
    p = optparse.OptionParser()
    p.add_option('-s', action='append', type='string')
    p.add_option('-b', action='store_true', default=False)

    options, args = p.parse_args()
    print(options.b)

    for s in options.s:
        print(s)
        print(str_to_num(str_=s, bin_=options.b))