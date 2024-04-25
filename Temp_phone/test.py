import time
import subprocess
from xiaopy import *
from Phone_COTC import *

tap_Until_Disappear(World_Map)
# delay_tap(224, 452)  # tap world type
time.sleep(0.5)
zoom_map()
delay_tap(Town_Loc[0], Town_Loc[1])  # tap town