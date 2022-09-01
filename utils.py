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

def bgIterImage(screen, image):
    for x in range(svx // image.get_width() + 1):
        for y in range(svy // image.get_height() + 1):
            screen.blit(image, (x*image.get_width(), y*image.get_height()))

def bgFullImage(screen, imagepath):
    image = Image.open(f"{gpath}/assets/{imagepath}")
    image = image.resize((svx, svy)); image.save(f"assets/temp_{imagepath}")
    screen.blit(spriteLoad(f"{gpath}/assets/temp_{imagepath}"), (0, 0))

def bgPutImage(screen, imagepath, size_x, size_y, pos_x, pos_y): #size-pos should be cell%
    fs_x, fs_y = returnCell(size_x, size_y)
    fpos_x, fpos_y = returnCell(pos_x, pos_y)
    fs_x = int(fs_x); fs_y = int(fs_y)
    image = Image.open(f"{gpath}/assets/{imagepath}")
    image = image.resize((fs_x, fs_y)); image.save(f"assets/temp_{imagepath}")
    screen.blit(spriteLoad(f"{gpath}/assets/temp_{imagepath}"), (fpos_x, fpos_y))

def returnCell(pos_x, pos_y):
    '''Works for both positions and length/height values'''
    svxc = svx / 100; svyc = svy / 100 #finds out cell size
    return pos_x * svxc, pos_y * svyc  #returns %posi into pixel posi

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