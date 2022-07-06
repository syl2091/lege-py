# 函数的高级应用

import random
import time





#download('MySQL从删库到跑路.avi')
#upload('Python从入门到住院.pdf')


# 定义装饰器函数，它的参数是被装饰的函数或类
from functools import wraps


def record_time(func):
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result

    # 返回带装饰功能的wrapper函数
    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}')
    time.sleep(random.randint(2, 6))
    print(f'下载完成{filename}')


@record_time
def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.randint(4, 8))
    print(f'上传完成{filename}')

#download('MySQL从删库到跑路.avi')
#upload('Python从入门到住院.pdf')
# 取消装饰器
#download.__wrapped__('MySQL必知必会.pdf')
#upload = upload.__wrapped__
#upload('Python从新手到大师.pdf')


#递归
def fib(n):
    if n in (1,2):
        return 1
    return fib(n-1)+fib(n-2)

for i in range(1,20):
    print(fib(i))


