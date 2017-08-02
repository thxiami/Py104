# Summary
## 1 回顾练习过程

一年前接触 Python 时就从《笨方法学python》这本书开始，但是仅做了前面20个习题，之后就开始用 python 作数据处理和一些小的项目，在实际项目的过程中又学习并使用了类这个概念。所以在这次入学挑战中，跟着作者把代码敲下来这个过程整体都比较顺畅。在这次的练习过程中，会多一些思考，也发现了书中其中自己发现且稍加挖掘的地方有3个：


## 2 复盘解题过程

### 2.1 发现问题
在完成加分习题时，使用 help 看 list 的帮助文档时发现
浅拷贝(shallow copy)这个名词。关于浅拷贝和深拷贝，以前听说过但一直未探究，这次又碰到所以就想深入了解一下。
```
 copy(...)
     L.copy() -> list -- a shallow copy of L
```

### 2.2 探索问题
- 为何有浅拷贝和深拷贝？
- 二者的含义和区别，从区别入手加强对各自含义的理解

### 2.3 解决问题
查阅 Python 文档，二者只有在对复杂对象的拷贝时有差异。
> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

> A deep copy constructs a new compound object and then, **recursively**, inserts copies into it of the objects found in the original.

查阅其他人的学习笔记，然后总结出以下代码。通过看具体的代码实例，感受二者的差异（例子修改自参考文献1）：
```
Python2.7.12
>>> import copy
>>> origin = [1, 2, [3, 4]]

# origin 里边有三个元素：1， 2，[3, 4]
>>> cop1 = copy.copy(origin)
>>> cop2 = copy.deepcopy(origin)
>>> cop1 == cop2
True
>>> cop1 is cop2
False
# cop1 和 cop2 看上去相同，但已不再是同一个object

# 修改 origin 中的第 1 个元素
>>> origin[0] = "biu!"
>>> origin
["biu!", 2, [3, 4]]
>>> cop1
[1, 2, [3, 4]]
>>> cop2
[1, 2, [3, 4]]
# 可以看到, cop1 和 cop2均没有改变

# 修改 origin 中的 sub-list 中的第 1 个元素
>>> origin[2][0] = "hey!"
>>> origin
["biu!", 2, ['hey!', 4]]
>>> cop1
[1, 2, ['hey!', 4]]
>>> cop2
[1, 2, [3, 4]]
# 把 origin 内的 sub-list 改掉了一个元素，观察 cop1 和 cop2
# 浅拷贝的 cop1 发生变化
# 深拷贝的 cop2 未发生变化
```
通过以上代码及结果，可以直观感受到两种拷贝的差异。至于具体的原因，根据我查阅参考文献的理解，核心在于深拷贝是**递归**的复制对象内的元素与内存地址之间的映射关系，并将这种映射关系赋给了新创建的对象。
下面通过比对**对象和对象中元素的内存地址**，来解释二者差异的原因。
```
# 声明：id() 函数用于获取对象的内存地址。

import copy
origin = [1, 2, [3, 4]]
# 仍然是刚刚的例子
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print "id(origin)", id(origin) # 68410632
print "id(cop1)", id(cop1)     # 69279816
print "id(cop2)", id(cop2)     # 68299848
# 三者各不相同

print  "-"*20
print "id(origin[0])", id(origin[0]) # 32801912
print "id(cop1[0])", id(cop1[0])     # 32801912
print "id(cop2[0])", id(cop2[0])     # 32801912
# 三者都对应于同一个内存地址

print  "-"*20
print "id(origin[2])", id(origin[2]) # 68446280
print "id(cop1[2])", id(cop1[2])     # 68446280
print "id(cop2[2])", id(cop2[2])     # 68446344
# 可以看到，cop1 和 origin 中的 sub-list 对应同一个内存地址
# 与 cop2 的 sub-list 对应的内存地址不同
# 原因即之前官方文档提到的 cop2 中的 sub-list 是递归复制原 sub-list 中映射关系产生的新的对象

"""
通过上面的分析，我们猜想：
无论是通过 origin 还是 cop1 改变 sub-list 中的某个元素时,
改变的都是同一个内存地址对应的 sub-list 中的元素，本质是改变了 sub-list 中这个元素与内存地址的对应关系
因此存在于不同内存地址的 cop2 的 sub-list 并不会受到影响
"""

# 下面我们改变 origin 中 sub-list 中的某个元素，验证以上猜想
# 改变前先输出该元素的内存地址
print  "-"*20
print "before change, id(origin[2][0])", id(origin[2][0]) # 32801864
print "before change, id(cop1[2][0])", id(cop1[2][0])     # 32801864
print "before change, id(cop2[2][0])", id(cop2[2][0])     # 32801864
# 三者均对应同一个内存地址，此处内存存放 int 类型的 3

origin[2][0] = "hey!"
# 输出改变后的该元素的内存地址
print "after change, id(origin[2][0])", id(origin[2][0]) # 69483576
print "after change, id(cop1[2][0])", id(cop1[2][0])     # 69483576
print "after change, id(cop2[2][0])", id(cop2[2][0])     # 32801864
# origin 和 cop1 的 sub-list 中的该元素对应了新的内存地址，此处内存存放了 str 类型的 "hey"
# cop2 中该位置的元素仍对应于原内存地址

# 输出改变后的 sub-list 的内存地址
print "after change, id(origin[2])", id(origin[2]) # 68446280
print "after change, id(cop1[2])", id(cop1[2])     # 68446280
print "after change, id(cop2[2])", id(cop2[2])     # 68446344
# 改变前后, origin, cop1, cop2 中的 sub-list 对应的内存地址都没有发生变化
# 说明发生变化的只是 sub-list 内元素与内存地址的映射关系，之前的猜想正确
```
写下以上文字的过程也不断加深我对于浅拷贝和深拷贝的理解，但是表述还是有很多不是很清楚的地方，如果加上图片，在理解元素与内存地址的映射关系这部分就会直观一些。可以翻阅参考文献，会有更详细的解答。

### 3 全时长
- 探索和解决问题: 3.5h
- 写文档：2h

### 4 参考文献
- [Python documention-8.10 copy-Shallow and deep copy operations](https://docs.python.org/3.4/library/copy.html#module-copy)
- [Python中 copy, deepcopy 的区别及原因](https://iaman.actor/blog/2016/04/17/copy-in-python)
- [Python3 - Tutorial Shallow and Deep Copy](http://www.python-course.eu/python3_deep_copy.php)