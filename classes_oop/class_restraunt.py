class Restraunt():
    
    def __init__(self, restraunt_name, cuisine_type):
        #когда вызываем конструктор - указываем в скобках, какие аргументы нужно передать при создании экземпляра класса
        #и с помощью self записываем их в атрибуты name, cuisine 
        self.name = restraunt_name
        self.cuisine = cuisine_type
        
    def describe_restraunt(self):
        #работает с self.name, self.cuisine внутри класса
        print('Restraunt: ' + self.name + ', Cuisine: ' + self.cuisine)
        
    def open_restraunt(self):
        print(self.name + ' is open now')
        
#создаем экземпляр класса, передавая требуемые аргументы для конструктора
rest_palma = Restraunt('Palma', 'Meat')
rest_swiss = Restraunt('Swiss', 'Meat')
rest_halav = Restraunt('Tevie', 'Milk')

print('Name of restraunt: ' + rest_palma.name)
print('Type of Cuisine: ' + rest_palma.cuisine)
print('Name of restraunt: ' + rest_swiss.name)
print('Type of Cuisine: ' + rest_swiss.cuisine)
print('Name of restraunt: ' + rest_halav.name)
print('Type of Cuisine: ' + rest_halav.cuisine)
print()

rest_palma.describe_restraunt()
rest_swiss.describe_restraunt()
rest_halav.describe_restraunt()

print()

rest_palma.open_restraunt()
rest_swiss.open_restraunt()
rest_halav.open_restraunt()