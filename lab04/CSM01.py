# _*_ coding: utf-8 _*_
# @Time : 2022/1/23 13:49
# @Author : 进击的大饼
# @File : CSM01 
# @Project : lab04
# Recursion Q1
def is_sorted(n):
    if n < 10:
        return True
    right = n % 10
    left = (n //10) % 10
    if left >= right:
        return is_sorted(n // 10)
    return False

# Tree Recursion Q1



# DISC03 Trees & Sequences

def tree(label, branches = []):
    return [label] + list(branches)

def label(tree):
    return tree[0]
def branches(tree):
    return tree[1 : ]
def is_leaf(tree):
    return not branches(tree)
# Q3.1
def tree_max(t):
    """
    我要把一颗tree上的所有label都集合到一个列表里面，然后max()
    smart
    """
    if not is_leaf(t):
        return max([label(t)] + [tree_max(b) for b in branches(t)])
    else:
        return label(t)

# Q3.2
def height(t):
    """
    Return the height of a tree.
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])


# Q3.3
def square_tree(t):
    return tree(label(t) ** 2, [square_tree(b) for b in branches(t)] )

# Q3.4
def find_path(tree, x):
    """
    我怎么找到5？从root node往下走，逐个检查分支；一个递归结构。
    >>>find_path(t, 5)
    [2, 7, 6, 5]
    什么时候要这个node，当且仅当这个node的所有分支至少有一个不是None
    """
    if label(tree) == x:
        return [x]
    if is_leaf(tree):
        return None
    s = [find_path(b, x) for b in branches(tree)]
    for i in s:
        if not i == None:
            return [label(tree)] + i
    return None



# Q3.5
def prune(t, k):
    if k == 0:
        return [label(t)]
    elif k == height(t):
        return t
    else:
        return tree(label(t), [prune(b, k-1) for b in branches(t)])