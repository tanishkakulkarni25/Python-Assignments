#Create a base class Vehicle with a method move() and two sub classes car and bicycle. Override the move method in both the subclasses.
#The car should print "Driving on the road" and the bicycle should print "Pedalin gon the road".
#Demonstrate polymorphism by calling the move method()
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")
vehicles = [Car(), Bicycle()]

for v in vehicles:
    v.move()