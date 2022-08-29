import os, pygame
import toml; sv = toml.load("settings.toml")
svx = sv["screen_res_x"]; svy = sv["screen_res_y"]
from PIL import Image
gpath = os.path.dirname(os.path.abspath("road.py"))

#===================================================
# SPRITES
#===================================================
def spriteLoad(path):
    path = os.path.join(gpath, "assets", path)
    try:
        surface = pygame.image.load(path)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (path, pygame.get_error()))
    return surface.convert()

def bgIterImage(screen, image, qual: int):
    for x in range(svx // qual + 1):
        for y in range(svx // qual + 1):
            screen.blit(image, (x*qual, y*qual))

def bgFullImage(screen, imagepath):
    image = Image.open(f"{gpath}/assets/{imagepath}")
    image = image.resize((svx, svy)); image.save(f"assets/temp_{imagepath}")
    screen.blit(spriteLoad(f"{gpath}/assets/temp_{imagepath}"), (0, 0))

def scaleToRes(imagepath):
    ratio = svx / svy
    image = Image.open(f"{gpath}/assets/{imagepath}")
    image = image.resize((svx, svy)); image.save(f"assets/temp_{imagepath}")

#===================================================
# SOUNDS
#===================================================
def soundLoad(path):
    if not pygame.mixer: return None
    path = os.path.join(gpath, "assets", path)
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error:
        print("Warning, unable to load, %s" % path)
    return None

#===================================================
# SYS
#===================================================
def exitRemover():
    """Removes temp files used by program"""
    import os; vdel = os.listdir(f"{gpath}/assets/")
    for i in vdel:
        if "temp_" in i:
            os.remove(f"{gpath}/assets/{i}")