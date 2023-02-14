""" Optional problems for Lab 6 """


## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    count = 0

    def give_one():
        nonlocal count
        count += 1
        return snacks[count % len(snacks) - 1]

    return give_one


# questions from Disc04

def memory(n):
    def input_func(g):
        nonlocal n
        print(g(n))
        n = g(n)
        return input_func

    return input_func


pokemon = {'jolteon': 135, 'pikachu': 25, 'dragonair': 148, 'mew': 151, 'ditto': 25}


def group_by(s, fn):
    result_dict = {}
    mylist = [[fn(e), e] for e in s]
    for m in mylist:
        if m[0] not in result_dict:
            result_dict[m[0]] = [m[1]]
        else:
            result_dict[m[0]] += [m[1]]
    return result_dict


def replace_all_deep(d, x, y):
    for key, value in d.items():
        if value == x:
            d[key] = y
        elif type(value) == dict:
            replace_all_deep(value, x, y)


def add_this_many(x, el, lst):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    for i in range(count):
        lst.append(el)


def reverse(lst):
    replace_idx = 0
    for i in lst:
        lst.insert(replace_idx, lst.pop())
        replace_idx += 1


a = [1, 2, [3, 4]]
b = list(a)


def has_seven(k):
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def make_pingpong_tracker():
    index, current, add = 1, 0, True

    def pingpong_tracker():
        nonlocal index, current, add
        if add:
            current += 1
        else:
            current -= 1
        if has_seven(index) or index % 7 == 0:
            add = not add
        index += 1
        return current

    return pingpong_tracker


# def accumulate(lst):
#     all_sum = []
#     for i in lst:
#         idx = lst.index(i)
#         if isinstance(i, list):
#             inside = accumulate(i)
#         else:
#             i_sum = sum([i for i in lst[:idx + 1]])
#             all_sum.append(i_sum)
#     return all_sum


def accumulate(lst):
    old_lst = lst[:]
    my_sum = 0
    for i in old_lst:
        idx = lst.index(i)
        if isinstance(i, list):
            inside = accumulate(i) #return 的是这个list中元素的和！
            lst[idx] = i
            my_sum += inside
        else:
            my_sum += i
            lst[idx] = my_sum
    return my_sum
