class Buffer:
    
    def __init__(self):
        # конструктор без аргументов
        self.total = 0
        self.list1 = []        

    def add(self, *a):
        # добавить следующую часть последовательности
        for element in a:
            self.list1.append(element)
            if len(self.list1) == 5:
                self.total = sum(self.list1)
                self.list1 = self.list1[5:]
                print(self.total)
  
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
        if len(self.list1) < 5:
            return self.list1