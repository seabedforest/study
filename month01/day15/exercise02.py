class Person:

    def __init__(self,nickname,sex,hp,ad):
        self.nickname = nickname
        self.sex = sex
        self.hp = hp
        self.ad = ad

    def attack(self,p1):
        p1.hp -= self.ad
        print('%s攻击了%s,%s还剩%s血量'%(self.nickname,p1.nickname,p1.nickname,p1.hp))

    def weapon_attack(self,wea):
        # 武器类的对象封装到人的对象中当做一个属性.就叫做组合.
        self.weapon = wea

class Weapon:

    def __init__(self,name,att):
        self.name = name
        self.att = att

    def Aux_attack(self,p,p1):
        p1.hp -= self.att
        print('%s利用%s打了%s%s滴血,%s还剩%s滴血' %(p.nickname,self.name,p1.nickname,self.att,p1.nickname,p1.hp))


alex = Person('alex','男',100,20)
barry = Person('太白','男',200,50)
axe = Weapon('斧子',30)
barry.weapon_attack(axe)
barry.weapon.Aux_attack(barry,alex)

axe.Aux_attack(alex,barry)
alex.attack(barry)
alex.attack(barry)