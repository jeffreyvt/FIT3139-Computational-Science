import numpy as np

x = 100.0
multiplier = 2.0
while True:
    x_previous = x
    x = np.multiply(x, multiplier)
    if x == np.inf:
        x = x_previous
        multiplier = (multiplier - 1.0) / 10.0 + 1.0
    if multiplier < 1.00000001:
        break
print(x)
