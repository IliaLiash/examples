'''
Реализуйте класс "Нейрон", у которого будет несколько методов: 
'''

class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None
        
    def forward(self, x):
        self.x = x
        total = 0
        for i in range(len(w)):
            total += x[i] * w[i]
            
        return self.f(total) 

    def backlog(self):
        return self.x
