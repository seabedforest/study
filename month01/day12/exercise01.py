"""
小明请保洁打扫卫生
"""


class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, household_service):
        print(self.name, "通知")
        household_service.cleaning()


class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)