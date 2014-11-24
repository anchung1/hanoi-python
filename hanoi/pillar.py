from ring import Ring
class Pillar(object):
    


    def __init__(self, name):
        #names can be left, middle, right
        self.name = name;
        self.rings = [];
        if name=="left":
            self.column = 1;
            self.label = "A"
        elif name=="middle":
            self.column = 2;
            self.label = "B"
        else:
            self.column = 3;
            self.label = "C"    
        
    def set_rings(self, ring):
        self.rings.append(ring)
        
    def check_legal_move(self, a_ring):
        for ring in self.rings:
            if a_ring.ringSize > ring.ringSize:
                return False
        return True    

    def setPillarX(self, x):
        self.x = x;
        
    def setFont(self, text):
        self.text = text;    
        
    
    
        
        
        
    
        