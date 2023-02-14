""" Optional problems for Lab 3 """

from lab03 import *

#Q4: I heard you like Funcionts
## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def h(n):
        def f(x):
            if n == 0:
                return x
            i = 1
            while i <= n:
                if i % 3 == 1:
                    x = f1(x)
                elif i % 3 == 2:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return f
    return h

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

#Q8 hint: you will need a helper function
# iteration的写法是这样的
'''
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True
'''
# 以及，判断素数的时候，枚举到它的根号就可以了
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 2:
        return True
    else:
        return helper(n, 2)

def helper(n, k):
    if n % k == 0:
        return False
    if k * k > n:
        return True
    return helper(n, k + 1)

#Q9 也还是用到helper
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n == 1:
        return odd_term(1)
    else:
        return helper2(n, odd_term, even_term, 1)

def helper2(n, odd_term, even_term, k):
    if k <= n - 2:
        return odd_term(k) + even_term(k + 1) + helper2(n, odd_term, even_term, k + 2)
    if k == n:
        return odd_term(k)
    if k == n - 1:
        return odd_term(k) + even_term(k + 1)




def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 19
            :
        return 0
    else:
        return helper3(n, 0)

def helper3(n, t):# t = how many times a digit appears in n
    allButLast, last = n // 10, n % 10
