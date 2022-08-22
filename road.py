import pygame; pygame.init()
import toml; sv = toml.load("settings.toml")
svx = sv["screen_res_x"]; svy = sv["screen_res_y"]
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

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (svx/2, svy/2), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()