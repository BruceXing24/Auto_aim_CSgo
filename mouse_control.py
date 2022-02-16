# Fachhochschule Aachen
# Name:Bruce_Xing
# Time: 2022/2/9 10:48

import pydirectinput
import keyboard
import time
def mouse_move(x,y):
    flag = 0
    x = int(x*2.4)
    y = int(y*1.8)
    j, k = pydirectinput.position()
    print("进入mouse_move")
    if keyboard.read_key() == 'i' and flag==0:
        print("move_x=={},move_y=={}".format(x,y))
        # print(pydirectinput.size())
        pydirectinput.moveTo(x,y)
        # time.sleep(0.5)
        # flag+=1
        # pydirectinput.moveRel(x-960,y-540)

