from __future__ import division
from time import sleep
from pyPS4Controller.controller import Controller


def transf(raw):
    temp = (raw+32767)/65534
    # Filter values that are too weak for the motors to move
    if abs(temp) < 0.9:
        return 0
    # Return a value between 0.3 and 1.0
    else:
        return round(temp, 1)
    

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_L3_down(self, value):
        value = transf(value)
        print(value)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()