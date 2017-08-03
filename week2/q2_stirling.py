"""
Student ID: 2594 4800
Name: JiaHui (Jeffrey) Lu
Aug-2017
"""

import numpy as np
import math

def stirling_approx(n):
    """
    Implements the Stirling's approximation
    :param n: value for n!
    :return: approximated value for n! using stirling's approximation.
    """
    return np.sqrt(2*np.pi*n)*np.power((n/np.exp(1)),n)

if __name__ == "__main__":
    for n in range(1,16):
        real_val = math.factorial(n)
        approx_val = stirling_approx(n)
        abs_error = abs(real_val - approx_val)
        print("n: ", n, "Absolute error: ", abs_error, "relative error: ", abs_error/real_val*100,"%")