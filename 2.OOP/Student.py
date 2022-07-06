class student:

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print(f'学生正在玩')

    @property
    def name(self):
        return self.name

    def name(self,name):
        self.name=name




# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = student('乐哥', 40)
stu2 = student('王大锤', 15)
stu1.study('Python程序设计')    # 乐哥正在学习Python程序设计.
stu2.play()   # 王大锤正在玩游戏

stu1.sex  = '男'
print(stu1.sex)



