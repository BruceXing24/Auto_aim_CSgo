# Fachhochschule Aachen
# Name:Bruce_Xing
# Time: 2022/1/9 10:48

import pydirectinput
import keyboard
import time
class Mouse:
    def __init__(self):
        print("start init")
    def move(self,x,y):
        # from 640*480 => 1536*864
        screen_x = int(x * 2.4)
        screen_y = int(y * 1.8)
        if keyboard.read_key() == 'i':
            print("move_x=={},move_y=={}".format(x,y))
            # 672=<x<=864     360=<y<=504   in 1536*864
            pydirectinput.moveTo(screen_x,screen_y)

