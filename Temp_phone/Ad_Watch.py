import time
import subprocess
from xiaopy import *
from Phone_COTC import *

ad_button = ["#FFFFFF", 1679, 885]
use_ticket = ["#2A5D57", 1684, 769]
use_ticket_xy = [1605, 740]
def ad_cait():
    launch_game()
    count = 0
    while True:
        if count < 5:
            delay_tap(1624, 902)
            delay_tap(1416, 520)
            tap_After_checking(use_ticket)
            time.sleep(2)
            tap_Until_Exsit(ad_button,use_ticket_xy)
            count += 1
            xp.toast(str(count))
        else:
            xp.toast("Completed")
            break
ad_cait()
