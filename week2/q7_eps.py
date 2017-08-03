import numpy as np


def eps():
    eps = 1
    while 1 + eps > 1:
        eps /= 2

    # prints out the double of before it was registered by the condition.
    print(eps * 2)


if __name__ == "__main__":
    print("The machine eps is: ")
    eps()
