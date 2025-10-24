
class Grandparent:
    def land(self):
        print("grand parents has a big land")

class Parent(Grandparent):
    def house(self):
        print("parents have a house")

class child(Parent):
    def car(self):
        print("child has a car")

c=child()
c.land()
c.house()
c.car()