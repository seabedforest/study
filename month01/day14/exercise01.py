"""
定义员工管理器
1. 记录所有员工
2. 计算员工总工资
    程序员：底薪 + 项目分红
    测试员:底薪 + bug数 × 5元
    增加新岗位:
    销售:底薪 + 销售额 * 5%
写出体现的面向对象特征与原则
三大特征
    封装:
    继承:
    多态:
六大原则
    开闭原则:
    单一职责:
    依赖倒置:
    组合复用:
"""


class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, target):
        self.employee_list.append(target)

    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.employee_list:
            total_salary += emp.get_total_salary()
        return total_salary


class Employee:
    def get_total_salary(self):
        pass


class Programmer(Employee):

    def __init__(self, salary=0, project_bonus=0):
        self.salary = salary
        self.project_bonus = project_bonus

    def get_total_salary(self):
        return self.salary + self.project_bonus


class Tester(Employee):

    def __init__(self, salary=0, bug_count=0):
        self.salary = salary
        self.bonus = bug_count * 5

    def get_total_salary(self):
        return self.salary + self.bonus


manager = EmployeeManager()
manager.add_employee(Programmer(10000, 100000))
manager.add_employee(Tester(8000, 100))
print(manager.calculate_total_salary())
