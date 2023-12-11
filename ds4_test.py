# -*- coding: utf-8 -*-
from __future__ import division
from time import sleep
from pyPS4Controller.controller import Controller



def transf(raw):
    temp = raw/65534 * 5
    return round(temp, 1)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_R3_down(self, value):
        if(abs(value) <0.5):
            value = 0
        else:
            value = transf(value)
        print(value)
            
    def on_R3_up(self, value):
        if(abs(value) <0.5):
            value = 0
        else:
            value = transf(value)
        print(value)
        
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()