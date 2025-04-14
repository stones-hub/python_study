'''
类与类之间的关联关系
'''


# 关联关系示例
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(f"部门 {self.dept_name} 的员工: {employee.name}")


# 创建员工和部门实例
employee1 = Employee("张三")
employee2 = Employee("李四")
dept = Department("技术部")

# 将员工添加到部门
dept.add_employee(employee1)
dept.add_employee(employee2)

# 显示部门员工
dept.show_employees()


# 聚合关系示例
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} 引擎启动")


class Car:
    def __init__(self, car_model, engine):
        self.car_model = car_model
        self.engine = engine

    def start_car(self):
        print(f"启动 {self.car_model} 汽车")
        self.engine.start()


# 创建引擎和汽车实例
engine = Engine("汽油发动机")
car = Car("宝马 X5", engine)

# 启动汽车
car.start_car()


# 合成关系示例
class Room:
    def __init__(self, room_number):
        self.room_number = room_number


class House:
    def __init__(self, house_address):
        self.house_address = house_address
        self.rooms = []

    def add_room(self, room_number):
        room = Room(room_number)
        self.rooms.append(room)

    def show_rooms(self):
        print(f"{self.house_address} 的房间:")
        for room in self.rooms:
            print(f"房间号: {room.room_number}")


# 创建房子实例并添加房间
house = House("XX 路 123 号")
house.add_room(101)
house.add_room(102)

# 显示房子的房间
house.show_rooms()
    