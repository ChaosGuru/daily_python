def fib_first_nums(num: int) -> list:
    f1, f2 = 0, 1
    list_ = []

    for _ in range(num):
        list_.append(f1)
        f1, f2 = f2, f1 + f2

    return list_

def fib_num(num: int) -> int:
    f1, f2 = 0, 1

    for _ in range(num-1):
        f1, f2 = f2, f1 + f2

    return f1

if __name__=='__main__':
    for i in [0, 1, 2, 5, 10, 20]:
        print(f'Fib {i}: {fib_first_nums(i)}')
        print(f'Fib num {i}: {fib_num(i)}')