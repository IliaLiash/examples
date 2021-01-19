class Clock:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s-1
        
    def __next__(self):
        self.s += 1
        if self.s > 59:
            self.s = 0
            self.m += 1
        if self.m > 59:
            self.m = 0
            self.h += 1
        if self.h > 23:
            self.h = 0 
                
        return '{0:0=2d}'.format(self.h) + ':' + '{0:0=2d}'.format(self.m) + ':' + '{0:0=2d}'.format(self.s)
        
    def __iter__(self):
        return self