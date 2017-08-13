"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""

import numpy as np
import matplotlib.pyplot as plt

S = [0, 1]
for i in range(2, 101):
    S.append(S[i - 2] + 0.5 * S[i - 1])
plt.plot(S)
plt.show()



"""
Solving the recurrence relation using eigenvalue decomposition, we get

Sk+1 = ((2^(-3 - 2 n) (1 - Sqrt[17])^(1 + n) (1 + Sqrt[17]))/Sqrt[17] + (
    2^(-3 - 2 n) (-1 + Sqrt[17]) (1 + Sqrt[17])^(1 + n))/Sqrt[
    17]) s0 + (-((2^(-1 - 2 n) (1 - Sqrt[17])^(1 + n))/Sqrt[17]) + (
    2^(-1 - 2 n) (1 + Sqrt[17])^(1 + n))/Sqrt[17]) s1


The system is growing exponentially
"""