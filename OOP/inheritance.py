class vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def veh_det(self):
        print("mileage is ",self.mileage)
        print("cost",self.cost)
v1=vehicle(5000,12000)
v1.veh_det()
#above is superclass
#now child class

class Car(vehicle):
    def car_det(self):
       print("I AM A CAR")
c1=Car(50,456)
c1.veh_det()   
    