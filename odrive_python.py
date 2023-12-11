# -*- coding: utf-8 -*-
from __future__ import division
import time
from pyPS4Controller.controller import Controller

import odrive
from odrive.enums import *


odrv0 = odrive.find_any()
print(str(odrv0.vbus_voltage))

odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL



def transf(raw):
    temp = raw/65534 * 5
    return round(temp, 1)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_R3_down(self, value):
        value = transf(value)
        odrv0.axis0.controller.input_vel = value
        print(value)
            
    def on_R3_up(self, value):
        value = transf(value)
        odrv0.axis0.controller.input_vel = value
        print(value)
    
    def on_x_puless(self):
        kill = 1

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
