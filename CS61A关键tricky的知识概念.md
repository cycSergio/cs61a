# CS61A关键/tricky的知识概念

## 关于function的frame，name，environment啊等等相关的

来看两道我觉得非常tricky的问题，来自Lab02的Q4和Q5

**Q4**：Try drawing an environment diagram for the following code and predict what Python will output. **You do not need to submit or unlock this question through Ok.** Instead, you can check your work with the [Online Python Tutor](http://tutor.cs61a.org/), but try drawing it yourself first!

```python
>>> a = lambda x: x * 2 + 1
>>> def b(b, x):
...     return b(x + a(x))
>>> x = 3
>>> b(a, x)
______
```



**Q5**: Draw the environment diagram for the following code:

```python
n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)
```

There are 3 frames total (including the Global frame). In addition, consider the following questions:

1. In the Global frame, the name `add_ten` points to a function object. What is the intrinsic name of that function object, and what frame is its parent?
2. In frame `f2`, what name is the frame labeled with (`add_ten` or λ)? Which frame is the parent of `f2`?
3. What value is the variable `result` bound to in the Global frame?

![image-20220125175115020](C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220125175115020.png)



<font color = pink>对我而言，这个问题的难点就在于，最后f2这个frame中，k是多少？</font>

==我是在 global frame里面调用这个make_adder, 是先传进去/去找这个参数，然后再创建了新的一个frame。但是，参数传进去之后，我的参数和它的值之间的binding，是创建在我这个新的frame中的。== 比如，你看下面的make_withdra2(20) 和make_withdraw(7)

![image-20220126103355148](C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220126103355148.png)



我记得第一遍做的时候，这道题目给给给我讲了很久。最后明白了，但是隔了2个月再回头看感觉还是很需要理解。

当时的笔记是：

① 调用一个函数的时候，传进去的参数的值到底从哪里来？ →Local Frame，也就是它写在哪里。

②要区分调动函数的过程 & 执行body的过程

今天还复习了小蓝本上video的笔记，看见了这样一句很有启发很重要的句子：

A call expression and the body of the function being called are evaluated in ==不同环境==！

单独的Global Frame是一个环境，另外的sequences of frames是其他环境。

感觉很有启发，结合这句笔记，感觉自己真正理解了Q5.

##### 一道有趣的题目：

https://pythontutor.com/composingprograms.html#code=lamb%20%3D%20'da'%0Adef%20da%28da%29%3A%0A%20%20%20%20def%20lamb%28lamb%29%3A%0A%20%20%20%20%20%20%20%20nonlocal%20da%0A%20%20%20%20%20%20%20%20def%20da%28nk%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20da%20%3D%20nk%20%2B%20%5B'da'%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20da.append%28nk%5B0%3A2%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20nk.pop%28%29%0A%20%20%20%20da%28lamb%29%0A%20%20%20%20return%20da%28%5B%5B1%5D,2%5D%29%20%2B%203%0A%0Ada%28lambda%20da%3A%20da%28lamb%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

![image-20220206180649669](C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220206180649669.png)

感觉很能加深对于==怎么look up name==和==nonloca作用==的认识！



## 关于如何解决一个recursive的问题

![image-20220129125242731](C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220129125242731.png)



## 关于Non-local statement

先看这个withdraw的错误例子：

![image-20220125182941068](C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220125182941068.png)



<font color = pink>我的疑问是：为什么找不到balance呢？这个balance不能去 f1 里面找呢？f1不是 f2的parent 吗？</font>

把左边的balance改成amount，你不能修改一个parent的值！





### 2.7 object abstraction的内容

关于 repr 到底是什么意思，我目前的理解是，它是一个，如果你这个class中有定义_ _repr_ _ 这个class attribute， 那么你print（这个class中的实例）的时候，它能够给你返回一个string representation？ 



### 关于@property等相关问题：

这个写得很好：https://zhuanlan.zhihu.com/p/366156798



### 装饰器

#### 1、关于闭包

要想了解装饰器，首先要了解一个概念，闭包。什么是闭包，一句话说就是，在函数中再嵌套一个函数，并且引用外部函数的变量，这就是一个闭包了。光说没有概念，直接上一个例子。

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

print(outer(6)(5))
-----------------------------
>>>11
```

如代码所示，在outer函数内，又定义了一个inner函数，并且inner函数又引用了外部函数outer的变量x，这就是一个闭包了。在输出时，outer(6)(5),第一个括号传进去的值返回inner函数，其实就是返回6 + y，所以再传第二个参数进去，就可以得到返回值，6 + 5。

<font color = pink>啊，make_adder那个例子就是一个==闭包==。但是其实不明白到底什么是“闭包”。</font>

<img src="C:\Users\cyc\AppData\Roaming\Typora\typora-user-images\image-20220210222109444.png" alt="image-20220210222109444" style="zoom:67%;" />

#### 2、装饰器

接下来就讲装饰器，其实装饰器就是一个闭包，装饰器是闭包的一种应用。什么是装饰器呢，简言之，python装饰器就是用于**拓展原来函数功能的一种函数**，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在**不用更改原函数的代码前提下给函数增加新的功能**。使用时，再需要的函数前加上@demo即可。

```python
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def hello():
    print("hello")

hello()
-----------------------------
>>>[DEBUG]: enter hello()
>>>hello
```

例子中的装饰器给函数加上一个进入函数的debug模式，不用修改原函数代码就完成了这个功能，可以说是很方便了。

#### 3、带参数的装饰器

上面例子中的装饰器是不是功能太简单了，那么装饰器可以加一些参数吗，当然是可以的，另外装饰的函数当然也是可以传参数的。

```python
def logging(level):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(level, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return outwrapper

@logging(level="INFO")
def hello(a, b, c):
    print(a, b, c)

hello("hello,","good","morning")
-----------------------------
>>>[INFO]: enter hello()
>>>hello, good morning
```

如上，装饰器中可以传入参数，先形成一个完整的装饰器，然后再来装饰函数，当然函数如果需要传入参数也是可以的，用不定长参数符号就可以接收，例子中传入了三个参数。

#### 4、类装饰器

装饰器也不一定只能用函数来写，也可以使用类装饰器，用法与函数装饰器并没有太大区别，实质是使用了类方法中的**call**魔法方法来实现类的直接调用。

```python
class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter {}()".format(self.func.__name__))
        return self.func(*args, **kwargs)

@logging
def hello(a, b, c):
    print(a, b, c)

hello("hello,","good","morning")
-----------------------------
>>>[DEBUG]: enter hello()
>>>hello, good morning
```

类装饰器也是可以带参数的，如下实现

```python
class logging(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(self.level, func.__name__))
            return func(*args, **kwargs)
        return wrapper

@logging(level="TEST")
def hello(a, b, c):
    print(a, b, c)

hello("hello,","good","morning")
-----------------------------
>>>[TEST]: enter hello()
>>>hello, good morning
```

## 一些积累 挠头

### 一个数的因素个数怎么求？

首先看看这个数小于等于其算数平方根的因数有多少，例如24小于其算术平方根的因数有1，2 ，3，4 总共4个，那么其总的因数有4*2=8个，因为每个小于其算数平方根的因数（a）必定对应了另一个大于等于其算数平方根的因素（b）（a * b = 24哈）。



## Tree相关的

### 定义Tree Class & Binary Tree

```python
# Trees

class Tree:
    """A tree with label as its label value."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.label)] + indented

    def is_leaf(self):
        return not self.branches

def leaves(tree):
    """Return the leaf values of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.label]
    else:
        return sum([leaves(b) for b in tree.branches], [])

# Binary trees

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty' 
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)

