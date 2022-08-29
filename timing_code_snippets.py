import timeit


def addition(a: float, b: float) -> float:
    return a + b


def subtraction(a: float, b: float) -> float:
    return a - b


if __name__=='__main__':
    print('1000000 times')
    print('addition: ', timeit.timeit('addition(99, 77)', globals=globals(), number=1000000))
    print('subtraction: ', timeit.timeit('subtraction(99, 77)', globals=globals(), number=1000000))