import numpy as np


def eps():
    eps = 1
    while 1 + eps > 1:
        eps /= 2
    print(eps * 2)


if __name__ == "__main__":
    eps()
