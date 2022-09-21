import sys


def fahrenheit_to_celsius(t: float) -> float:
    """
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(70)
    21.1
    """
    return round((t - 32) * 5 / 9, 1)


def celsius_to_fahrenheit(t: float) -> float:
    """
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(21.1)
    70.0
    """
    return round((t * 9 / 5) + 32, 1)


if __name__=='__main__':
    if sys.argv[1] == 'F':
        print(fahrenheit_to_celsius(float(sys.argv[2])), 'C')
    elif sys.argv[1] == 'C':
        print(celsius_to_fahrenheit(float(sys.argv[2])), 'F')
    else:
        print('Command should be in format: $ python temperature.py <C|F> <99.9>')