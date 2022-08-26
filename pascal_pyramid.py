def print_pascal_pyramid(num: int, width: int) -> None:
    row = [1]

    for n in range(num, 0, -1):
        print(' ' * n*int(width/2) + ' '.join([str(i).center(width) for i in row]))

        row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]


if __name__=='__main__':
    print_pascal_pyramid(5, 4)