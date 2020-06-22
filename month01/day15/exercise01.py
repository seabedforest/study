"""
练习:以封装思想,重构下列代码
实现打印所有学生的功能.
"""
"""
    MVC 架构
"""


class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", sex="", age=0, score=0, sid=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
        self.sid = sid  # 对信息的唯一标识


class StudentView:
    """
        # 学生视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = StudentController()
        self.secede = True
    def __display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示所有学生信息")
        print("3) 删除学生信息")
        print("4) 退出")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__show_students_info()
        elif item == "3":
            self.remove_students_info()
        elif item == "4":
            self.secede = False

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.sex = input("请输入性别:")
        stu.score = int(input("请输入成绩:"))
        self.__controller.add_student(stu)

    def __show_students_info(self):
        for stu in self.__controller.list_students:
            print(f"我是{stu.name},今年{stu.age}岁,性别为{stu.sex},学生编号为{stu.sid},成绩{stu.score}")

    def main(self):
        while self.secede:
            self.__display_menu()
            self.__select_menu()

    def remove_students_info(self):
        sid = int(input("请输入要删除学生的编号"))
        self.__controller.delete_students_info(sid)


class StudentController:
    """
        学生逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.list_students = []
        self.start_id = 1001

    def add_student(self, stu):
        stu.sid = self.start_id
        self.start_id += 1  # 学生编号自增长
        self.list_students.append(stu)

    def delete_students_info(self,sid):
        for index in range(len(self.list_students)):
            if self.list_students[index].sid == sid:
                del self.list_students[index]


# 入口
view = StudentView()
view.main()
