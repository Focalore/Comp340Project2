
from Goomba import Goomba
class GoombaAdv(Goomba):

    def __init__(self, speed):
        super().__init__(speed)
        self.goombaSpriteRightFoot = [""] * 10
        self.goombaSpriteLeftFoot = [""] * 10
        self.footCount = 0   # for determining which foot is forward, and ease of calling the next sprite
        

        self._set_sprite()

    def draw_sprite(self):
        spaces = " " * self._pos_X

        if self.footCount % 2 == 0: #if footCount is even, right foot is forward
            for line in self.goombaSpriteRightFoot:
                print(spaces + line)
                
        else:
            for line in self.goombaSpriteLeftFoot:
                print(spaces + line)

        self.footCount += 1
                


    def _set_sprite(self):
        self.goombaSpriteRightFoot[0] = r"     ________  ";         #right foot forward sprite
        self.goombaSpriteRightFoot[1] = r"    /        \ ";
        self.goombaSpriteRightFoot[2] = r"   /  \    /  \ ";
        self.goombaSpriteRightFoot[3] = r"  /   |    |   \ ";
        self.goombaSpriteRightFoot[4] = r" /  -^------^-  \ ";
        self.goombaSpriteRightFoot[5] = r"|________________| ";
        self.goombaSpriteRightFoot[6] = r"      /    \ ____ ";
        self.goombaSpriteRightFoot[7] = r" ____|      /____\ ";
        self.goombaSpriteRightFoot[8] = r"/____\ ====         ";
        self.goombaSpriteRightFoot[9] = r"                     ";

        self.goombaSpriteLeftFoot[0] = r"     ________  ";          #left foot forward sprite
        self.goombaSpriteLeftFoot[1] = r"    /        \ ";
        self.goombaSpriteLeftFoot[2] = r"   /  \    /  \ ";
        self.goombaSpriteLeftFoot[3] = r"  /   |    |   \ ";
        self.goombaSpriteLeftFoot[4] = r" /  -^------^-  \ ";
        self.goombaSpriteLeftFoot[5] = r"|________________| ";
        self.goombaSpriteLeftFoot[6] = r" ____ /    \ ";  
        self.goombaSpriteLeftFoot[7] = r"/____\      |____ ";
        self.goombaSpriteLeftFoot[8] = r"       ==== /____\ ";
        self.goombaSpriteLeftFoot[9] = r"                     ";



#IM going to be honest, im running out of time for this and i have made it work. I repoened the project and made a change to something 
# that change in turn somehow completely broke the whole of the code and i for the life of me cannot figure out how to fix whatever this error is. 
#hours wasted: 4 (as of 11:00 pm on due date, i have made it work. thank god, but i do hate dingle character mistakes. sorry i lost all my comments in the mess)
#hours not wasted: 1.5 (when i got it workign)