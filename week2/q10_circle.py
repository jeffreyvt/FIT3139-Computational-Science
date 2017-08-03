"""
Student ID: 2594 4800
Name: JiaHui (Jeffrey) Lu
Aug-2017
"""

import numpy as np


def est_area(r, dx=1.0):
    """
    estimates the area of the circle with radius r.
    taking small square of length dx
    :param r: radius of the circle
    :param dx: the unit length of the square. default = 1
    :return: the estimated area of the circle
    """
    # plots the quarter of the circle
    x = np.arange(0, r, dx)
    y = np.sqrt(r * r - np.power(x, 2))

    # only keep the squares that are inside of the circle
    y = np.floor(y / dx) * dx

    # counts the squares by summing up the values in y.
    # multiply the value by 4 as we only computed a
    # quarter of a circle
    return (np.sum(y) - y[0]) * dx * 4


if __name__ == "__main__":
    r = 420
    estimated_area = est_area(r)
    estimated_pi = estimated_area / (r * r)
    print("r =", r, "dx = 1", "estimated pi =",
          estimated_pi, "The absolute error is:",
          np.abs(np.pi - estimated_pi))

    r = 100
    dx = 0.1
    estimated_area = est_area(r, dx=dx)
    estimated_pi = estimated_area / (r * r)
    print("r =", r, "dx =", dx, "estimated pi =",
          estimated_pi, "The absolute error is:",
          np.abs(np.pi - estimated_pi))
