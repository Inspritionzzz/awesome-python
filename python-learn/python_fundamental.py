import sys
from collections import namedtuple, deque, OrderedDict, defaultdict, Counter
from math import sin as sin
from math import cos as cos
import random as rd
import numpy as np
import mytoolkits.parameters as PI
# from mytoolkits.parameters import PI

def builinFunction():
    # 查看python内置函数
    dir(__builtins__)
    help(type)


def operator():
    # 运算符
    print(1 + 1)  # 2
    print(2 - 1)  # 1
    print(3 * 4)  # 12
    print(3 / 4)  # 0.75
    print(3 // 4)  # 0
    print(20220202 // 10000 == 2022)
    print(3 % 4)  # 3
    print(2 ** 3)  # 8

    # 比较运算符
    print(2 > 1)  # True
    print(2 >= 4)  # False
    print(1 < 2)  # True
    print(5 <= 2)  # False
    print(3 == 4)  # False
    print(3 != 5)  # True

    # 逻辑运算符
    print((3 > 2) and (3 < 5))  # True
    print((1 > 3) or (9 < 2))  # False
    print(not (2 > 1))  # False

    # 位运算符
    print(bin(4))  # 0b100
    print(bin(5))  # 0b101
    print(bin(~4), ~4)  # -0b101 -5
    print(bin(4 & 5), 4 & 5)  # 0b100 4
    print(bin(4 | 5), 4 | 5)  # 0b101 5
    print(bin(4 ^ 5), 4 ^ 5)  # 0b1 1
    print(bin(4 << 2), 4 << 2)  # 0b10000 16
    print(bin(4 >> 2), 4 >> 2)  # 0b1 1

    # 三元运算符
    x, y = 4, 5
    small = x if x < y else y
    print(small)  # 4

    # 其他运算符
    letters = ['A', 'B', 'C']
    if 'A' in letters:
        print('A' + ' exists')
    if 'h' not in letters:
        print('h' + ' not exists')
    # A exists
    # h not exists

    a = "hello"
    b = "hello"
    print(a is b, a == b)  # True True
    print(a is not b, a != b)  # False False

    # 运算符优先级
    print(-3 ** 2)  # -9
    print(3 ** -2)  # 0.1111111111111111
    print(1 << 3 + 2 & 7)  # 0
    print(-3 * 2 + 5 / -2 - 4)  # -12.5
    print(3 < 4 and 4 < 5)  # True

    pass


def variables():
    teacher = "jason"
    print(teacher)  # jason

    first = 2
    second = 3
    third = first + second
    print(third)  # 5

    myTeacher = "jason"
    yourTeacher = "jason2"
    ourTeacher = myTeacher + ',' + yourTeacher
    print(ourTeacher)  # jason,jason2

    set_1 = {"welcome", "study", "Python"}
    print(set_1.pop())
    pass


def dataType():
    # Number: int float complex
    x = 1
    y = 1.0
    print(type(x))
    a1 = b1 = c1 = 2
    print(a1, b1, c1)
    a2, b2, c2 = 3, 3.1, 3 + 10j
    print(a2, b2, c2)
    print(type(a2), type(b2), type(c2))

    # Boolean
    print(True + 1)  # 可视为int
    print(False)
    print(not False)

    # String
    str1 = 'just\ta\ttest'
    print(str1, type(str1))
    print(str1 + '\ttest\t', 'test' * 3)
    print(len(str1))
    print(str1[0], str1[-1])
    print(dir(str))
    print(help(str.split))
    print(str1.split("\t"))
    print(str1.title())
    print("{} {}".format("hello", "python"))
    print("{0} {1} {0}".format("hello", "python"))
    print("{:.2f}".format(3.1415926))
    print("{:+.2f}".format(3.1415926))
    print("{:.0f}".format(3.1415926))

    # List
    list1 = []
    print(type(list1))
    list1 = ['abc', 'math', 10]
    print(list1, list1[-1], list1[-2])
    list1[0] = 'def'  # 修改列表数据
    print(list1[0])
    print(list1[0:5], list1[:2], list1[1:], list1[:])  # 左闭右开[0:5)

    list2 = [2, 'cn', [1, 2, 3]]  # 嵌套列表
    print(list2)

    list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list3[0:9:2])
    print(list3[::-1])
    print(list3 + list1)
    print(list3 * 3)

    list4 = list('just a test')
    print(list4)

    list5 = ['aa', 'bb', 'cc', 'dd', 'ee']
    list5.append('ff')
    print(id(list5))  # 内存地址不会因为上述操作而改变
    list5.insert(2, 'gg')
    print(id(list5))
    list5.extend(list3)
    print(list5)
    print(id(list5))

    list5.pop()
    print(list5)
    list5.pop(2)
    print(list5)
    print(list5.remove('cc'))  # 删除列表中第一个值为cc的元素
    print(list5)
    del list5[1]
    print(list5)
    list5.clear()

    list6 = ['aaa', 'bbb', 'ccc', 'ddd', 'bbb']
    print(list6.count('bbb'))
    print(list6.index('bbb'))  # 首次出现的位置
    print('ccc' in list6)
    print('ddd' not in list6)

    list7 = ['AA', 'cc', 'BB', 'CC']
    print(list7)
    list7.sort()
    print(list7)
    list7.reverse()
    print(list7)
    list7.sort(key=None, reverse=False)
    print(list7)
    sorted(list7, reverse=True)  # 使用全局函数
    print(list7)  # 使用sort()会改变列表本身,内置函数在原始列表复制一个副本,在副本上进行排序操作

    print(dir(list))
    list8 = ['AA', 'BB', 'CC', 'DD']
    print(list(zip(list8, range(len(list8)))))
    print(enumerate(list8))  # 枚举对象不能直接输出
    print(list(enumerate(list8)))  # 添加序号并枚举列表
    print(list(enumerate(list8, start=1)))

    # Tuple
    tup1 = ()
    print(type(tup1))
    tup2 = (100,)
    tup3 = (100)
    print(type(tup2), type(tup3))
    tup4 = 'a', 'b', 2
    print(type(tup4))
    print(tup4[:1])
    print(tup2 + tup4)
    alist = [11, 22, 33]
    atuple = tuple(alist)
    print(atuple)
    newtuple = tuple('just a test')
    print(newtuple)
    print(id(newtuple))
    newtuple = newtuple[:1] + ('just',) + newtuple[1:]  # 元组不可更改,这里采用拼接的方式创建新的元组
    print(id(newtuple))

    # Dictionary
    dict1 = {'a': 1, '2022': [1, 2, 3], 100: ('just', 'a', 'test')}
    print(dict1)
    print(dict1.items())  # 获取字典中的所有键/值对元素,并封装在元组中
    print(dict1.keys())
    print(dict1.values())
    print(dict1[100])  # 看起来像数组的索引值,其实是字典里的一个键
    print(dict1.get('a'))
    print(dict1.get('a', '此元素不存在'))
    dict1['a'] = 2  # 修改元素
    dict1['2023'] = 3
    print(dict1)
    dict2 = {'zhao': 33, 'a': 4}
    dict1.update(dict2)  # 将一个字典整体更新另一个字典
    print(dict1)
    print(dict2.pop('a'))  # 指名道姓的删除
    print(dict2.popitem())

    # Set
    a = {3, 3, 4, 5}
    print(type(a), a)
    list1 = [1, 3, 3, 5, 7]
    print(set(list1))
    a_set = set([8, 9, 10, 11])
    b_set = {10, 11, 12, 13}
    print(a_set | b_set)
    print(a_set & b_set)
    print(a_set - b_set)
    print(a_set ^ b_set)
    print(a_set.symmetric_difference(b_set))
    pass

def Structured():

    flag = False
    if flag:
        print('test if')
    else:
        print('test if else')

    score = 90
    if 90 <= score <= 100:
        print('A')
    elif 80 <= score <= 89:
        print('B')
    else:
        print('C')

    a_dict = {}
    if not a_dict:
        print('空字典')  # 非空即为真,None为False

    x = 10
    y = 20
    small = x if x < y else y
    print(small)

    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    for mylist in list1:
        temp = mylist * 2
        print(temp)

    sum = 0
    for x in range(101):  # range(start, stop[, step])
        sum = sum + x
    print(sum)

    seq = ['a', 'b', 'c', 'd']
    for index, key in enumerate(seq):
        print('seq [{0}] = {1}'.format(index, key))

    # while
    numbers = [23, 43, 56, 64, 76]
    even = []
    odd = []
    # even, odd = [], []
    while len(numbers) > 0:
        num2 = numbers.pop()
        if num2 % 2 == 0:
            even.append(num2)
        else:
            odd.append(num2)
    print("Even", even)
    print("Odd", odd)

    n = 1
    nums = []
    while n < 100:
        n = n + 1
        if n > 50:
            break
        if n % 2 == 0:
            nums.append(n)
    print(nums)

    # 推导式
    # 列表推导式
    a_list = [1, '4', 9, 'a', 0, 'bc']
    squared_ints = [e**2 for e in a_list if type(e) == int]
    print(squared_ints)

    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flag_vec = [num for elem in vec for num in elem]
    print(flag_vec)

    new_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(new_list)

    # 上面代码等价于
    new_list = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y :
                new_list.append((x, y))
    print(new_list)
    # 字典推导式
    mcase = {'a': 10, 'b': 30, 'c': 50}
    kv_exchange = {v : k for k, v in mcase.items()}
    print(kv_exchange)
    # 集合推导式
    squared = {x**2 for x in [1, 1, 2, -2, 3]}
    print(squared)

    pass

def buildinFunction():
    # 1. 使用自定义模块
    sin(0.4)
    x = rd.random()
    print("x = ", x)
    a = np.array((1, 2, 3, 4, 5))
    print(a)
    PI.printPI()
    print("PI.PI ", PI.PI)

    # 2. 查看系统扫描模块路径
    print(sys.path)
    home_dir = 'D:\\DevelopmentEnvironment'
    sys.path.append(home_dir)
    print(sys.path)
    # %run parameters.py

    # 3. Collections
    # namedtuple: 创建特殊的类, 属于元组
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(p.x, p.y, isinstance(p, Point), isinstance(p, tuple), p[0], p[1])
    a, b = p
    print(a, b)
    # deque: 实现高效插入和删除操作的数据类型, 解决列表插入和删除慢的问题(线性存储)
    dq = deque(['a', 'b', 'c'])
    dq.append(1)
    print(dq)
    dq.appendleft(2)
    print(dq)
    dq.insert(2, 'x')
    print(dq)
    dq.pop()
    print(dq)
    dq.popleft()
    print(dq)
    dq.remove('x')
    print(dq)
    dq.reverse()
    print(dq)
    # OrderedDict: 有序字典
    od = OrderedDict()
    od["a"] = 1
    od["b"] = 2
    od["c"] = 3
    print(od)
    keys = ["aa", "bb", "cc"]
    value = [4, 5, 6]
    od.update(zip(keys, value))
    print(od)
    print(od.pop('a'))
    od.move_to_end('b')
    print(od)
    # defaultdict: 键值不存在时返回一个默认值
    dd = defaultdict(lambda: 'N/A') # 要早于字典的创建
    dd['key1'] = 'abc'
    print(dd['key1'], dd['key2'])
    # Counter
    colors = ['aa', 'aa', 'dd', 'dd', 'ee','ff', 'aa']
    result = {}
    # 使用for统计颜色数量
    for color in colors:
        if result.get(color) == None:
            result[color] = 1
        else:
            result[color] += 1
    print(result)
    # 使用Counter统计
    result2 = Counter(colors)
    print(dict(result))
    print(result2.most_common(2))  # 频次前二, 返回列表对象
    print(result2.most_common(2)[1][1])  #

    # 4. datatime

    pass


def Function():


    pass


# 在本文件中__name__就是__main__
# 在外部执行本文件,__name__就是python文件名(不包含.py)
if __name__ == '__main__':

    # 运算符
    # operator()

    # 变量
    # variables()

    # 数据类型:Number Boolean String List Tuple Dictionary Set
    # dataType()

    # 程序结构
    # Structured()

    # python标准库和内置模块
    buildinFunction()


    # python函数

    # Function()

    # python高级特性
