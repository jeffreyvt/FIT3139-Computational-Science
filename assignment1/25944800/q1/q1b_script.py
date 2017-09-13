"""
Author: JiaHui (Jeffrey) Lu
ID: 25944800
"""
import numpy as np
import matplotlib.pyplot as plt
import time


def my_log1p(x):
    """
    The function takes in x value then uses taylor expansion formula to generate the value for log1p
    :param x: the input to the function log(1+x)
    :return: ans: the result of log1p with input x.
             n: the number of iteration used to obtain a convergent result
             error: the error of my_log1p compare to inbuilt np.log1p
             inbuilt_error: error of np.log compare to np.log1p
             my_runtime: runtime of my_log1p
             inbuilt_runtime: runtime of inbuilt log
             actual_runtime: runtime of np.log1p
    """
    n = 2
    ans = x
    start = time.time()
    while True:
        delta = (((-1) ** (n + 1)) * (x ** n)) / n
        ans += delta
        if n >= 1000000 or abs(delta) < 0.000001:
            break
        n += 1
    end = time.time()
    my_runtime = end - start

    # compute the error and run time.
    start = time.time()
    inbuilt = np.log(1 + x)
    end = time.time()
    inbuilt_runtime = end - start

    start = time.time()
    actual = np.log1p(x)
    end = time.time()
    actual_runtime = end - start
    error = abs((ans - actual) / actual)
    inbuilt_error = abs((inbuilt - actual) / actual)

    # Return value as required
    return ans, n, error, inbuilt_error, my_runtime, inbuilt_runtime, actual_runtime


def my_another_log1p(x):
    """
    This function computes the log1p via a more direct method compare to previous alternating convergent formula
    :param x: input to the log(1+x)
    :return: ans: the return value to log(1+x)
             n: the number of iteration until convergence
             error: the relative error compare to the np.log1p method
    """
    y = 1 - 2 / (2 + x)
    n = 2
    ans = 2 * y
    while True:
        delta = 2 * (y ** (2 * n - 1)) / (2 * n - 1)
        ans += delta
        if n >= 1000000 or abs(delta) < 0.000001:
            break
        n += 1
        # print(delta)
    actual = np.log1p(x)
    error = abs((ans - actual) / actual)
    return ans, n, error


# Generate test values
small_vals = np.array([2.220446049250313e-50, 2.220446049250313e-16])
tmp = np.linspace(0, 2, 10000)
test_val = np.concatenate([small_vals, tmp[1:]])
# Generate test values
# Using values that were significantly smaller than machine eps.
small_vals = np.array([2.220446049250313e-50, 2.220446049250313e-20, 2.220446049250313e-16])
# add in values from 0 to 1
tmp = np.linspace(0, 1, 10000)
test_val = np.concatenate([small_vals, tmp[1:]])

my_errors = []
other_errors = []
my_ns, other_ns = [], []
for test_item in test_val:
    _, my_n, my_error, inbuilt_error, mine, inbuilt, actual = my_log1p(test_item)
    ___, other_n, other_error = my_another_log1p(test_item)
    my_errors.append(my_error)
    other_errors.append(other_error)
    my_ns.append(my_n)
    other_ns.append(other_n)

fig = plt.figure(figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')

# plot errors of the two function on the same plot
plt.subplot(3, 1, 1)
plt.ylim((0, 0.000001))
plt.xlim((-0.01, 1.01))
plt.plot(test_val, my_errors, label="my_log1p errors")
plt.plot(test_val, other_errors, label="my_another_log1p errors")
plt.legend(loc=1)
plt.title("Relative Errors")

# plot the number of iteration it took to converge
plt.subplot(3, 1, 3)
plt.ylim((0, 50))
plt.plot(test_val, my_ns, label="my_log1p iterations")
plt.plot(test_val, other_ns, label="my_another_log1p iterations")
plt.legend(loc=2)
plt.title("iterations")

# plot the errors of the second method when x is ranging from 0 to 10
plt.subplot(3, 1, 2)
small_vals = np.array([2.220446049250313e-50, 2.220446049250313e-20, 2.220446049250313e-16])
tmp = np.linspace(0, 10, 10000)
test_val = np.concatenate([small_vals, tmp[1:]])
other_errors = []
for test_item in test_val:
    _, __, other_error = my_another_log1p(test_item)
    other_errors.append(other_error)
plt.ylim((0, 0.000001))
plt.xlim((-0.01, 10.01))
plt.plot(test_val, other_errors, label="my_another_log1p errors")
plt.legend(loc=1)
plt.title("Relative Errors")
plt.show()
