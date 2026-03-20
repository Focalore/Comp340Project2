class Goomba:
    def __init__(self, speed: int):
        self._pos_X = 0
        self._speed = speed
        self.__goomba_sprite = [""] * 10
        self.__set_sprite() #for setting goomba image to __goomba_sprite
        self._direction = True #True: ->, False: <-

    def draw_sprite(self):
        spaces = " " * self._pos_X
        output_frame = ""

        for line in self.__goomba_sprite:
                print(spaces + line)

    def __set_sprite(self):
        self.__goomba_sprite[0] = r"     ________  "
        self.__goomba_sprite[1] = r"    /        \ "
        self.__goomba_sprite[2] = r"   /  \    /  \ "
        self.__goomba_sprite[3] = r"  /   |    |   \ "
        self.__goomba_sprite[4] = r" /  -^------^-  \ "
        self.__goomba_sprite[5] = r"|________________| "
        self.__goomba_sprite[6] = r"      /    \ "
        self.__goomba_sprite[7] = r" ____|      |____ "
        self.__goomba_sprite[8] = r"/____\ ==== /____\ "
        self.__goomba_sprite[9] = r"                     "
    

    def update_pos(self):
        if self._direction: #If self.__direction == True
            self._pos_X += self._speed
        else: #If self.__direction == False
            self._pos_X -= self._speed
    
    def change_dir(self):
        self._direction = not self._direction #Changes True to False and False to True