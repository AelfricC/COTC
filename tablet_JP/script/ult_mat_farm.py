import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

launch_game()
battle_count = 0
print("start")
while True:
    wait_Idle()
    print("swping")
    swipe_Until_Black()
    battle_count += 1
    xp.toast(str(battle_count))