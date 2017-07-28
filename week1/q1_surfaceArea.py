import numpy as np

def dA_exact(r, delta):
    return 4*np.pi*(2*r*1000+delta/1000)*delta/1000


def dA_approx(r, delta):
    return 8*np.pi*r*delta


if __name__ == "__main__":
    for i in range(10):
        print("exact dA = ", dA_exact(6367, i), "approx. dA = ", dA_approx(6367, i))