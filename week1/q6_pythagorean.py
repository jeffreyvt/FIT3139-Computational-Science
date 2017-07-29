import numpy as np


def triangle(a,b,c):
    L = [a,b,c]
    L.sort()
    if L[2]*L[2] == L[1]*L[1] + L[0]*L[0]:
        return True
    return False


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                print(i, j, k, triangle(i, j, k))