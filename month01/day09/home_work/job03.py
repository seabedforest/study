"""
5.
    员工列表 eid表示员工编号 did 表示部门编号
@author hailin
@date 2020-05-12
"""
dict_employees = [
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


# 定义员工信息的打印格式
def print_info_format(employee_info):
    print("%s的员工编号是%d,部门编号是%d,月薪%.2f元." % (
        employee_info["name"], employee_info["eid"], employee_info["did"], employee_info["money"]))


# （1）. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employee_infos(dict_target):
    """
    打印所有员工信息
    :param dict_target: 员工列表
    :return:
    """
    for employee_info in dict_target:
        print_info_format(employee_info)


# 调试
print_employee_infos(dict_employees)


# （2）. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_money_gt_2w(dict_target):
    """
    打印所有月薪大于2w的员工信息
    :param dict_target: 员工列表
    :return:
    """
    for employee_info in dict_target:
        if employee_info["money"] > 20000:
            print_info_format(employee_info)


# 调试
print_money_gt_2w(dict_employees)


# （3）. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
def print_employees_department(list_target, dict_target):
    """

    :param list_target: 部门列表
    :param dict_target: 员工列表
    :return:
    """
    for department in list_target:
        for employee_info in dict_target:
            if department["did"] == employee_info["did"]:
                print(f"{employee_info['name']}的部门是{department['title']},月薪{employee_info['money']}元.")


# 调试
print_employees_department(list_departments, dict_employees)


# （4）. 查找薪资最少的员工
def get_min_money(dict_target):
    """
    查找薪资最少的员工
    :param dict_target: 员工列表
    :return:
    """
    employee_info = dict_target[0]
    for i in range(1, len(dict_target)):
        if employee_info["money"] > dict_target[i]["money"]:
            employee_info = dict_target[i]
    return employee_info["name"]


print(get_min_money(dict_employees))


# （5）. 根据薪资对员工列表升序排列
def get_money_sor_asc(dict_target):
    """
    根据薪资对员工列表升序排列
    :param dict_target:员工列表
    :return:
    """
    for i in range(len(dict_target) - 1):
        for j in range(i + 1, len(dict_target)):
            if dict_target[i]["money"] < dict_target[j]["money"]:
                dict_target[i], dict_target[j] = dict_target[j], dict_target[i]


# 调试
get_money_sor_asc(dict_employees)
print(dict_employees)
