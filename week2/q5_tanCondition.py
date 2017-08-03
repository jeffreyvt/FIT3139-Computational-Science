import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = x * (1 + np.power(np.tan(x), 2)) / np.tan(x)
y1 = np.tan(x)

plt.subplot(1, 2, 1)
plot1, = plt.plot(x, y, label="condition")
plot2, = plt.plot(x, y1, "g", label="function")
plt.title("f(x) = tan(x)")
plt.legend(handles=[plot1, plot2], loc=1)
plt.ylim((-100, 100))

plt.subplot(1, 2, 2)
z = x / ((1 + np.power(x, 2)) * np.arctan(x))
z1 = np.arctan(x)
plot3, = plt.plot(x, z, label="condition")
plot4, = plt.plot(x, z1, "g", label="function")
plt.legend(handles=[plot3, plot4], loc=1)
plt.title("f(x) = arctan(x)")
plt.show()

"""
The green plot shows the function value and the blue plot shows the condition number.
As you can see, the condition number for arctan(x) behaves much nicer (much better conditioned) than tan(x)
"""