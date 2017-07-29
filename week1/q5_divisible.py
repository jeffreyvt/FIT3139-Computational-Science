import numpy as np


def divisible(num):
    if num % 2 == 0:
        if num % 5 == 0:
            if num % 7 == 0:
                return True
    return False


if __name__ == "__main__":
    for i in range(1, 100):
        print(i, divisible(i))
