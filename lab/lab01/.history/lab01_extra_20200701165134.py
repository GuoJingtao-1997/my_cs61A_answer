"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    falling_result = 1
    if k == 0:
        falling_result
    else:
        while k:
            falling_result = falling_result * n
            n -= 1
            k -= 1
    return falling_result
print(falling(4,3))    
    
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
    while n:
        temp_num1 = n % 10
        print(temp_num1)
        n = n // 10
        temp_num2 = n % 10
        print(temp_num2)
        n = n // 10
        if temp_num1 == 8 and temp_num2 == 8:
            cmp_result = True
            print("hr1")
            break
        else:
            print("hr2")
            cmp_result = False
    return cmp_result
print(double_eights(2882))


