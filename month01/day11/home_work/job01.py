"""
4. 使用封装数据的思想
    创建员工类/部门类,修改实现下列功能.
        (1). 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (2). 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (3). 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
        (4). 定义函数,查找薪资最少的员工
        (5). 定义函数,根据薪资对员工列表升序排列

    # 员工列表
    list_employees = [
        {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
        {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
        {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
        {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
        {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
    ]

    # 部门列表
    list_departments = [
        {"did": 9001, "title": "教学部"},
        {"did": 9002, "title": "销售部"},
    ]
@author hailin
@date 2020-05-15
"""


# 创建员工类/部门类
class Employees:
    """
    员工类
    """

    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def show_employee_info(self):
        """
        打印所有员工信息
        :return:
        """
        print(f"{self.name}的员工编号是{self.eid},部门编号是{self.did},月薪{self.money}元.")


class Departments:
    """
    部门类
    """

    def __init__(self, did, title):
        self.did = did
        self.title = title


list_employees = [
    Employees(1001, 9002, "师父", 60000),
    Employees(1002, 9001, "孙悟空", 50000),
    Employees(1003, 9002, "猪八戒", 50000),
    Employees(1004, 9001, "沙僧", 30000),
    Employees(1005, 9001, "小白龙", 15000)
]

list_departments = [
    Departments(9001, "教学部"),
    Departments(9002, "销售部")
]

# (1). 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
for employee_info in list_employees:
    employee_info.show_employee_info()

# (2). 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
for employee_info in list_employees:
    if employee_info.money > 20000:
        employee_info.show_employee_info()


# (3). 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
def show_employee_department_infos():
    """
    打印所有员工的部门信息
    :return:
    """
    for employee_info in list_employees:
        for department in list_departments:
            if employee_info.did == department.did:
                print(f"{employee_info.name}的部门是{department.title},月薪{employee_info.money}元.")
                break


show_employee_department_infos()


# (4). 定义函数,查找薪资最少的员工
def find_employee_min_money():
    """
    查找薪资最少的员工
    :return:
    """
    min_money = list_employees[0]
    for index in range(1, len(list_employees)):
        if min_money.money > list_employees[index].money:
            min_money = list_employees[index]
    return min_money


find_employee_min_money().show_employee_info()


# (5). 定义函数,根据薪资对员工列表升序排列
def get_employee_money_sort_asc():
    """
    根据薪资对员工列表升序排列
    :return:
    """
    for i in range(len(list_employees) - 1):
        for j in range(i + 1, len(list_employees)):
            if list_employees[i].money > list_employees[j].money:
                list_employees[i], list_employees[j] = list_employees[j], list_employees[i]


get_employee_money_sort_asc()
for employee_info in list_employees:
    print(employee_info.__dict__)
