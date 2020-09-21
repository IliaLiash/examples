class LoggableList(Loggable, list): 
    
    def append(self, element):
        super(LoggableList, self).append(element)        
        return self.log(element)
#a идет на место self
#a = LoggableList()
#a.append('msg 1')
#a.append('msg 2')
