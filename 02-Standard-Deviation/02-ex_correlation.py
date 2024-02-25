# Simple code to calc the Correlation Coefficient.
import math


def co_sum(x, y):
    if len(x) != len(y):
        raise Exception("Please ensure you have the same number of scores for both your X and Y variable.")
    
    x_sum = 0
    y_sum = 0
    xy_sum = 0
    x_pow = 0
    y_pow = 0
    n = len(x)
    for i in range(n):
        x_sum += x[i] 
        y_sum += y[i]
        xy_sum += x[i] * y[i]
        x_pow += pow(x[i],2)
        y_pow += pow(y[i],2)
    # print(x_sum, y_sum, xy_sum, x_pow, y_pow)
    
    a = n*xy_sum - x_sum*y_sum
    b = math.sqrt((n*x_pow - x_sum**2))
    c = math.sqrt((n*y_pow - y_sum**2))
    
    result = a / (b * c)
    print(f" r = {result}")


# Test code | r should be 0.9984
co_sum([1,2,3,4,5,6], [2,4,7,9,12,14])
