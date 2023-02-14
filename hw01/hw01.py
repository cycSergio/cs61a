from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a * a + b * b + c * c - min(a, b, c) * min(a, b, c)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    x = n-1
    while not (n % x == 0):
        x = x - 1
        # print('x is ', x)
    return x

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False
def t():
    "*** YOUR CODE HERE ***"
    return print(2)
def f():
    "*** YOUR CODE HERE ***"
    return print(1)
'''这道题目的两个要点是：
    ①在if_statement中，有一个return是不会被执行的——短路；
    但是在if_function中，c(),t(),f()都是把函数执行完了以后的参数传进去，每一个都会被执行
    在执行return if_function(c(), t(), f())时，解释器会首先计算3个函数，
    并将函数返回值作为参数传入if_function，c()的返回值不会影响t()和f()的执行
    ②pure-function 和non-pure function
    参考答案见下：
    def c():
        return False

    def t():
        print(1)

    def f():
        print(2)
    '''



# Q5
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n != 1:
        print(n)
        count = count + 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3*n + 1)
    print(1)
    return count+1
    # Q5 和参考答案一样

'''hw01 1121 done
   needs review~
'''

def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('61A is awesome!')

what_prints()

