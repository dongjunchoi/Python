from pywin.docking.DockingBar import PtInRect
class Animal:
# __init__ : 생성자
    def __init__(self):
        self.age = 0
        self.egg = False
    def getOld(self):
        self.age += 1
    def changEgg(self):
        self.egg = not self.egg

class Hunman(Animal):
    def __init__(self):
#         super().__init__()
        Animal.__init__(self)
        self.moneypower = 11
    def makemoney(self, earnmoney):
        self.moneypower += earnmoney
        
# a = Animal()
a = Hunman()
print(a.age)
print(a.egg)
print(a.moneypower)

a.getOld()
a.changEgg()
a.makemoney(100)

print(a.age)
print(a.egg)
print(a.moneypower)
    