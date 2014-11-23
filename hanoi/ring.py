class Ring(object):
    
    def __init__(self, ringSize):
        self.ringSize = ringSize;
        self.column = 0;
        
    def move(self, column):
        self.column = column;
        
    
        