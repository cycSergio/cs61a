## zju python程序设计

## 第三章

### 8 - 有关sort的用法！易错⭐⭐

如果一个字符串是 另一个字符串的重新排列组合，那么这两个字符串互为变位词。比如，”heart”与”earth”互为变位 词，”Mary”与”arMy”也互为变位词。

### 输入格式:

第一行输入第一个字符串，第二行输入第二个字符串。

### 输出格式:

输出“yes”,表示是互换词，输出“no”,表示不是互换词。

### 输入样例1:

在这里给出一组输入。例如：

```in
Mary
arMy
```

### 输出样例1

在这里给出相应的输出。例如：

```out
yes
```

### 输入样例2:

在这里给出一组输入。例如：

```in
hello 114
114 hello
```

### 输出样例2:

在这里给出相应的输出。例如：

```out
yes
```

### 输入样例3:

在这里给出一组输入。例如：

```in
Wellcom
mocllew
```

### 输出样例3:

在这里给出相应的输出。例如：

```out
no
```

```python
str1 = list(input())
str2 = list(input())
str1.sort()
str2.sort()
if str1 == str2:
    print("yes")
else:
    print("no")
```

<font color = pink>要特别注意的是，list.sort()并不返回任何值，所以不能有 a = a.sort()这样的写法，单是a.sort()就可以了，a就已经被sort过了。</font>

### 9 - 序列中有元素相同，怎么返回索引更大的那个？ ⭐

输入字符串，排序后输出最大字符及该字符在原字符串中的索引。相同字符的索引取最大值。提示：用元组实现。

### 输入格式:

在一行输入字符串。

### 输出格式:

在一行输出字符和索引。

### 输入样例:

在这里给出一组输入。例如：

```in
Hello Python
```

### 输出样例:

在这里给出相应的输出。字符和数字间空3格。例如：

```out
y   7
```

```python
ipt = tuple(input())
now = ipt[0]
idx = 0
for i in range(1, len(ipt)):
    if ipt[i] >= now:
        now = ipt[i]
        idx = i
print(now, " ", idx)
```

<font color  = pink>如果字符相同，取索引最大值。此处的处理学习！之前自己是没想到的。</font>

### 10 - 给定n，怎么换行输入n行input？ ⭐

编写程序，用于计算有n(1<n<10)个字符串中最长的字符串的长度。前导空格不要计算在内！

### 输入格式:

在第一行中输入n,接下的每行输入一个字符串

### 输出格式:

在一行中输出最长的字符串的长度

### 输入样例:

在这里给出一组输入。例如：

```in
4	
        blue
yellow
red
green
```

### 输出样例:

在这里给出相应的输出。例如：

```out
length=6
```

```python
n = int(input())
length = 0
result = ''
for i in range(0, n):
    str_input = input().strip()
    if len(str_input) >= length:
        length = len(str_input)
        result = str_input
print("length={0}".format(length))
```



### 17 - 查验身份证 ⭐⭐