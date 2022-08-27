import operator


def bubble_sort(list_: list, reverse: bool = False) -> list:
    compare = operator.lt if reverse else operator.gt

    for i in range(len(list_)):
        for j in range(len(list_)-1-i):
            if compare(list_[j], list_[j+1]):
                list_[j+1], list_[j] = list_[j], list_[j+1]
                print(list_)


if __name__=='__main__':
    lists = [
        [],
        [1],
        [2, 1],
        [1, 9, 8, 7, 6, 5, 1, 4, 3],
        [1, 2, 3, 4, 5, 6, 7, 8],
    ]

    for l in lists:
        bubble_sort(l)
        print(l)