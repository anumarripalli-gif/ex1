
class Grandparent:
    def land(self):
        print("grandparent has a big land")


        ### deriving from grand parent
class parent(Grandparent):
    def luxary_house(self):
        print("parent has a luxary_house")

        ### deriving from parent

class child(parent):
    def  car(self):
        print("child has a car")

        ### creating objects of child class
c=child()
c.land()
c.car()
c.luxary_house()
