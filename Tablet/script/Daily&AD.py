import time
import subprocess
from xiaopy import *
from Phone_COTC import *

ad_button = ["#FFFFFF", 2307, 1448]
accept_reward = ["#FFFFFF", 2605, 320]
def ad_cait():
    launch_game()
    count = 0
    tap_After_checking(World_Map)
    double_fast_tap(307, 444)
    zoom_map()
    #xp.swipe(1711, 527,1009, 1258)
    time.sleep(1)
    while True:
        ret = xp.findImage("nameless_town.png", 46, 163, 2850, 1666,0.7)
        if ret:
            delay_tap(ret.x-200, ret.y)
            print("found")
            time.sleep(0.5)
            delay_tap(2183, 1524)
            delay_tap(1959, 1456)
            tap_Until_Exsit(Menu,close_window)
            print("back to menu")
            time.sleep(1)
            double_fast_tap(2221, 668)
            tap_once_After_checking(accept_reward)
            tap_Until_Exsit(Menu,close_window)
            tap_Until_Exsit(Menu, close_window)
            break
        else:
            print("not found yet")
            time.sleep(0.5)
    while True:
        wait_Idle()
        if count < 5:
            delay_tap(2218, 1489)
            delay_tap(1926, 884)
            delay_tap(2174, 1230)
            time.sleep(2)
            tap_Until_Exsit(ad_button,Middle_Screen)
            count += 1
            xp.toast(str(count))
        else:
            xp.toast("Completed")
            break
ad_cait()
