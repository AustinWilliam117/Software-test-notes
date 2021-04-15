## Python笔记

注意python的缩进

### 变量和赋值

1. 变量命名规则

   - 变量名必须是字母，数字，下划线，但是不能用数字开头（规则和C语言一样）

   - 变量名大小写敏感
   - 变量命名要做到“见名知意”

   ```python
   >>> name = 'william'
   >>> print('hello,$s' %name)
   hello,william
   
   >>> age = 18
   >>> height = 1800.2000001
   >>> print('hello %s, 今年你%d岁了,有%3.2f' %(name,age,height))
   hello william, 今年你18岁了,有180.20
   ```

2. 赋值
   - 动态类型 type（变量名）
   - python 不支持++ / --

### 字符串

- r 转义全部失效 `print(r"hello world! \n 'I love python'")`

### 切片

```python
>>> word = 'adcdefghjklmn'
>>> print(word[0:3])  # 左闭右开
adb

# 字符串翻转
>>> a = 'abcdefg'
>>> print(a[::-1])
```

python 没有字符类型

### 注释

```python
# 查看系统默认编码方式
>>> import sys
>>> print(sys.getdefaultencoding())
utf-8

"""
这也是以一种注释啦
"""
```

### 取余数

```python
# 判断闰年
year = int(input("请输入某一年，将自动判断是否为闰年: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))  
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))
else:
   print("{0} 不是闰年".format(year))

# 质数判断

num = int(input("请输入一个数字，来判断是否为质数: "))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"不是质数")
            break
    else:
        print(num,"是质数")
else:
    print("请输入一个大于1的整数")
```

###  format 格式化函数

Python2.6 开始，新增了一种格式化字符串的函数 **str.format()**，它增强了字符串格式化的功能。

基本语法是通过 **{}** 和 **:** 来代替以前的 **%** 。

format 函数可以接受不限个参数，位置可以不按顺序。

```python
>>> "{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

print("网站名：{name}, 地址 {url}".format(name="mengxun", url="mengxun.club"))
 
# 通过字典设置参数
>>> site = {"name": "mengxun", "url": "mengxun.club"}
>>> print("网站名：{name}, 地址 {url}".format(**site))
网站名：mengxun, 地址 mengxun.club
 
# 通过列表索引设置参数
>>> my_list = ['mengxun', 'mengxun.club']
>>> print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
网站名：mengxun, 地址 mengxun.club
```

### 数字格式化

下表展示了 str.format() 格式化数字的多种方法：

```python
>>> print("{:.2f}".format(3.1415926))
3.14
```

| 数字       | 格式                                                         | 输出                   | 描述                         |
| :--------- | :----------------------------------------------------------- | :--------------------- | :--------------------------- |
| 3.1415926  | {:.2f}                                                       | 3.14                   | 保留小数点后两位             |
| 3.1415926  | {:+.2f}                                                      | +3.14                  | 带符号保留小数点后两位       |
| -1         | {:+.2f}                                                      | -1.00                  | 带符号保留小数点后两位       |
| 2.71828    | {:.0f}                                                       | 3                      | 不带小数                     |
| 5          | {:0>2d}                                                      | 05                     | 数字补零 (填充左边, 宽度为2) |
| 5          | {:x<4d}                                                      | 5xxx                   | 数字补x (填充右边, 宽度为4)  |
| 10         | {:x<4d}                                                      | 10xx                   | 数字补x (填充右边, 宽度为4)  |
| 1000000    | {:,}                                                         | 1,000,000              | 以逗号分隔的数字格式         |
| 0.25       | {:.2%}                                                       | 25.00%                 | 百分比格式                   |
| 1000000000 | {:.2e}                                                       | 1.00e+09               | 指数记法                     |
| 13         | {:>10d}                                                      | 13                     | 右对齐 (默认, 宽度为10)      |
| 13         | {:<10d}                                                      | 13                     | 左对齐 (宽度为10)            |
| 13         | {:^10d}                                                      | 13                     | 中间对齐 (宽度为10)          |
| 11         | `'{:b}'.format(11) '{:d}'.format(11) '{:o}'.format(11) '{:x}'.format(11) '{:#x}'.format(11) '{:#X}'.format(11)` | `1011 11 13 b 0xb 0XB` | 进制                         |

**^**, **<**, **>** 分别是居中、左对齐、右对齐，后面带宽度， **:** 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

**+** 表示在正数前显示 **+**，负数前显示 **-**； （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制

