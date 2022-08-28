import sys


def main():
    try:
        nums = list(map(float, sys.argv[1:]))
    except ValueError:
        print('Some or all arguments are not numbers!')
    else:
        print(f'Sum is {sum(nums)}')


if __name__=='__main__':
    main()