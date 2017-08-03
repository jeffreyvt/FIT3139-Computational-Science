import numpy as np

def taylor_expo(x):
    """
    Implements the taylor expansion of the exponential function.
    Prints out approximate relative error as the computation proceeds.
    :param x: the input value for expo(x)
    :return: the value for expo(x)
    """
    ans_list = [1]
    ans = 1
    print("iteration 1, value = 1")
    i = 1
    factorial = 1
    while True:
        # Taylor series expansion of exponential function.
        previous_ans = ans
        factorial *= i
        ans += np.power(x, i)/factorial
        ans_list.append(ans)
        error = (ans-previous_ans)/(ans)*100
        print("iteration ", i+1, ", value = ", ans, ", error = ", error)
        if error < 0.00001: # stops when error is less than this.
            break
        i += 1
    return ans



if __name__ == "__main__":
    value = 2.3
    ans = taylor_expo(value)
    print("The value for exp", value, "=", ans)