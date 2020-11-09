class Car():
    
    """Простая модель автомобиля."""
    
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        #получает make, model, year и сохраняет их в атрибутах,
        #которые будут связаны с экземплярами, созданными на основе класса.
        #При создании нового экземпляра Car необходимо указать фирму-производителя, модель и год выпуска
        #для данного экземпляра.
        self.make = make
        self.model = model
        self.year = year
        #добавим пробег
        self.odometer = 0
        
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer) + " miles on it.")    
        
    def update_odo(self, mileage):
        self.odometer += int(mileage)

#создаем экземпляр класса
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#изменение значения атрибута
my_new_car.odometer = 23
my_new_car.read_odometer()

#добавляем пробег
print("\n---Update Odometer---")
my_new_car.update_odo(150)
my_new_car.read_odometer() #23 + 150 = 173

#НАСЛЕДОВАНИЕ
class ElectricCar(Car):
    
    """Представляет аспекты машины, специфические для электромобилей."""
    
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery_size = 70	
        #Эта строка приказывает Python вызвать метод
        #__init__() класса, являющегося родителем ElectricCar (Car), в результате чего экземпляр
        #ElectricCar получает все атрибуты класса-родителя. Имя super происходит
        #из распространенной терминологии: класс-родитель называется суперклассом,
        #а класс-потомок — субклассом.	
	
my_tesla = ElectricCar('tesla', 'model s', 2016)    #создаем экземпляр
print(my_tesla.get_descriptive_name())
print("Battery size:", str(my_tesla.battery_size) + " kWh battery")