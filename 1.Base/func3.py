import operator

#关键字函数

def is_triangle(a,b,c):
    print(f'a={a},b={b},c={c}')
    return a+b>c and b+c>a and a+c>b

print(is_triangle(1,2,3))
print(is_triangle(c=1,b=2,a=3))

def calc(*args,**kargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    return result

print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc())     # 6
print(calc(1, 2, c=3, d=4))    # 10


# 高阶函数
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            result = op(result, arg)
    for value in kwargs.values():
        if type(value) in (int, float):
            result = op(result, value)
    return result

def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))    # 120


def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]

#Lambda函数
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]


