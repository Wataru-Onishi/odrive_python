from __future__ import division
from time import sleep
from pyPS4Controller.controller import Controller


def transf(raw):
    temp = (raw+32767)/65534

    

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_L3_down(self, value):
        value = transf(value)
        print(value)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()