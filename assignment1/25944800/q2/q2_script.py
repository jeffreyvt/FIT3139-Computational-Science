"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""
import numpy as np
# used to export text file
import pandas as pd


def parse_coordinates(file_name):
    """
    search the file for CA terms and return their coordinates
    :param file_name: name of the file which contains the data
    :return: coord: coordinate array
    """
    file = open(file_name).readlines()
    coord = []
    for item in file:
        if item[13:15] == "CA":
            coord.append([float(item[31:39]), float(item[39:47]), float(item[47:55])])
    return coord

# parse the coordinates
A = np.array(parse_coordinates("A.pdb"))
B = np.array(parse_coordinates("B.pdb"))


def RMSD(U, V):
    """
    Computes RMSD using the efficient algorithm
    :param U: set of coordinates
    :param V: set of coordinates
    :return: the rmsd value between U and V
    """
    U_centoid = np.sum(U, axis=0) / len(U)
    V_centoid = np.sum(V, axis=0) / len(V)
    U_prime = U - U_centoid
    V_prime = V - V_centoid
    minus = V_prime - U_prime
    plus = V_prime + U_prime
    xm = minus[:, [0]]
    ym = minus[:, [1]]
    zm = minus[:, [2]]
    xp = plus[:, [0]]
    yp = plus[:, [1]]
    zp = plus[:, [2]]
    I = np.zeros((4, 4))

    I[0, 0] = np.sum(xm * xm + ym * ym + zm * zm)
    I[1, 1] = np.sum(xm * xm + yp * yp + zp * zp)
    I[2, 2] = np.sum(xp * xp + ym * ym + zp * zp)
    I[3, 3] = np.sum(xp * xp + yp * yp + zm * zm)

    I[0, 1] = I[1, 0] = np.sum(yp * zm - ym * zp)
    I[0, 2] = I[2, 0] = np.sum(xm * zp - xp * zm)
    I[0, 3] = I[3, 0] = np.sum(xp * ym - xm * yp)
    I[1, 2] = I[2, 1] = np.sum(xm * ym - xp * yp)
    I[1, 3] = I[3, 1] = np.sum(xm * zm - xp * zp)
    I[2, 3] = I[3, 2] = np.sum(ym * zm - yp * zp)
    w, _ = np.linalg.eig(I)
    return np.sqrt(np.min(w) / len(U))


def find_well_superposable(A, B, k=9):
    """
    Computes well superposable with size 9
    :param A: set of coordinates
    :param B: set of coordinates
    :param k: Size of the continuous interval
    :return: count: total count of superposable set of coordinates of size k
             return_array: contain the position of the pair and the RMSD of the pairs.
    """
    count = 0
    return_array = []
    for i in range(len(A) - k + 1):
        for j in range(len(B) - k + 1):
            val = RMSD(A[i: i+k], B[j:j+k])
            if val < 1.5:
                count += 1
                return_array.append([i+1, j+1, val])
    return count, return_array

count, pairs = find_well_superposable(A, B)
print("the total number of well superposable pairs is:", count)

df = pd.DataFrame(pairs)
# Add the total number of pairs to the start of the file

with open("output.txt", "w") as f:
    f.write(str(count)+"\n")

# Write the data frame to an output file
df.to_csv("output.txt", index=None, sep=' ', float_format='%.3f', mode="a", header=False)