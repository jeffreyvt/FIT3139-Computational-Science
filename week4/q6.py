"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""

import numpy as np


def function(x):
    return x ** 2 - 1


def function_d(x):
    return 2 * x

def function2(x):
    return (x-1)**4

def function2_d(x):
    return 4*(x-1)**3



def newton(fun, fun_d, true_val, i=0):
    error_list = []
    x_current = i
    while True:
        x_next = x_current - fun(x_current) / fun_d(x_current)
        error_list.append(abs(true_val - x_next))
        error = np.abs(x_next - x_current)
        if error < 0.000000001:
            return x_next, error_list
        else:
            x_current = x_next


solution, errors = newton(function, function_d, 1, i=1000000)
print(solution)
for i in range(len(errors)-1):
    errors[i] = errors[i+1]/errors[i]
errors.pop()
print(errors)

solution, errors = newton(function2, function2_d, 1, i=10)
print(solution)
for i in range(len(errors)-1):
    errors[i] = errors[i+1]/errors[i]
errors.pop()
print(errors)