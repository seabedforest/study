"""
参照demo01,完成员工管理器的迭代
"""


class NextItem:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        self.index += 1
        try:
            return self.data[self.index]
        except IndexError:
            raise StopIteration


class EmployeeManager:

    def __init__(self):
        self.list_employees = []

    def add_employee(self, emp):
        self.list_employees.append(emp)

    def __iter__(self):
        return NextItem(self.list_employees)


manager = EmployeeManager()
manager.add_employee("程序员")
manager.add_employee("测试员")
manager.add_employee("销售")

for item in manager:
    print(item)

# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
#
# print(manager.list_employees)