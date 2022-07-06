from random import randint
# 函数


def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n

    return result

#m = int(input('m= '))
#n = int(input('n= '))

#print(fac(m),fac(n))


# 定义摇色子的函数，n表示色子的个数，默认值为2
def roll_dice(n=2):
    """摇色子返回总的点数"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
#print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
#print(roll_dice(3))

#可变参数
# 用星号表达式来表示args可以接收0个或任意多个参数
def add(*args):
    total = 0
    # 可变参数可以放在for循环中取出每个参数的值
    for val in args:
        if type(val) in (int, float):
            total += val
    return total

print(add())
print(add(1,1.2))


def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


foo()  # 大家猜猜调用foo函数会输出什么