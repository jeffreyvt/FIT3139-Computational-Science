"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""

import numpy as np


# import matplotlib.pyplot as plt

def function1(x):
    return np.power(x, 3) - 2 * x - 5


def function2(x):
    return np.exp(-x) - x


def function3(x):
    return x * np.sin(x) - 1


def function4(x):
    return np.power(x, 3) - 3 * np.power(x, 2) + 3 * x - 1


def intervalBisection(fun):
    f0 = fun(0)
    if f0 == 0:
        return 0
    i = 1
    while True:
        f1 = fun(i)
        f2 = fun(-i)
        if f1 == 0:
            return i
        elif f2 == 0:
            return -i
        elif np.sign(f0) != np.sign(f1):
            L = 0
            U = i
            fL = f0
            fU = f1
            break
        elif np.sign(f0) != np.sign(f2):
            L = -i
            U = 0
            fL = f2
            fU = f0
            break
        else:
            i += 1
    # the root is [L, U]
    # print(L, U, fL, fU)
    error = np.abs(fL - fU)
    while error > 0.00001:
        mid = (U - L) / 2 + L
        fmid = fun(mid)
        if np.sign(fmid) != np.sign(fL):
            U = mid
            fU = fmid
        else:
            L = mid
            fL = fmid
        error = np.abs(fL - fU)
        # print(mid, error)
        # print(L, U, fL, fU)
        # input()
    return mid


if __name__ == "__main__":
    print(intervalBisection(function1))
    print(intervalBisection(function2))
    print(intervalBisection(function3))
    print(intervalBisection(function4))