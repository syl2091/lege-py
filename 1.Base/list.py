item1 = [35, 12, 99, 68]
item2 = ['Python', 'Java', 'Go', 'Kotlin']

print(item1)
print(item2)

item1 = list(range(1, 10))

print(item1)
item2 = list('hello')
print(item2)

# 列表拼接
items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

item3 = items1 + items2
print(item3)

# 列表得重复
item4 = ['hello'] * 3
print(item4)

# 列表成员运算
print(100 in item3)
print('hello' in item4)

# 获取列表的长度(元素个数)
size = len(item3)
print(size)
# 列表索引
print(item3[0], item3[-size])
item3[-1] = 100
print(item3[size - 1], item3[-1])

# 列表的切片
print(item3)
print(item3[:5])
print(item3[4:])
print(item3[-5:-7:-1])
print(item3[::-2])

# 列表的比较运算
item5 = [1, 2, 3, 4]
item6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(item5 == item6)
item7 = [2, 1, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(item5 <= item7)

# 列表元素遍历
items = ['Python', 'Java', 'Go', 'Kotlin']

for index in range(len(items)):
    print(items[index])

for index in items:
    print(index)

# 列表的方法
items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)  # ['Python', 'Java', 'Go', 'Kotlin', 'Swift']
# 使用insert方法在列表指定索引位置插入元素
items.insert(2, 'SQL')
print(items)  # ['Python', 'Java', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定的元素
items.remove('Java')
print(items)  # ['Python', 'SQL', 'Go', 'Kotlin', 'Swift']
# 删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)
print(items)  # ['SQL', 'Go', 'Kotlin']

# 清空列表中的元素
items.clear()
print(items)  # []

items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素的索引位置
print(items.index('Python'))  # 0
print(items.index('Python', 2))  # 5
# 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的
# print(items.index('Java', 3))      # ValueError: 'Java' is not in list


items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素出现的次数
print(items.count('Python'))  # 2
print(items.count('Go'))  # 1
print(items.count('Swfit'))  # 0

items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']

# 排序
items.sort()
print(items)  # ['Go', 'Java', 'Kotlin', 'Python', 'Python']
# 反转
items.reverse()
print(items)  # ['Python', 'Python', 'Kotlin', 'Java', 'Go']

# 列表的生成
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

items2 = []

for x in 'hello world':
    if x not in 'aeiou':
        items2.append(x)
print(items2)

items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x+y)
print(item3)

# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


#嵌套列表
scores = [[0]*3]*5
print(scores)
#scores[0][0]=95
#print(scores)

scores = [[0*3]*3 for x in range(5)]
scores[0][0]=95
print(scores)