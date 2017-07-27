import numpy as np
import math

def stirling_approx(n):
    return np.sqrt(2*np.pi*n)*np.power((n/np.exp(1)),n)

if __name__ == "__main__":
    for n in range(15):
        real_val = math.factorial(n)
        approx_val = stirling_approx(n)
        abs_error = abs(real_val - approx_val)
        print("n: ", n, "Absolute error: ", abs_error, "relative error: ", abs_error/real_val*100,"%")