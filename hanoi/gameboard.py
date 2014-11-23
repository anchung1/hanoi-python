import pygame
from pygame.surface import Surface

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PILLAR_HEIGHT = 250;
PILLAR_WIDTH = 15

LARGE_BLOCKS = 9;
MEDIUM_BLOCKS = 7;
SMALL_BLOCKS = 5;
RING_LARGE_WIDTH = PILLAR_WIDTH * LARGE_BLOCKS;
RING_MEDIUM_WIDTH = PILLAR_WIDTH * MEDIUM_BLOCKS;
RING_SMALL_WIDTH = PILLAR_WIDTH * SMALL_BLOCKS;

class Base(object): 
            
    def __init__(self, s, w, h): 
        self.surface = s;
        self.surface_width = w;
        self.surface_height = h;
        self.base_y = self.surface_height-100;
        
        
    def draw_base(self):
        #Rect(left, top, width, height)
        pygame.draw.rect(self.surface, BLACK, (0, self.base_y, self.surface_width, 10))
        
        
    def draw_pillar(self, column):
        interval_spacing = self.surface_width / 3;
        mid_spacing = interval_spacing / 2;
        
        total_spacing = interval_spacing * column + mid_spacing - PILLAR_WIDTH/2;
        pygame.draw.rect(self.surface, BLUE, (total_spacing, self.base_y-PILLAR_HEIGHT, PILLAR_WIDTH, PILLAR_HEIGHT));
    
    def find_mid_ring(self, ring_width):
        for i in range(1, ring_width):
            left_blocks = i;  # x ^ xx..xx where ^ is midpoint
            blocks = left_blocks + 1;
            right_blocks = ring_width - blocks; 
            if left_blocks==right_blocks:
                break;
        return i+1;
    
    def draw_ring_large(self, column):
        mid_block = self.find_mid_ring(LARGE_BLOCKS);
        left_blocks = mid_block - 1;
        
        
    
    
    def draw_ring_medium(self, column):
        pass;
    
    def draw_ring_small(self, column):
        pass;