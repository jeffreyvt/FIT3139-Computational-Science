import numpy as np
import matplotlib.pyplot as plt


def taylor_sine(x, d):
    """
    Element-wise function for sine.
    :param x: sine argument
    :param d: specifies when to stop the taylor series expansion
    :return: the taylor expansion of x to d-th term
    """
    ans = x
    factorial = 1
    for i in range(1, d):
        factorial *= 2 * i * (2 * i + 1)
        ans += np.power(-1, i) * np.power(x, 2 * i + 1) / factorial
    return ans


if __name__ == "__main__":
    x = np.arange(0, np.pi, 0.015)
    y_real = x - 1 - 0.5 * np.sin(x)
    y_est = np.zeros(x.size)

    plt.plot(x, y_est, "g*")

    d = 1
    while True:
        for i in range(x.size):
            y_est[i] = x[i] - 1 - 0.5 * taylor_sine(x[i], d)
        error = np.max(np.abs(y_est - y_real))
        print("Taylor series expansion order: ", d, "max error: ", error)
        d += 1
        if d > 12 or error < 0.015:
            break
    