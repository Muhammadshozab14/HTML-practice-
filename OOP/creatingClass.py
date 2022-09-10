class Phone:
    def set_color(self,color):
        self.color=color
    def show_color(self):
        return self.color
    def set_cost(self,cost):
        self.cost=cost
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Calling")
    def playing_game(self):  
        print("Playing")  
p2=Phone()

p2.set_color()
p2.show_color()
p2.set_cost()
p2.show_cost()


