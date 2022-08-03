
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
    print(True + 1) # 可视为int
    print(False)
    print(not False)

    # String
    str1 = 'just\ta\ttest'
    print(str1, type(str1))
    print(str1+'\ttest\t', 'test'*3)
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
    # Dictionary
    # Set

    pass


if __name__ == '__main__':
    # 内置函数
    # builinFunction()

    # 运算符
    # operator()

    # 变量
    # variables()

    # 数据类型
    dataType()

    

