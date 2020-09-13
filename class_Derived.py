class Base:
    
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()


class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)

'''
1) Мы создаем a = Derived() как экземпляр Derived;

2) Вызываем a.add_one(). Т.к. функция add_one() есть внутри класса Derived, то a.val == 10.

3) Мы создаем b как экземпляр класса Derived;

4) Вызываем b.add_many(3). Т.к. функции add_many() нет внутри класса Derived, мы идем в его родительский класс Base

5) В Base есть функция add_many(). При ее выполнении вызывается add_one(), которая есть и в классе Base и в классе Derived(). Т.к. b = Derived(), то именно функция add_one() из родного для b класса Derived b будет исполнена 3 раза (10 + 10 + 10)
'''