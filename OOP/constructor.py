class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def emp_det(self):
        print("Name",self.name)
        print("Age",self.age)
e1 = Emp('Sam','32')
e1.emp_det()

