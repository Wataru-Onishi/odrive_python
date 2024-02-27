# -*- coding: utf-8 -*-
from __future__ import division
import time
from pyPS4Controller.controller import Controller

import odrive
from odrive.enums import *


odrv0 = odrive.find_any()
print(str(odrv0.vbus_voltage))

windows_size = 15
speed = [0] * windows_size
speed_param = 15

def mov_ave(new_val):
    speed.pop(0)
    speed.append(new_val)

    if not speed:  # 配列が空の場合
        return 0
    return sum(speed) / len(speed)  # 合計値を要素数で割って平均を求める

def transf(raw):
    speed = raw/65534 * 2 * speed_param
    speed = round(mov_ave(speed), 1)
    print(speed)
    return speed

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_R3_down(self, value):
        value = transf(value)
        if(abs(value) <1):
            value = 0
            odrv0.axis0.controller.input_vel = 0
        else:
            odrv0.axis0.controller.input_vel = value
            #print(value)
            
    def on_R3_up(self, value):
        value = transf(value)
        if(abs(value) <1):
            value = 0
            odrv0.axis0.controller.input_vel = 0
        else:
            odrv0.axis0.controller.input_vel = value
            #print(value)

    #def on_R2_press(self):
    #    for i in range(len(speed)):
    #        speed[i] = 0
    
    def on_R3_y_at_rest(self):
        odrv0.axis0.controller.input_vel =0

    def on_circle_press(self):
        odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    
    def on_x_press(self):
        odrv0.axis0.controller.input_vel = 0
        odrv0.axis0.requested_state = AXIS_STATE_IDLE
        exit()  


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