```python
# 此外我们可以使用大括号 {} 来转义大括号，如下实例：
>>> print ("{} 对应的位置是 {{0}}".format("mengxun"))
mengxun 对应的位置是 {0}
```

### 整除

```python
>>> print(5%3)
2
>>> print(5/-3)
-1.6666666666666667
>>> print(5//-3) # 取最小整数
-2
>>> print(5//3)
1
```

### 字符串比较

```python
# 0~9 < A~Z < a~z
>>> print('az' < 'bc')
True

# 字符串只比较第一个值的大小

>>> print('123' < '23')
True
```

### 元组（ tuple ）

Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号 **( )**，列表使用方括号 **[ ]**。

```python
>>> tup1 = ("google","runoob",1997,2000)                                               >>> tup3 = "1",'a','c','d'                                                             >>> type(tup3) 	#  不需要括号也可以 
<class 'tuple'>

>>> print(tup)
('1', 'a', 'c', 'd')                                                                
```

元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：

```python
>>> tup1 = (50)
>>> type(tup1)     # 不加逗号，类型为整型
<class 'int'>

>>> tup1 = (50,)
>>> type(tup1)     # 加上逗号，类型为元组
<class 'tuple'>
```

元组可以使用下标索引来访问元组中的值，如下实例:

```python
>>> tup1 = ('Google', 'Runoob', 1997, 2000)
>>> tup2 = (1, 2, 3, 4, 5, 6, 7 )
>>> print ("tup1[0]: ", tup1[0])
Google
>>> print ("tup2[1:5]: ", tup2[1:5])
(2,3,4,5)
```

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

```python
>>> tup1 = (12, 34.56)
>>> tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
>>> tup3 = tup1 + tup2
>>> print (tup3)
(12,34.56,'abc','xyz')

# 更改元组中的列表，而不是元组中的元素
>>> tup1 = (12,'ab',[2,98,'d'])
>>> tup1[2][1] = 5	
>>> tup1[2][2] = 1

>>> print(tup1)
(12, 'ab', [2, 5, 1])

# 嵌套
>>> tup2 = (12,'ac',[2,(1,2,[1,2]),'p'],'xc') # 更改最里面列表的值
>>> tup2[2][1][2][0] = 'pd'
>>> print(tup2)
(12, 'ac', [2, (1, 2, ['pd', 2]), 'p'], 'xc')
```

删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

```python
>>> tup1 = (12,'ab',[2,98,'d'])
>>> print(tup1)
(12, 'ab', [2, 98, 'd'])
>>> del tup1
>>> print(tup1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tup1' is not defined
```

元组运算符

与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

| Python 表达式                  | 结果                         | 描述         |
| :----------------------------- | :--------------------------- | :----------- |
| len((1, 2, 3))                 | 3                            | 计算元素个数 |
| (1, 2, 3) + (4, 5, 6)          | (1, 2, 3, 4, 5, 6)           | 连接         |
| ('Hi!',) * 4                   | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制         |
| 3 in (1, 2, 3)                 | True                         | 元素是否存在 |
| for x in (1, 2, 3): print (x,) | 1 2 3                        | 迭代         |

元组索引

```python
tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo','Weixin')
```

| Python 表达式 | 结果                                            | 描述                                             |
| :------------ | :---------------------------------------------- | :----------------------------------------------- |
| tup[1]        | 'Runoob'                                        | 读取第二个元素                                   |
| tup[-2]       | 'Weibo'                                         | 反向读取，读取倒数第二个元素                     |
| tup[1:]       | ('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin') | 截取元素，从第二个开始后的所有元素。             |
| tup[1:4]      | ('Runoob', 'Taobao', 'Wiki')                    | 截取元素，从第二个开始到第四个元素（索引为 3）。 |

元组内置函数

```python
# 计算元组个数
>>> tuple = "11a","22b","3ad",123
>>> print(len(tuple))
4

# 元组中的最大值
>>> tuple = "11a","22b","3ad","123"
>>> print(max(tuple))
3ad

# 元组中的最小值
>>> tuple = "11a","22b","3ad","123"
>>> print(min(tuple))
11a

# 列表转化元组 tuple对象是不可调用的
>>> list1 = ["google","taobao","douban"]
>>> tuple1 = tuple(list1)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
```

元组是不可变的

所谓元组的不可变指的是元组所指向的内存中的内容不可变。

