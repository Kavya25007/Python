class Car:
    @staticmethod
    def Start():
        print("Car started.....")

    @staticmethod
    def Stop():
        print("Car stoped.....")

class Toyotacar(Car):
    def __init__(self, modelname ):
        self.modelname = modelname

car1= Toyotacar("Fortuner")
print(car1.modelname)

car2= Toyotacar("Innova")
print(car2.modelname)

print(car1.Start())
print(car2.Stop())
