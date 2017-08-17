"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""

import numpy as np


def function1(x):
    return np.power(x, 3) - 2 * x - 5


def function1_d(x):
    return 3 * np.power(x, 2) - 2


def function2(x):
    return np.exp(-x) - x


def function2_d(x):
    return -np.exp(-x) - 1


def function3(x):
    return x * np.sin(x) - 1


def function3_d(x):
    return x * np.cos(x) + np.sin(x)


def function4(x):
    return np.power(x, 3) - 3 * np.power(x, 2) + 3 * x - 1


def function4_d(x):
    return 3 * np.power(x, 2) - 6 * x + 3


def newton(fun, fun_d, i=0):
    x_current = i
    while True:
        x_next = x_current - fun(x_current)/fun_d(x_current)
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



if __name__ == "__main__":
    print("Newton's Method: ")
    print("The root for function 1 is: ", newton(function1, function1_d))
    print("The root for function 2 is: ", newton(function2, function2_d))
    # This gives divide by zero error unless the starting position is initialized correctly
    print("The root for function 3 is: ", newton(function3, function3_d, 0.5))
    print("The root for function 4 is: ", newton(function4, function4_d))

    print("Secant Method: ")
    print("The root for function 1 is: ", secant(function1))
    print("The root for function 2 is: ", secant(function2))
    # This gives divide by zero error unless the starting position is initialized correctly
    print("The root for function 3 is: ", secant(function3))
    print("The root for function 4 is: ", secant(function4))