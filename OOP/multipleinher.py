
class P1:
    def assign_s1(self,str1):
        self.str1=str1 
    def show_s1(self):
        return self.str1
class P2:
    def assign_s2(self,str2):
        self.str2=str2 
    def show_s1(self):
        return self.str2

class Child(P1,P2):
    def assign_s3(self,str3):
        self.str3=str3 
    def show_s3(self):
        return self.str3

my_child=Child()
my_child.assign_s1("string 1")
my_child.assign_s2("string 2")
my_child.assign_s3("string 3")
my_child.show_s1()
my_child.show_s2()
my_child.show_s3()