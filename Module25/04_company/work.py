class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def get_salary(self):
        return 'Employee salary'


class Manager(Employee):
    __fix_salary = 13000

    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)

    def get_salary(self):
        return self.__fix_salary


class Agent(Employee):
    __fix_salary = 5000
    __percent = 0.05

    def __init__(self, name: str, surname: str, age: int, total_sold: float):
        super().__init__(name, surname, age)
        self.__total_sold = total_sold

    def get_salary(self):
        return self.__fix_salary + self.__total_sold * self.__percent


class Worker(Employee):
    pass
