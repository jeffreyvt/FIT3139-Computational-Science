import numpy as np
import matplotlib.pyplot as plt

def taylor_sine(x, d):
    ans = x
    factorial = 1
    for i in range(1, d):
        factorial *= 2*i*(2*i+1)
        ans += np.power(-1, 2*i+1 )*np.power(x, 2*i+1)/factorial
    return ans

if __name__ == "__main__":
    x = np.arange(0, np.pi, 0.015)
    y_real = x-1-0.5*np.sin(x)
    plt.plot(x,y_real)
    y_est = x - 1 - 0.5 * taylor_sine(x, 10)
    plt.plot(x, y_est, "g")
    plt.show()
    input()



    i = 1
    while True:
        y_est = x-1-0.5*taylor_sine(x, i)
        print(y_est)
        error = np.max(np.abs(y_est - y_real))
        print(error)
        i += 1
        if i == 10:
            break