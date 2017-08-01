import numpy as np
import math

def taylor_expo(x):
    ans_list = [1]
    ans = 1
    print("iteration 1, value = 1")
    i = 1
    while True:
        previous_ans = ans
        ans += np.power(x, i)/math.factorial(i)
        ans_list.append(ans)
        error = (ans-previous_ans)/(ans)*100
        print("iteration ", i+1, ", value = ", ans, ", error = ", error)
        if error < 0.00001:
            break
        i += 1
    print(ans)



if __name__ == "__main__":
    taylor_expo(7)