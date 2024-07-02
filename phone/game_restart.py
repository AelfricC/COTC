import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

def game_restart():
    xp.home()
    time.sleep(3.5)
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")
    tap_Until_Exsit(moloply_restart_confirm, Middle_Screen)
    tap_Until_Exsit(moloply_restart_confirm, Middle_Screen)
    double_tap(1919, 1201)
game_restart()