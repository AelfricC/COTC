import time
import subprocess
from xiaopy import *
from cotc import COTC
from Phone_COTC import *

c = COTC("en")
round_per_recover = 6

def find_lv70_cat():
    ret = xp.matchColor("#80854C", 363, 236,1)
    if ret:
        return True
    else:
        return False

characters_array = [1, 0, 0, 4]
skills_array = [3, 0, 0, 4]

characters_array_Cait = [0, 0, 0, 0]
skills_array_Cait = [0, 0, 0, 0]

def run_script_battle():
    #Locate_Wild()
    while True:
        common_encounter_count = 0
        cait_encounter_count = 0
        while True:
            print("swping")
            c.swipe_until_black_screen([206, 434], [1200, 700])
            if find_lv70_cat():
                print("found cait!")
                wait_Battle()
                Boost_Atk()
                wait_Battle()
                print("passed")
                swap()
                delay_tap(1994, 1562)  # boost
                delay_tap(2361, 1551)  # atk
                cait_encounter_count += 1
                common_encounter_count += 1
                Tap_Until_Exsit(Menu, Middle_Screen)
                print("finish battle")
            elif wait_Battle(): #xp.matchColor("#250209", 187, 1496,1):  # bottom left red
                print("start battle")
                # c.flee_battle()
                select_char_and_skill(characters_array, skills_array)
                Boost_Atk()
                common_encounter_count += 1
                print("start clicking until finsh battle")
                Tap_Until_Exsit(Menu, Middle_Screen)
                print("finish battle")
            if common_encounter_count >= round_per_recover:
                break
        # return to hotel
        xp.toast("open world map")
        Tap_Until_Disappear(World_Map)
        double_tap(224, 452)  # tap world type
        double_tap(Town_Loc[0],Town_Loc[1])  # tap town
        Locate_Wild()


run_script_battle()
