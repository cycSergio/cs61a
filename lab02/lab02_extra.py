""" Optional problems for lab02 """

from lab02 import *

# Higher Order Functions

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    return lambda x: f(g(x)) == g(f(x))



def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def f(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return f
# 总觉得不应该这样写，而是用lambda写一些肾么简单的句子。但是想不出来。
# 啊，震惊，发现参考答案也是这样写的。是不是增添了一些自信呢。


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
# 感觉有点难。看了参考答案，明天再来自己写一遍。
# To figure out which function we should next use in our cycle,
# we can use the mod operation via %, and loop through the function applications
# until we have made exactly n function applications to our original input x.





# disc02的内容也写在这里☀
#2.1
def product_rec(m, n):
    if m == 1:
        return n
    else:
        return n + product_rec(m - 1, n)
#2.2
def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        return countdown(n - 1)
#2.3
def countup(n):
    #你知道吗，一个函数里面可以不写return耶，( •̀ ω •́ )y！
    if n == 1:
        print(n)
    else:
        countup(n - 1)
        print(n)
#2.4

def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n % 10
        return last + sum_digits(n // 10)

i = 1
while i < 100:
    print(i, sum_digits(i))
    i+=1

#3.1
def count_stair_ways(n):
     if n == 1:
         return 1
     elif n == 2:
         return 2
     else:
         return (count_stair_ways(n - 1) + count_stair_ways(n - 2) )

# 啊，真的是这样写吗。等给给空下来了问一下他。
#3.2
def count_k(n, k):
    print(n, k)
    if n == 1:
        return 1
    if k == 1:
        return 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    i, count = 1, 0
    while i <= k:
        count = count + count_k(n-i, k)
        print(i, count)
        i += 1
    return count

