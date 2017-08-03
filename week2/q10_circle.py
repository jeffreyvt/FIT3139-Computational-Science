import numpy as np


def est_area(r, dx=1.0):
    x = np.arange(0, r, dx)
    y = np.sqrt(r * r - np.power(x, 2))
    y = np.floor(y / dx) * dx
    return (np.sum(y) - y[0]) * dx * 4


if __name__ == "__main__":
    r = 10
    estimated_area = est_area(r)
    estimated_pi = estimated_area / (r * r)
    print("r =", r, "dx = 1", "estimated pi =", estimated_pi, "The absolute error is:", np.abs(np.pi - estimated_pi))

    r = 100
    dx = 0.01
    estimated_area = est_area(r, dx=dx)
    estimated_pi = estimated_area / (r * r)
    print("r =", r, "dx =", dx, "estimated pi =", estimated_pi, "The absolute error is:",
          np.abs(np.pi - estimated_pi))
