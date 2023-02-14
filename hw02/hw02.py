HW_SOURCE_FILE = 'hw02.py'

def square(x):
    return x * x

def identity(x):
    return x

triple = lambda x: 3 * x

increment = lambda x: x + 1

add = lambda x, y: x + y

mul = lambda x, y: x * y

def product(n, term):
    """Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    outcome, k = 1, 1
    while k <= n:
        outcome, k = outcome * term(k), k+1
    return outcome

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return product(n, identity)


def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda k: k + n

# 一些discussion02的内容
#1.1
def wears_jacket(temp, raining):
    return temp < 60 or raining
#1.2
def handle_overflow(s1, s2):
    '''
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    Move to Section 2: 1
    >>> handle_overflow(20, 32)
    Move to Section 1: 10
    >>> handle_overflow(35,30)
    No space left in either section
    '''
    if s1 <= 30 and s2 <= 30:
        print('No overflow')
    elif s1 < 30 and s2 > 30:
        print('Move to Section 1: ', abs(s1-30))
    elif s1 > 30 and s2 < 30:
        print('Move to Section 2: ', abs(s2 - 30))
    else:
        print('No space left in either section')
    return

#1.3
#1.4
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



#2.1
def keep_ints(cond, n):
    k = 1
    while k <= n:
        if cond(k):
            print(k)
        k += 1
def is_even(x):
    return x % 2 == 0

#2.2
def outer(n):
    def inner(m):
        return n - m
    return inner

#2.3
def keep_ints(n):
    def inner_cond(cond):
        k = 1
        while k <= n:
            if cond(k):
                print(k)
            k += 1
        return
    return inner_cond

def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return x % 2 == 1

#3.1


#3.2
