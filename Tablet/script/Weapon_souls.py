import time
from xiaopy import *
from Phone_COTC import *

found_soul = ["#999999", 988, 1204]
set_new_soul = ["#191919", 932, 748]
set_old_soul = ["#1D1D1C", 889, 471]
set_soul = ["#E9E9E9", 65, 140]
loading_screen = ["#A4A4A4", 68, 140]
set_another_soul = [1851, 1225]
set_another_soul_new = [1860, 1354]

ui = xp.ui()
Keep_Which = ui.stringValue("Keep_Which")
Rare = ui.boolValue("Rare")

launch_game()
while True:
    double_fast_tap(2599, 1490) #enchant
    double_fast_tap(1839, 1573) #ok
    time.sleep(3)
    while True:
        if Rare: #Only need rare
            if xp.matchColor("#6D7B7B", 2086, 1214,0.85):
                tap_once_After_checking(loading_screen)
                break
            elif xp.matchColor("#999999", 988, 1204) or xp.matchColor("#6F4D3A", 2123, 1222):
                break
            else:
                print("not yet to select soul")
                time.sleep(0.5)
        else:
            if xp.matchColor("#6D7B7B", 2086, 1214,0.85) or xp.matchColor("#704E3B", 2086, 1219,0.85):
                break
            elif xp.matchColor("#999999", 988, 1204) or xp.matchColor("#6F4D3A", 2123, 1222) or xp.matchColor("#6D7B7B", 2086, 1214,0.9):
                time.sleep(2.5)
                break
            else:
                print("not yet to select soul")
                time.sleep(0.5)
    if Keep_Which == "Keep_Old":
        print("keep old")
        double_fast_tap(1461, 791)
        double_fast_tap(1539, 1583) # ok
        time.sleep(3.5)
        print("tap until done")
        tap_Until_Exsit(set_soul, set_another_soul)
        print("done")
    elif Keep_Which == "Keep_New":
        print("keep new")
        double_fast_tap(1505, 1286)
        double_fast_tap(1539, 1583)  # ok
        time.sleep(3)
        print("tap until done")
        tap_Until_Exsit(set_soul, set_another_soul_new)
        print("done")
