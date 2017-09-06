##Question 1. Part A).

### the values of x that lead to most inaccurate result in terms of relative error.
For `my_log1p(x)` the values of x which leads to the most inaccurate result are values which greater than 1. This is due to the fact that the degree of each term grows linearly, which results us taking `x^n` when x is greater than 1, the term `x^n` diverges as n grows. Consequently, the Taylor expansion fails to converge to an accurate value for `log(1+x)`. 

In almost all cases, an input of x greater than 1 will result in the function diverging and returning an error due to overflow.

### identify/describe the adv/limitations of using the above expansion

The advantages:

* This implementation of log1p is able to compute values which are much smaller than machine epsilon very accurately to the reference inbuilt `np.log1p(x)`.
* The output converge to an acceptable output within an acceptable time for x between 0 and 1.

The disadvantages:

* None linear complexity compare to the other inbuilt algorithms.
* Can only be used within the range of x between 0 and 1.
* It's less accurate than the inbuilt `log(1+x)` for range of x between machine eps and 1


### specify the value of x for which you would use the expansion over the inbuilt.
Summarising the above advantages and disadvantages. We can conclude that the only usable range for `my_log1p(x)` is for x between 0 and machine epsilon (`2.22044604925e-16`)

Observe the graph below showing the relative errors. The function `my_log1p` produces good results even when the input are much less than machine eps. However, the inbuilt log function was unable to handle the addition `x+1` for x being less than machine eps. Consequently, the huge error spike in green towards 0.

![q1a_output](./img/script1_output.png)
*Figure 1: computation time and relative error of the algorithms.*