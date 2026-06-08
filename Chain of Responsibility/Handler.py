

class Logger:

    def __init__(self,level):
        self.level = level
        self.next_logger = None

    def setNextLogger(self,next_logger):
        self.next_logger = next_logger

    def log(self,level,message):
        if self.level<=level:
           self.write(message)
        if self.next_logger:
            self.next_logger.log(level,message)
        
    
    def write(self,message):
        pass


