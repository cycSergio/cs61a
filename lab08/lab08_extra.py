""" Extra questions for Lab 08 """

from lab08 import *


# OOP
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        self.buttons = [*args]
        self.my_dict = {a.pos: a.key for a in [*args]}

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        "*** YOUR CODE HERE ***"
        self.buttons[info].pressed += 1
        return self.my_dict[info]

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        "*** YOUR CODE HERE ***"
        my_str = ''
        for i in typing_input:
            my_str += self.my_dict[i]
            self.buttons[i].pressed += 1
        return my_str


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0


# Nonlocal
def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    "*** YOUR CODE HERE ***"
    global_count = 0

    def counter():
        count = 0

        def action(ipt):
            nonlocal global_count
            nonlocal count
            if ipt == 'count':
                count += 1
                return count
            elif ipt == 'global-count':
                global_count += 1
                return global_count
            elif ipt == 'reset':
                count = 0
            elif ipt == 'global-reset':
                global_count = 0

        return action

    return counter


# Lists
def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    "*** YOUR CODE HERE ***"

    sum1, sum2 = first[0], second[0]
    result = 0
    while m <= len(first) and n <= len(second):
        if sum1 == sum2:
            result = 1
            break
        elif sum1 < sum2:
            if m >= len(first):
                break
            sum1 += first[m]
            m += 1
        elif sum1 > sum2:
            if n >= len(second):
                break
            sum2 += second[n]
            n += 1

    if result == 1:  # change this line!
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


# Recursive objects
def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """
    "*** YOUR CODE HERE ***"

    def trans(lst):
        trans_str = ''
        count_back = 0
        while lst is not Link.empty:
            trans_str += front + str(lst.first) + mid
            lst = lst.rest
            count_back += 1
        trans_str += empty_repr + count_back * back
        return trans_str

    return trans


def tree_map(fn, t):
    """Maps the function fn over the entries of t and returns the
    result in a new tree.

    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return Tree(fn(t.label))
    else:
        new_tree = []
        for b in t.branches:
            new_tree.append(tree_map(fn, b))
    return Tree(fn(t.label), new_tree)


def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    "*** YOUR CODE HERE ***"
    # def mypath(t):
    #     if t.is_leaf():
    #         return [Link(t.label)]
    #     else:
    #         lst = []
    #         for b in t.branches:
    #             path_list = mypath(b)
    #             for path in path_list:
    #                 lst.append(Link(t.label, path))
    #     return lst
    # all_path = mypath(tree)
    # real_list = []
    # for i in all_path:
    #     i_count = 0
    #     copy_i = Link(i.first, i.rest)
    #     while copy_i.rest is not Link.empty:
    #         i_count += 1
    #         copy_i = copy_i.rest
    #     if i_count >= n:
    #         real_list.append(i)
    # return real_list
    lst = []
    if tree.is_leaf():
        if n > 0:
            return None
        else:
            return [Link(tree.label)]
    else:
        for b in tree.branches:
            paths = long_paths(b, n - 1)
            if not paths is None:
                for p in paths:
                    this_path = Link(tree.label, p)
                    lst.append(this_path)
    return lst

# Orders of Growth
def zap(n):
    i, count = 1, 0
    while i <= n:
        while i <= 5 * n:
            count += i
            print(i / 6)
            i *= 3
    return count


def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n * n:
        while b <= n * n:
            sum += (a * b)
            b += 1
        b = 0
        a += 1
    return sum


# Tree class
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


# mentor05

def skip(lst):
    if lst is Link.empty:
        return lst
    elif lst.rest is Link.empty:
        return Link(lst.first)
    return Link(lst.first, skip(lst.rest.rest))


def new_skip(lst):
    if lst is Link.empty:
        return lst
    elif lst.rest is Link.empty:
        return lst
    lst.rest = lst.rest.rest
    new_skip(lst.rest)
