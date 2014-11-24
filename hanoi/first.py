import pygame
from gameboard import Base
from keyhandler import KeyHandler


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tower of Hanoi")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

board = Base(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
key = KeyHandler(board)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            #print "done"
        if event.type == pygame.KEYDOWN and event.key==pygame.K_a:
            key.keyAdd("a")
            #print "Key A pressed"
        if event.type == pygame.KEYDOWN and event.key==pygame.K_b:
            key.keyAdd("b")
            #print "Key B pressed"
        if event.type == pygame.KEYDOWN and event.key==pygame.K_c:
            key.keyAdd("c")
            #print "Key C pressed"
        if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
            key.keyClear()
               
                     
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    
    board.draw_base();
    board.draw_pillar("left");
    board.draw_pillar("middle");
    board.draw_pillar("right");
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()