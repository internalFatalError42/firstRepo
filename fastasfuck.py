from functools import cache, lru_cache
import numpy as np
import time


#@lru_cache(maxsize=5)
@cache
def fib(n):
    if n <= 1:
        return n
    #return fib(np.subtract(n, 1)) + fib(np.subtract(n, 2))
    return fib(n - 1) + fib(n - 2)


def loop():
    for i in range(4000):
        print(f"{i} {fib(i)}")
    print("done")


def main():
    """
    for i in range(400):
        print(i, fib(i))
    print("done")
"""
    print(time.time())
    timeBegin = time.time()
    loop()
    timeEnd = time.time()
    print("Dauer Programmausführung:", )
    print(timeBegin - timeEnd)


if __name__ == '__main__':
    main()
