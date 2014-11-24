from gameboard import Base

class KeyHandler(object):
    
    def __init__(self, board):
        self.keys = [];
        self.gameboard = board;
        
    def keyAdd(self, key):
        if len(self.keys) < 2:
            self.keys.append(key)
        if len(self.keys) == 2:    
            self.gameboard.move(self.keys[0], self.keys[1])
            while len(self.keys) > 0 :
                self.keys.pop()
    
    def keyClear(self):
        while len(self.keys) > 0:
            self.keys.pop()
                        
        
   
        
    