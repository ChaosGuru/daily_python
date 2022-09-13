import sys
import time


def main(seconds: int) -> None:
    first_time = time.perf_counter()

    while True:
        remaining_time = int(seconds - (time.perf_counter() - first_time))
        
        if remaining_time < 0:
            break

        m, s = remaining_time // 60, remaining_time % 60
        print(f'{m}m {s}s', end='\r')

        time.sleep(1)

    print('***BOOM***')


if __name__=='__main__':
    main(int(sys.argv[1]))