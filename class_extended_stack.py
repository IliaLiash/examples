class ExtendedStack(list):
    def sum(self):
        #операция сложения
        a = self[len(self) - 1]
        self.pop()
        b = self[len(self) - 1]
        self.pop()
        
        c = (a + b)
        self.append(c)
        return self 

    def sub(self):
        a = self[len(self) - 1]
        self.pop()
        b = self[len(self) - 1]
        self.pop()
        
        c = (a - b)
        self.append(c)
        return self 

    def mul(self):
        # операция умножения
        a = self[len(self) - 1]
        self.pop()
        b = self[len(self) - 1]
        self.pop()
        
        c = (a * b)
        self.append(c)
        return self         

    def div(self):
        # операция целочисленного деления
        a = self[len(self) - 1]
        self.pop()
        b = self[len(self) - 1]
        self.pop()
        
        c = (a // b)
        self.append(c)
        return self        