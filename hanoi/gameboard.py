import pygame
from pygame.surface import Surface
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
RING_HEIGHT = 50;
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
        
     
        
    def setPillarSpacing(self, name):
        
        pillar = self.pillar[name];
        interval_spacing = self.surface_width / 3;
        mid_spacing = interval_spacing / 2;
        column = pillar.column;
        
        total_spacing = interval_spacing * column + mid_spacing - PILLAR_WIDTH/2;
        pillar.setPillarX(total_spacing);    
        
        
    def draw_base(self):
        #Rect(left, top, width, height)
        pygame.draw.rect(self.surface, BLACK, (0, self.base_y, self.surface_width, 10))
        
        
    def draw_pillar(self, name):
        pygame.draw.rect(self.surface, BLUE, 
                         (self.pillars[name].x, self.base_y-PILLAR_HEIGHT, PILLAR_WIDTH, PILLAR_HEIGHT));
        
        self.draw_rings_in_pillar(name);
        
    def draw_rings_in_pillar(self, name):
        
        num_rings = len(self.pillars[name].rings)
        for ring in num_rings:
            height = (ring+1) * RING_HEIGHT
            
            pygame.draw.rect(self.surface, RED, 
                             (self.pillars[name].x, 
                              self.basey-PILLAR_HEIGHT-height,
                              RING_BLOCK_WIDTH*5,
                              RING_HEIGHT))
    
    
    
    def find_mid_block(self, ring_width):
        for i in range(1, ring_width):
            left_blocks = i;  # x ^ xx..xx where ^ is midpoint
            blocks = left_blocks + 1;
            right_blocks = ring_width - blocks; 
            if left_blocks==right_blocks:
                break;
        return i+1;
    
    def draw_ring_large(self, column):
        #mid_block = self.find_mid_block(LARGE_BLOCKS);
        #left_blocks = mid_block - 1;
        pass
        
    
    
    def draw_ring_medium(self, column):
        pass;
    
    def draw_ring_small(self, column):
        pass;