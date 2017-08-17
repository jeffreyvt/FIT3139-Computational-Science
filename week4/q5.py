"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""

import numpy as np

def function(x):
    return (x**2-1)/(2*x)-1/np.tan(x)


def function_d(x):
    return -1+(x**2-1)/(2*x*x) - 1/(np.sin(x)**2)

def newton(fun, fun_d, i=0):
    x_current = i
    while True:
        x_next = x_current - fun(x_current)/fun_d(x_current)
        # print(x_next)
        error = np.abs(x_next - x_current)
        if error < 0.000000001:
            return x_next
        else:
            x_current = x_next

def secant(fun, i1=0, i2=0.01):
    x_current = i1
    x_previous = i2
    while True:
        x_next = x_current - (fun(x_current)*(x_current-x_previous))/(fun(x_current)-fun(x_previous))
        error = np.abs(x_next - x_current)
        if error < 0.000000001:
            return x_next
        else:
            x_previous = x_current
            x_current = x_next


def intervalBisection(fun, U, L):
    error = np.abs(U - L)
    fL = fun(L)
    while error > 0.00001:
        mid = (U - L) / 2 + L
        fmid = fun(mid)
        if np.sign(fmid) != np.sign(fL):
            U = mid
        else:
            L = mid
            fL = fmid
        error = np.abs(U - L)
    return mid

if __name__ == "__main__":
    print(secant(function, 0.1, 0.01))
    print(intervalBisection(function, 2, 1))
    # Cant seem to get the newton to converge
    print(newton(function,function_d, 1.33))