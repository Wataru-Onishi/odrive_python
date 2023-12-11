import odrive
from odrive.enums import *

odrv0 = odrive.find_any()
print(str(odrv0.vbus_voltage))

odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis0.controller.input_vel = 2
