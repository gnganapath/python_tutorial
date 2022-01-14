# classes and objects

class Person:
    pass

p = Person()
p
print (p)  # <__main__.Person object at 0x000001A0794A5A80>

class Person:
    def getName(self):
        print("ganapath")

p= Person()
p.getName()  # ganapath   <<< output

class PersonDetail:
    def __init__(self, name):
        self.name = name
    def getName(self):
        print("person name"+ self.name)

#p1= PersonDetail()
#p1.getName() # Traceback (most recent call last):

p1 = PersonDetail("Hello Pongal 2022")

p1.getName()   # person nameHello Pongal 2022  <<<<< output

