# our class Ship
class Ship:
    def __init__(self, name, country):
        self.name = name
        self.cargo = 0
        

    # the old sail method that you need to rewrite
    def sail(self, country):
        self.country = country
        print("The {0} has sailed for {1}!".format(self.name, self.country))



black_pearl = Ship("Black Pearl", 800)
black_pearl.sail(input())