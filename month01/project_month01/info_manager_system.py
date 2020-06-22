"""
    MVC 架构

"""

from typing import List


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

    def __display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示所有学生信息")
        print("3) 删除学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            # 先写方法调用,通过快捷键生成方法.
            # alt + 回车 + 回车
            self.__display_students()
        elif item == "3":
            self.__delete_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.sex = input("请输入性别:")
        stu.score = int(input("请输入成绩:"))
        self.__controller.add_student(stu)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        # list_students
        for stu in self.__controller.list_students:
            # print("我是xx,今年xx,性别xx,成绩xx,学号xx.")
            print(f"我是{stu.name},今年{stu.age},性别{stu.sex},成绩{stu.score},学号{stu.sid}.")

    def __delete_student(self):
        sid = int(input("请输入学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")


class StudentController:
    """
        学生逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.__list_students = []  # type:List[StudentModel]
        self.__start_id = 1001

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu):
        """

        :param stu:
        :return:
        """
        stu.sid = self.__start_id
        self.__start_id += 1  # 学生编号自增长
        self.__list_students.append(stu)

    def remove_student(self, sid) -> bool:
        """

        :param sid:
        :return:
        """
        for i in range(len(self.list_students)):
            if self.list_students[i].sid == sid:
                del self.list_students[i]
                return True  # 删除成功
        return False  # 删除失败


view = StudentView()
view.main()
