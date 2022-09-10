from re import M


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
    def __init__(self,mileage,cost,tyre,hp):
        
        super().__init__(mileage,cost)#here we inherit this from parent class by super() method
        self.tyre=tyre
        self.hp=hp
    
    def car_det(self):
       print("Tyre",self.tyre)
       print("Hp",self.hp)
       print("I AM A CAR")

c1=Car(50,456,4,50)
c1.veh_det() 
c1.car_det()  
    