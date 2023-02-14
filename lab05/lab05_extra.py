""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev] += [word]
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result = result + word + ' '
        next = random.choice(table[word])
        word = next
    return result.strip() + word

#def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
#    import os
#    from urllib.request import urlopen
#    if os.path.exists(path):
#        return open('shakespeare.txt', encoding='ascii').read().split()
#    else:
#        shakespeare = urlopen(url)
#        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
#tokens = shakespeare_tokens()
#table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Q8
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.
    那我首先就是要找出leaf嘛，然后判断是不是要删除这个leaf
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) in vals:
            return None
        else:
            return tree(label(t))
    else:
        pru_branch = [prune_leaves(b, vals) for b in branches(t)]
        real_branch = []
        for i in pru_branch:
            if not i == None:
                real_branch += [i]
        return tree(label(t), real_branch)



# Q9
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(i) for i in vals])
    else:
        sp_branch = [sprout_leaves(b, vals) for b in branches(t)]
        return tree(label(t), sp_branch)

# Q10
import itertools
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if t2 is None:
        return t1
    if t1 is None:
        return t2
    label_new = label(t1) + label(t2)
    zipped_branch = itertools.zip_longest(branches(t1), branches(t2), fillvalue=None)
    new_branch = [add_trees(x, y) for x, y in zipped_branch]
    return tree(label_new, new_branch)








def sum_of_nodes(t):
    if is_leaf(t):
        return label(t)
    else:
        s = 0
        for b in branches(t):
            s += sum_of_nodes(b)
        return label(t) + s

def sum_nodes(t):
    if is_leaf(t):
        return label(t)
    else:
        return sum([label(t)] + [sum_nodes(b) for b in branches(t)])


