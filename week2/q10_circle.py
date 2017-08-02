import numpy as np


def est_area(r, dx=0.1):
    x = np.arange(0, r, dx)
    y = np.sqrt(r * r - np.power(x, 2))
    y = np.floor(y / dx) * dx
    return np.sum(y) * dx * 4


if __name__ == "__main__":
    r = 10
    estimated_area = est_area(r, 0.001)
    estimated_pi = estimated_area / (r * r)
    print("estimated pi is = ", estimated_pi, "The absolute error is: ", abs(np.pi - estimated_pi))
