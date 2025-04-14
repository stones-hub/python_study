
from base.base_class import Person, Student

def main():
    person = Person("张三", 20)

    print(person.age)
    print(person.name)
    person.name = "李四"
    print(person.age)
    print(person.name)
    Person.say_hello()

    print("--------------------------------")

    student = Student("李四", 20, "123456")
    student.go_class()
    student.study("数学")
    student.say_hello()

    # sp = student.create_person()
    # sp.sleep() # 调用父类的方法报错，因为子类调用create_person()返回的是子类实例



if __name__ == "__main__":
    main()


