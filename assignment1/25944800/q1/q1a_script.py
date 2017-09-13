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


# Generate test values
# Using values that were significantly smaller than machine eps.
small_vals = np.array([2.220446049250313e-50, 2.220446049250313e-20, 2.220446049250313e-16])
# add in values from 0 to 1
tmp = np.linspace(0, 1, 10000)
test_val = np.concatenate([small_vals, tmp[1:]])

my_runtime, inbuilt_runtime, actual_runtime = [], [], []
my_errors = []
inbuilt_errors = []
for test_item in test_val:
    _, __, my_error, inbuilt_error, mine, inbuilt, actual = my_log1p(test_item)
    my_runtime.append(mine)
    inbuilt_runtime.append(inbuilt)
    actual_runtime.append(actual)
    my_errors.append(my_error)
    inbuilt_errors.append(inbuilt_error)

fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

# plot the run time of all three methods
plt.subplot(2, 1, 1)
plt.xlim((-0.01, 1.01))
plt.ylim((0, 0.0002))
plt.plot(test_val, my_runtime, label="my_log1p runtime")
plt.plot(test_val, inbuilt_runtime, label="inbuilt log runtime")
plt.plot(test_val, actual_runtime, label="inbuilt log1p runtime")
plt.legend(loc=2)
plt.title("Computation time in seconds")

# plot the relative error
plt.subplot(2, 1, 2)
plt.ylim((0, 0.000001))
plt.xlim((-0.01, 1.01))
plt.plot(test_val, my_errors, label="my_log1p error")
plt.plot(test_val, inbuilt_errors, label="inbuilt log errors")
plt.legend(loc=1)
plt.title("Relative Errors")
plt.show()
