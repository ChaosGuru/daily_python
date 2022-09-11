import sys


def print_fizzbuzz(num: int) -> None:
    for n in range(1, num+1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)



if __name__=='__main__':
    print_fizzbuzz(int(sys.argv[1]))
