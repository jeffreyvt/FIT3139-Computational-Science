import numpy as np


def pi(M):
    p = 22
    best_p = 22
    q = 7
    best_q = 7
    current_error = abs(np.pi - p / q)
    for i in range(7, M+1):
        p = best_p
        batch_error_previous = 100
        while True:
            p += 1
            batch_error = abs(np.pi - p / i)
            if batch_error < current_error:
                best_p = p
                best_q = i
            if batch_error > batch_error_previous:
                break
            batch_error_previous = batch_error
    print(best_p, best_q, best_p/best_q)


if __name__ == "__main__":
    pi(1000000)