def fib_tree(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

def contents(t):
    """The values in a binary tree.

    >>> contents(fib_tree(5))
    [1, 2, 0, 1, 1, 5, 0, 1, 1, 3, 1, 2, 0, 1, 1]
    """
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)

# Binary search trees

def bst(values):
    """Create a balanced binary search tree from a sorted list.

    >>> bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left, right = bst(values[:mid]), bst(values[mid+1:])
    return BTree(values[mid], left, right)

def largest(t):
    """Return the largest element in a binary search tree.

    >>> largest(bst([1, 3, 5, 7, 9]))
    9
    """
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)

def second(t):
    """Return the second largest element in a binary search tree.

    >>> second(bst([1, 3, 5]))
    3
    >>> second(bst([1, 3, 5, 7, 9]))
    7
    >>> second(Tree(1))
    """
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.label
    else:
        return second(t.right)

# Sets as binary search trees

def contains(s, v):
    """Return true if set s contains value v as an element.

    >>> t = BTree(2, BTree(1), BTree(3))
    >>> contains(t, 3)
    True
    >>> contains(t, 0)
    False
    >>> contains(bst(range(20, 60, 2)), 34)
    True
    """
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    elif s.label > v:
        return contains(s.left, v)

def adjoin(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = bst(range(1, 10, 2))
    >>> adjoin(b, 5) # already contains 5
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7)))
    >>> adjoin(b, 6)
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7, BTree(6))))
    >>> contents(adjoin(adjoin(b, 6), 2))
    [1, 2, 3, 5, 6, 7, 9]
    """
    if s is BTree.empty:
        return BTree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin(s.right, v))
    elif s.label > v:
        return BTree(s.label, adjoin(s.left, v), s.right)
```

### Morse Code的例子

```python
# Morse tree

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
    """Return a tree representing the code. Each internal (non-leaf) node
    of the tree other than its root is a signal. Each leaf node
    is a letter encoded by the path from the root.

    >>> pretty(morse(abcde))
       None   
     /    \   
     .    -   
    / \   |   
    - e   .   
    |    /  \ 
    a    .  - 
        / \ | 
        . d . 
        |   | 
        b   c 
    """
    whole = Tree(None)
    for letter, signals in sorted(code.items()):
        t = whole
        for s in signals:
            if s in [b.label for b in t.branches]:
                t = [b for b in t.branches if b.label == s][0]
            else:
                b = Tree(s)
                t.branches.append(b)
                t = b
        t.branches.append(Tree(letter))
    return whole

def decode(signals, tree):
    """Decode signals into a letter according to tree, assuming signals
    correctly represents a letter.  tree has the format returned by
    morse().

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.label == signal][0]
    leaves = [b for b in tree.branches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].label
    
# Link & Tree

class Link:
    """A linked list."""
    empty=()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

class Tree:
    """A tree with label as its label value."""
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

def height(tree):
    """The height of a tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])

def width(tree):
    """Returns the printed width of this tree."""
    label_width = len(str(tree.label))
    w = max(label_width,
            sum([width(t) for t in tree.branches]) + len(tree.branches) - 1)
    extra = (w - label_width) % 2
    return w + extra

def pretty(tree):
    """Print a tree laid out horizontally rather than vertically."""

    def gen_levels(tr):
        w = width(tr)
        label = str(tr.label)
        label_pad = " " * ((w - len(label)) // 2)
        yield w
        print(label_pad, file=out, end="")
        print(label, file=out, end="")
        print(label_pad, file=out, end="")
        yield 

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

    out = StringIO()
    h = height(tree)
    g = gen_levels(tree)
    next(g)
    for i in range(2*h + 1):
        next(g)
        print(file=out)
    print(out.getvalue(), end="")
```

