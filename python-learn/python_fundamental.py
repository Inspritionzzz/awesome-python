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

    set_1 = {"欢迎", "学习", "Python"}
    print(set_1.pop())
    pass


if __name__ == '__main__':
    # operator()
    variables()

    

