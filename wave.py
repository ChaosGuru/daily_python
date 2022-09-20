import sys


def wave(str_: str) -> list:
    """
    Returns a wave of string
    
    >>> wave('cat')
    ['Cat', 'cAt', 'caT']
    >>> wave('wow')
    ['Wow', 'wOw', 'woW']
    """
    str_ = str_.lower()

    return [
        str_[:i] + str_[i].upper() + str_[i+1:] 
        for i in range(len(str_)) 
        if str_[i].isalpha()
    ]


if __name__=='__main__':
    print(wave(sys.argv[1]))