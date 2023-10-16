import math  
  
def nearest_sq(n, prev_square=None, prev_dist=None):  
    if n == 0:  
        return 1  
    sqrt_n = math.isqrt(n)  
    square = sqrt_n ** 2  
    if sqrt_n ** 2 == n:  
        return square  
    elif prev_square is not None and prev_dist is not None:  
        dist = abs(n - prev_square)  
        if dist < prev_dist:  
            return prev_square  
    prev_square = square  
    prev_dist = abs(n - square)  
    if n - square < (sqrt_n + 1) ** 2 - n:  
        return square  
    else:  
        return (sqrt_n + 1) ** 2