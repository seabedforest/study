class Employee:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __eq__(self, other):
        return self.eid == other.eid or self.did == other.did

    def __lt__(self, other):
        return self.money < other.money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
# 根据员工编号
print(list_employees.index(Employee(1001)))
# 根据部门编号
print(list_employees.count(Employee(did=9002)))
# 查找工资最少的员工
min_value = min(list_employees)  # Employee(1005, 9001, "小白龙", 15000)
print(min_value.__dict__)
# 根据工资排序
list_employees.sort()
for employee in list_employees:
    print(employee.__dict__)
