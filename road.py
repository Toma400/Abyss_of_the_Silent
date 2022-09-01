import pygame; pygame.init()
import objects, utils
from utils import (
    gpath,
    svx,
    svy
)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Set up the drawing window
screen = pygame.display.set_mode([svx, svy])
imbg = utils.spriteLoad("test.jpg")
imbt = utils.spriteLoad("start.png")

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    utils.bgIterImage(screen=screen, image=imbg)
    utils.bgPutImage(screen=screen, imagepath="start.png", size_x=50, size_y=30, pos_x=25, pos_y=60)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
utils.exitRemover(); pygame.quit()