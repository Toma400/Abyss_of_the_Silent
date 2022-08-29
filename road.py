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
imbg = utils.spriteLoad("menu.png")
imbt = utils.spriteLoad("start.png")

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    #utils.bgIterImage(screen=screen, image=imbg, qual=160)
    utils.bgFullImage(screen=screen, imagepath="isle.jpg")
    #screen.blit(imbt, (svx/3.5, svy/1.457))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
utils.exitRemover(); pygame.quit()