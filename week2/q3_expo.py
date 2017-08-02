import numpy as np

def taylor_expo(x):
    ans_list = [1]
    ans = 1
    print("iteration 1, value = 1")
    i = 1
    factorial = 1
    while True:
        previous_ans = ans
        factorial *= i
        ans += np.power(x, i)/factorial
        ans_list.append(ans)
        error = (ans-previous_ans)/(ans)*100
        print("iteration ", i+1, ", value = ", ans, ", error = ", error)
        if error < 0.00001:
            break
        i += 1
    print(ans)



if __name__ == "__main__":
    taylor_expo(1)