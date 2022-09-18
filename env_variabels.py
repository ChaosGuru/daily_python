import os
import sys

if __name__=='__main__':
    arg = sys.argv[1]

    print(f'getenv: {os.getenv} {type(os.getenv)}')
    print(f'environ: {os.environ} {type(os.environ)}')

    # Returns None is there no vaiable
    print(f'Getting environment variable {arg}')
    print(os.getenv(arg))
    print(os.environ.get(arg))