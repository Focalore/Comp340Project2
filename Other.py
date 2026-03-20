from random import random
from Goomba import Goomba
class other(Goomba):

    def __init__(self, speed):
        super().__init__(speed) 

        self.__otherSprite = [None] * 6
        

        self.__otherSprite = [""] * 10
        self.__otherSprite2 = [""] * 10

        self.__set_sprite()


    def __set_sprite(self):
  
        self.__otherSprite[0] = r"              "
        self.__otherSprite[1] = r"     /\_/\    "
        self.__otherSprite[2] = r"    ( >_< )   "
        self.__otherSprite[3] = r"     \___/    "
        self.__otherSprite[4] = r"       ||     "
        self.__otherSprite[5] = r"   ____||____ "
        self.__otherSprite[6] = r"  |__________|"
        self.__otherSprite[7] = r"  |    |     |"
        self.__otherSprite[8] = r"  |    |     |"
        self.__otherSprite[9] = r"  |__________|"
        #thank you ai, i dont know what this is but i love it. 

        self.__otherSprite2[0] = r"    __/\__    "
        self.__otherSprite2[1] = r"   / v v \    "
        self.__otherSprite2[2] = r"  | (O O) |   "
        self.__otherSprite2[3] = r"   \_____/    "
        self.__otherSprite2[4] = r"      ||      "
        self.__otherSprite2[5] = r"   ____||____ "
        self.__otherSprite2[6] = r"  |__________|"
        self.__otherSprite2[7] = r"  |    |     |"
        self.__otherSprite2[8] = r"  |    |     |"
        self.__otherSprite2[9] = r"  |__________|"
        #yet again a masterpiece from ai


    def draw_sprite(self):
        spaces = " " * self._pos_X
        
      
        if self._pos_X % 2 == 0:
            for line in self.__otherSprite:
                print(spaces + line)
        else:
            for line in self.__otherSprite2:
                print(spaces + line)