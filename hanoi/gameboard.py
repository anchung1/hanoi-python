import pygame

from pillar import Pillar
from ring import Ring

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED  = (255, 0, 0)


LARGE_BLOCKS = 9;
MEDIUM_BLOCKS = 7;
SMALL_BLOCKS = 5;
PILLAR_HEIGHT = 250;
PILLAR_WIDTH = 15
RING_LARGE_WIDTH = PILLAR_WIDTH * LARGE_BLOCKS;
RING_MEDIUM_WIDTH = PILLAR_WIDTH * MEDIUM_BLOCKS;
RING_SMALL_WIDTH = PILLAR_WIDTH * SMALL_BLOCKS;
RING_HEIGHT = 30;
RING_BLOCK_WIDTH = 50;

class Base(object): 
            
    def __init__(self, s, w, h): 
        self.surface = s;
        self.surface_width = w;
        self.surface_height = h;
        self.base_y = self.surface_height-100;
        self.pillars = {"left": Pillar("left"), "middle": Pillar("middle"), "right": Pillar("right")};
        self.rings = {"ring_1": Ring(1), "ring_2": Ring(2), "ring_3": Ring(3)};
        
        
        self.pillars["left"].set_rings(self.rings["ring_1"]);
        self.pillars["left"].set_rings(self.rings["ring_2"]);
        self.pillars["left"].set_rings(self.rings["ring_3"]);
        
        self.setPillarSpacing("left");
        self.setPillarSpacing("middle");
        self.setPillarSpacing("right");
        
        self.setupFont("left");
        self.setupFont("middle");
        self.setupFont("right");
     
        
    def setPillarSpacing(self, name):
        
        pillar = self.pillars[name];
        interval_spacing = self.surface_width / 3;
        mid_spacing = interval_spacing / 2;
        column = pillar.column;
        
        total_spacing = interval_spacing * (column-1) + mid_spacing - PILLAR_WIDTH/2;
        print name + str(total_spacing)
        
        pillar.setPillarX(total_spacing);    
        
        
    def setupFont(self, name):
        font = pygame.font.Font(None, 36);
        text = font.render(self.pillars[name].label, 1, (10, 10, 10));
        self.pillars[name].setFont(text);
            
    def draw_base(self):
        #Rect(left, top, width, height)
        pygame.draw.rect(self.surface, BLACK, (0, self.base_y, self.surface_width, 10))
        
        
        
        #font = pygame.font.Font(None, 36)
        #text = font.render("A", 1, (10, 10, 10))
        #self.surface.blit(text, (100, 100))
        
        
    def draw_pillar(self, name):
        pygame.draw.rect(self.surface, BLUE, 
                         (self.pillars[name].x, self.base_y-PILLAR_HEIGHT, PILLAR_WIDTH, PILLAR_HEIGHT));
        
        self.draw_rings_in_pillar(name);
        
        self.surface.blit(self.pillars[name].text, 
                          (self.pillars[name].x, self.base_y + 20));
        
    def draw_rings_in_pillar(self, name):

        i = 1;
        padding = 5;
        for ring in reversed(self.pillars[name].rings):
            width = RING_BLOCK_WIDTH * ring.ringSize
            x = self.pillars[name].x - (width - PILLAR_WIDTH)/2
            y = self.base_y - i *(RING_HEIGHT+padding)
            
            i += 1
            pygame.draw.rect(self.surface, RED, 
                             (x, 
                              y,
                              RING_BLOCK_WIDTH*ring.ringSize,
                              RING_HEIGHT))
    
    def move(self, key1, key2):
        #key1 is source
        #key2 is destination
        
        
        for pillar in self.pillars:
            if key1 == self.pillars[pillar].label.lower():
                source_pillar = self.pillars[pillar];
            if key2 == self.pillars[pillar].label.lower():
                dest_pillar = self.pillars[pillar];
        
        #crash when popping from empty list        
        if len(source_pillar.rings) == 0:
            return;
                
        source_ring = source_pillar.rings.pop(0);
        is_legal = dest_pillar.check_legal_move(source_ring);
        
        if is_legal:
            dest_pillar.rings.insert(0, source_ring)
        else:
            source_pillar.rings.insert(0, source_ring);
                
        print key1 + "," + key2
        
    
    