```python
>>> print(tup)
('1', '', '2', '3')
>>> id(tup)	# 查看内存地址
2102191068880

>>> tup = (1,2,3)
>>> id(tup)	
2102191014400

>>> tup1 = ('1','','2','3')
>>> id(tup1)
2102191068880	# 内存地址相同
```

### 排序

- sorted：返回一个有序的序列（**输出参数的副本**）

```python
>>> p = [2,6,7,9,1,4,6,0,]
>>> sorted(p)
[0, 1, 2, 4, 6, 6, 7, 9]
>>> print(p)
[2, 6, 7, 9, 1, 4, 6, 0]

# 逆排序
>>> p = [2,6,7,9,1,4,6,0,]
>>> print(sorted(p, reverse=True))
[9, 7, 6, 6, 4, 2, 1, 0]

# 按字符串长度排序
>>> m = ("11111","aa","cc","p","1x")
>>> print(sorted(m, key = len))
['p', 'cc', 'aa', '1x', '11111']	# 元组不可更改,长度相同没有顺序吧？

>>> print(sorted(m, key = len, reverse=True))
['11111', 'cc', 'aa', '1x', 'p']
```

- sort：返回一个有序序列，更改原内容

```python
>>> a = [-2,5.6,7,-24,91,87,6]
>>> sorted(a)
[-24, -2, 5.6, 6, 7, 87, 91]
>>> a
[-2, 5.6, 7, -24, 91, 87, 6]
>>> a.sort()
>>> a
[-24, -2, 5.6, 6, 7, 87, 91]
```

### 字典

字典是完全无序的映射集合

1. 字典无序：当你遍历字典元素时，与你添加元素的顺序、与你访问元素的顺序均无任何关联！
2. 当你遍历一个字典对象时，如果与你添加元素的顺序是一样的，这仅仅是个巧合而已，需要元素有序的字典请看OrderedDict

```python
# 修改字典
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict['Age'] = 18
>>> dict.update({"Name":"AustinWilliam117"})
>>> dict
{'Name': 'AustinWilliam117', 'Age': 18, 'Class': 'First'}

# 删除字典元素
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> del dict['Class']
>>> dict
{'Name': 'William', 'Age': '17'}
>>> dict.clear()
>>> dict
{}
```

内置方法

```python
# 删除字典所有内容
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict.clear()
>>> dict
{}

# 返回一个浅复制(创建新对象，其内容是原对象的引用)
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict.copy()
{'Name': 'William', 'Age': '17', 'Class': 'First'}

# 以列表返回可遍历的(键, 值) 元组数组
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> for key,values in dict.items():
    	print(key,values)
        
Name William
Age 17
Class First

# 判断键在字典dict里返回true，否则返回false
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> 'Name' in dict
True

# 返回一个迭代器，可以使用 list() 来转换为列表
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict.values()
dict_values(['William', '17', 'First'])
>>> dict.keys()
dict_keys(['Name', 'Age', 'Class'])

# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict.pop('Name')
'William'
>>> dict
{'Age': '17', 'Class': 'First'}

# 随机返回并删除字典中的最后一对键和值
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> dict.popitem()
>>> dict
{'Name': 'William', 'Age': '17'}
```

内置函数

```python
# 计算字典元素个数，即键的总数
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> len(dict)
3

# 输出字典，可以打印的字符串表示
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> str(dict)
"{'Name' : 'William', 'Age' : '17', 'Class' : 'First'}"

# 返回输入的变量类型，如果变量是字典就返回字典类型
>>> dict = {'Name' : 'William', 'Age' : '17', 'Class' : 'First'}
>>> type(dict)
<class 'dict'>
```

### 数据结构

| 方法              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。        |
| list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。 |
| list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。 |
| list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
| list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） |
| list.clear()      | 移除列表中的所有项，等于del a[:]。                           |
| list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。 |
| list.count(x)     | 返回 x 在列表中出现的次数。                                  |
| list.sort()       | 对列表中的元素进行排序。                                     |
| list.reverse()    | 倒排列表中的元素。                                           |
| list.copy()       | 返回列表的浅复制，等于a[:]。                                 |

