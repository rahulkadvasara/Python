class Vehicle:
    def general_usage(self):
        print("Transport")

class Car(Vehicle):
    def __init__(self):
        self.tyre=4
        self.isRoof=True

    def specific_usage(self):
        self.general_usage()
        print("Picnic")

class MotorCycle(Vehicle):
    def __init__(self):
        self.tyre=2
        self.isRoof=False

    def specific_usage(self):
        self.general_usage()
        print("Road trip")

c=Car()
m=MotorCycle()

c.specific_usage()
m.specific_usage()

print(isinstance(c,Car))
print(issubclass(Car,Vehicle))