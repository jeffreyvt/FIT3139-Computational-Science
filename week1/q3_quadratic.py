import numpy as np
import matplotlib.pyplot as plt


def find_min(L, R, b, c):
    xc = -b / 2
    if L <= xc <= R:
        return xc
    else:
        left = L * L + b * L + c
        right = R * R + b * R + c
        if left > right:
            return R
        else:
            return L


if __name__ == "__main__":
    L = -20
    R = 20
    b = 20
    c = 10
    minimum = find_min(L, R, b, c)
    x = np.arange(L - 10, R + 10, 0.1)
    x1 = np.arange(L, R, 0.1)
    y1 = np.add(np.add(np.multiply(x1, x1), np.multiply(b, x1)), c)
    y = np.add(np.add(np.multiply(x, x), np.multiply(b, x)), c)
    plt.plot(x, y)
    plt.plot(minimum, minimum * minimum + b * minimum + c, "ro")
    plt.plot(x1, y1, "r")
    plt.show()