```python
>>> list = [1,2,3,'william',3.7]
>>> list.append(117)
>>> list
[1, 2, 3, 'william', 3.7, 117]

>>> list.insert(0,"mengxun")	# 指定位置插入元素
>>> list
['mengxun', 1, 2, 3, 'william', 3.7, 117]

>>> list = ['mengxun', 1, 2, 3, 'william', 3.7, 1, 117]
>>> list.remove(1)				# 删除列表中值为1的第一个元素
>>> list
['mengxun', 2, 3, 'william', 3.7, 1, 117]

>>> list.pop(-2)				# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素
>>> list
1
>>> list.pop()
117
>>> list
['mengxun', 2, 3, 'william', 3.7]

>>> list.index('william')		# 返回列表中第一个值为 x 的元素的索引
3

>>> list.clear()				# 移除列表所有项
>>> list
[]

>>> list = [7,4,2,8,9,1,2,5,6,1,2,3,5]
>>> list.sort()					# 排序
[1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9]

>>> list.reverse()				# 倒序
>>> list
[9, 8, 7, 6, 5, 5, 4, 3, 2, 2, 2, 1, 1]

>>> list.count(1)				# 统计列表元素
2
```

将列表用做堆栈（后进先出）

```python
>>> stack = [3,4,5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3,4,5,6,7]
>>> stack.pop()
7
>>> stack
[3,4,5,6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3,4]
```

将列表用作队列（先进先出）

```python
>>> from collections import deque
>>> queue = deque(["Eric","John","Michael"])
>>> queue.append("Terry")
>>> queue.append("Graham")
>>> queue.popleft()
'Eric'
>>> queue.popleft()
'John'
>>> queue
deque(['Michael', 'Terry', 'Graham'])
```

列表推导式

列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

```python
>>> vec = [2,4,6]
>>> [3*x for x in vec]
[6, 12, 18]

>>> [[x, x**2] for x in vec]
[[2,4],[4,16],[6,36]]

>>> freshfruit = ['	banana','	loganberry ','passion fruit ']
>>> [weapon.strip() for weapon in freshfruit]	# strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
['banana', 'loganberry', 'passion fruit']

# 使用if过滤
>>> vec = [2,4,6]
>>> [3*x for x in vec if x > 3]
[12,18]
>>> [3*x for i in vec if x < 2]
[]

# 循环的技巧
>>> vec1 = [2,4,6]
>>> vec2 = [4,3,-9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8,12,-54]

>>> [str(round(355/113, i)) for i in range(1,6)]	# round() 方法返回浮点数x的四舍五入值,i表示从小数点位数
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

嵌套列表解析

```python
# 方法一
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 方法二
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 方法三
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

del 语句

使用del语句可以从一个列表中依索引而不是值来删除一个元素。这与使用pop()返回一个值不同。可以用del语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
[]

# 删除实体变量
>>> del a
```

元组和序列

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> u = t, (1,2,3,4,5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

集合

集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> basket
{'banana', 'orange', 'pear', 'apple'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False

>>> a = set('asdbasdasqweg')
>>> b = set('afagada')
>>> a
{'g', 's', 'w', 'a', 'e', 'q', 'b', 'd'}
>>> b
{'f', 'g', 'd', 'a'}
>>> a - b				# 在 a 中有的字母，但不在 b 中
{'s', 'w', 'e', 'b', 'q'}
>>> a | b				# 在 a 和 b 中的字母
{'g', 's', 'f', 'w', 'a', 'e', 'q', 'b', 'd'}
>>> a & b				# a 和 b 都有的字母
{'g', 'a', 'd'}
>>> a ^ b				# 在 a 或 b 中的字母，但不同时在a和b中
{'s', 'f', 'w', 'e', 'q', 'b'}

# 集合推导式
>>> a = {x for x in 'adcrtadsac' if x not in 'adc'}
{'s', 't', 'r'}
```

字典

同时遍历两个或更多的序列，可以使用 zip() 组合

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

反向遍历序列

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1        
```

要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

### 函数

不定长参数。一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

```python
>>> def printinfo(arg1,*vartuple):
...     print(arg1)
...     print(vartuple)
...
>>> printinfo(70,60,50)
70
(60, 50)

# 但没有指定参数，则为空元组
>>> def printinfo(arg1, *vartuple):
...     print(arg1)
...     for var in vartuple:
...         print(var)
...     return
...
>>> printinfo(10)
10
>>> printinfo(70,60,50)
70
60
50
```

加了两个星号 ***\*** 的参数会以字典的形式导入

```python
>>> def printinfo(arg1, **vardict):
...     print(arg1)
...     print(vardict)
...
>>> printinfo(1,a=2,b=3)
1
{'a': 2, 'b': 3}
```

匿名函数

`lambda [arg1 [,arg2,.....argn]]:expression`

```python
>>> sum = lambda arg1, arg2: arg1 + arg2
>>> print(sum(10,20))
30
```

