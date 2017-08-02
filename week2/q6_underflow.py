import numpy as np

x = -100.0
while x != -np.inf:
    x_previous = x
    x = np.multiply(x, 2.0)
x = x_previous
while x != -np.inf:
    x_previous = x
    x = np.multiply(x, 1.1)

x = x_previous
while x != -np.inf:
    x_previous = x
    x = np.multiply(x, 1.01)

x = x_previous
while x != -np.inf:
    x_previous = x
    x = np.multiply(x, 1.001)
print(x_previous)