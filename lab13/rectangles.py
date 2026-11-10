import pygame

# Always begin with initialization, sizing, and captioning
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SHAPE_WIDTH = 200
SHAPE_HEIGHT = 150
BORDER_THICKNESS = 10
SHAPE_FILL_COLOR = (255, 0, 200)
SHAPE_BORDER_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 192, 203)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle')

# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(BACKGROUND_COLOR)  
    the_rectangle = (300, 225, 600, 150) 
    pygame.draw.rect(screen, SHAPE_FILL_COLOR, the_rectangle)  
    pygame.draw.rect(screen, SHAPE_BORDER_COLOR, the_rectangle, BORDER_THICKNESS)  
    pygame.display.flip() 


# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit