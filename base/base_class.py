
''' 
类和对象
'''

# __ 开头的属性是私有属性， 不能直接访问， 需要通过方法访问
# _ 开头的属性是受保护的属性， 可以被继承的子类访问， 但是不能被外部访问
# 以上2种是命名惯例， 不是语法规则, 遵守这个惯例， 可以提高代码的可读性

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 实例方法， 允许传入 self 参数， 需要实例化， person.get_name()就可以调用
    @property
    def name(self):
        return self._name

    # 实例方法， 允许传入 self 参数， 需要实例化， person.get_age()就可以调用
    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    # 实例方法， 允许传入 self 参数， 需要实例化， person.study()就可以调用
    def study(self, subject):
        print(f"{self._name} is studying {subject}.")

    def sleep(self):
        print(f"{self._name} is sleeping.")


    # 静态方法， 不允许传入 self 参数, 不需要实例化， Person.say_hello()就可以调用
    @staticmethod
    def say_hello():
        print(f"Hello")


    # 类方法， 允许传入 cls 参数， 不需要实例化， Person.create_person()就可以调用
    @classmethod
    def create_person(cls):
        return cls("张三", 20)


# 继承 比如学生和人的关系、手机和电子产品的关系都属于继承关系, 这里Student继承了Person类，并且重写了父类的方法（多态）
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id

    def go_class(self):
        print(f"{self._name} is going to class. student_id: {self._student_id}")

    def say_hello(self):
        print(f"Hello, my name is {self._name}, my age is {self._age}, my student_id is {self._student_id}")

    

# 关联 比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。


# 依赖 比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系