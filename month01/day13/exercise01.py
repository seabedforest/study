class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return "员工名称:%s,员工编号:%d,部门编号:%d,工资:%d" % (self.name, self.eid, self.did, self.money)


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title

    def __str__(self):
        return "部门编号:%d,部门名称:%s" % (self.did, self.title)


class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    def __str__(self):
        return "技能名称:%s,攻速:%s,消耗法力%d,持续时间%d" % (self.name, self.atk_rate, self.cost_sp, self.duration)


e01 = Employee(1001, 9002, "师父", 60000)
print(e01)

d01 = Department(9001, "教学部")
print(d01)

s01 = Skill("乾坤大挪移", 1, -10)
print(s01)
