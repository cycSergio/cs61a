"""Lab 1: Expressions and Control Structures"""

# Coding Practice

#Q3:
import math


def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"

    c = 0
    while c < n:
        x = f(x)
        c += 1
    return x

#Q4:
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    import math
    c = 1
    d = 1
    while n // d >= 10:
        d = 10 * d
        c += 1
    # 这样算它有几位数有点麻烦，下面这个更好
    # temp_n = n
    # while n != 0:
    #     n = n // 10
    #     c += 1
    realSum = 0
    while c > 0:
        sum = n // math.pow(10,c-1)
        realSum = realSum + sum
        n = n % math.pow(10,c-1)
        c -= 1

    return int(realSum)


#Q5：一道可以反复多做的题
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

    # print("debug here")
    c = 1
    d = 1
    # while n // d >= 10:
    #     d = 10 * d
    #     c += 1
    # # print(d, c)
    # while c > 0:
    #     digit = n // math.pow(10, c -1)
    #     # print(digit, c)
    #     if digit == 8:
    #         n = n % math.pow(10, c - 1)
    #         double = n // math.pow(10, c - 2)
    #         # print("double = ",double)
    #         if double == 8:
    #             c = 0（这里就算没有这个，while也会跳出去的。因为return了之后，整个def的函数就是结束了
    #             return True
    #         else:
    #             n = n % math.pow(10, c - 1)
    #             c -= 1
    #     else:
    #         n = n % math.pow(10, c - 1)
    #         c -= 1
    # return False（False是写在最外面的，可以理解一下。之前自己写的时候没写这个，那么如果199976这样
    #就是没有连续双8的数字，不就是没有返回值的吗。再理解一下。
    # 上面标成注释的是我的垃圾写法，从高位一个个往后判断。下面是给给的优秀写法，从个位判断。
    # flag is the number of previous bit，往前一位的数字。一般都是从个位开始遍历的，you know?
    flag = -1
    while n:
        # bit is the least bit
        bit = n % 10 # 任何数%10都能得到它的个位啊！！！！！！！
        print("present n = ", n, "least bit=", bit, "last bit=",flag)

        if (flag == 8 and bit == 8):
            return True
        else:
            flag = bit
        n = n // 10
    return False
