def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    
    # result = 1
    
    # while k > 0:
    #     tmp=n-k+1
    #     result *= tmp
    #     k-=1
    #     print('DEBUG: tmp=', tmp, 'result =', result, 'k =', k)
        
    # return result
    total = 1
    while k > 0:
        total *= n
        n -= 1
        k -= 1
        print('Debug:n=', n, 'k=', k,  'total=', total)
    return total
    





def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    f, count = 1, 0 
    while f <= n:
        if f % k == 0:
            print(f)
            count += 1
        f += 1
    return count








def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    
    total, x, n=0, 0, digit_number(y)
    while n >= 1:
        x = y // (10 ** n)
        y = y - x * (10 ** n)
        n -= 1
        total += x
        print("Debug:x =", x, 'n =', n, 'y =', y, 'total = ', total)
    return total + y % 10

 
def digit_number(y):
    n, f=1, 0
    while y >= n:
        n *= 10
        f += 1
    return f




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    while n:
        this_digit = n % 10
        n = n // 10
        next_digit = n % 10
        if this_digit == next_digit == 8:
            return True
    return False




