import time
import subprocess
from xiaopy import *
from Phone_COTC import *

stove_reward = ["#4E4E50", 2617, 445]
close_window = [2918, 122]
feat_reward = ["#505050", 2222, 620]
page_return = ["#E9E9E9", 68, 141]
ok_collect = [1475, 1509]
stove_burning = ["#D0C4B4", 934, 566]
idel_hunt = ["#FBFAF7", 558, 1430]
tap_here = [2209, 1493]
def login_screen():
    tap_Until_Exsit(Menu,Middle_Screen)
    tap_Until_Exsit(Menu, Middle_Screen)
    if xp.matchColor("#F7F6F5", 1722, 1435,0.9):
        print("second world")
        xp.tap(1686, 1494)
    else:
        xp.tap(1955, 1495)
    time.sleep(2)
    checking_Color(page_return)
    delay_tap(502, 1562)#collect
    delay_tap(1823, 1460)
    delay_tap(1477, 1299)
    delay_tap(238, 1575)
    double_fast_tap(209, 1574)
    checking_Color(stove_reward)
    delay_tap(1485, 1495)
    print("started")
    tap_Until_Exsit(stove_burning,ok_collect,30)
    print("end")
    tap_Until_Exsit(Menu, close_window)
    tap_Until_Exsit(Menu, close_window)
    #hunt
    xp.tap(788, 1508)
    checking_Color(page_return)
    double_fast_tap(246, 1573)
    time.sleep(1)
    checking_Color(page_return)
    double_tap(264, 911)#other world tab
    delay_tap(219, 893)#LAL
    delay_tap(2609, 1550)#begin
    delay_tap(2271, 1542)# manual begin
    time.sleep(1)
    delay_tap(1854, 1259)#enter
    wait_Idle()
    delay_tap(2514, 274)#mini map
    delay_tap(1375, 429)#head to boss
    wait_Idle()
    xp.swipe(1445, 1123,1508, 268,1.7)
    time.sleep(1)
    delay_tap(1842, 1221)#fight boss
    time.sleep(7)
    if xp.matchColor("#F0ECE7", 2430, 587) and xp.matchColor("#FFAB1C", 2545, 528) and xp.matchColor("#FFFFFF", 2476, 1549):
        print("battle")
        delay_tap(1996, 1578)
        double_fast_tap(2515, 1583)
    time.sleep(4)
    tap_Until_Exsit(Menu, close_window)
    tap_Until_Exsit(Menu, close_window)
    #feats
    delay_tap(209, 1476)
    delay_tap(883, 1464)
    checking_Color(page_return)
    double_fast_tap(2533, 293)
    checking_Color(feat_reward)
    delay_tap(1487, 1320)
    #ads
    delay_tap(283, 1379)#open ads
    tap_Until_Exsit(Menu, close_window)
def lunch_game_login():
    launch_game(1)
    login_screen()

lunch_game_login()

# exchange
# delay_tap(209, 1476)
# delay_tap(1791, 1486)
# checking_Color(page_return)
# delay_tap(2120, 1538)
# time.sleep(1)
# checking_Color(page_return)
# double_fast_tap(281, 1433)
# delay_tap(2374, 671)
# delay_tap(2575, 1530)
# delay_tap(1857, 1489)
# tap_Until_Exsit(Menu, close_window)