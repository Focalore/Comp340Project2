from Star import Star
from Goomba import Goomba
from Ground import Ground
from GoombaWalk import Goombawalk
import subprocess
import os
import time
from GoombaAdv import GoombaAdv
from Other import other


star = Star(0)
goomba = GoombaAdv(4) #Goomba has speed of 4 #Changed to GoombaAdv for walking animation
ground = Ground(120)
thing = other(3) #my animation 

# for i in range(3):
#     subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
#     goomba.draw_sprite()
#     goomba.update_pos()
#     time.sleep(0.3) # wait 0.3 seconds

# goomba.change_dir()
# goomba.update_pos()

# for i in range(3):
#     subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Clear console using subprocess
#     goomba.draw_sprite()
#     goomba.update_pos()
#     time.sleep(0.3) # wait 0.3 seconds

gWalkAnimation = Goombawalk(star, goomba, ground)

#Clear console using subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

gWalkAnimation.start_animation()