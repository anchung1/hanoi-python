from ring import Ring
class Pillar(object):
    


    def __init__(self, name):
        #names can be left, middle, right
        self.name = name;
        self.rings = [];
        if name=="left":
            self.column = 1;
        elif name=="middle":
            self.column = 2;
        else:
            self.column = 3;    
        
    def set_rings(self, ring):
        self.rings.append(ring)
        
    def check_legal_move(self, a_ring):
        for ring in self.rings:
            if a_ring.ringSize > ring.ringSize:
                return False
        return True    

    def setPillarX(self, x):
        self.x = x;
        
    
    
        
        
        
    
        