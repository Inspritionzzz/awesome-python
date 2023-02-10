from typing import List


def f1():
        author = 'jason'
        print('legend, {}'.format(author))

        student, teacher = 'Tom', 'Jason'
        student, teacher = teacher, student

        print(student)
        pass

# 使用类型注解
def remove_element(items : List[int]):
        pass

if __name__ == '__main__':
        f1()
