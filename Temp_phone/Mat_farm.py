import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

characters_array = [1, 2, 0, 0]
skills_array = [[4,3], [0], [0], [0]] #cyrus
skills_array1 = [[4], [4,0,1], [0], [0]] #recover
skills_array2 = [[4], [3,0], [0], [0]] #abosorb
skills_array_Cait = [0, 0, 0, 0]

#farm const
Tap_Host = ["#EEE6DD", 1334, 417]
Enter_Holtel = ["#FFFFFF", 1149, 359]
Wild_Loc = [1122, 410]
Town_Loc = [1156, 673]
Monster_Loc = [894, 394]
Arrive_In_Sec = 4.5
round_per_recover = 18

def Locate_Wild():
    #time.sleep(6)
    double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    print("procced, gonna click ok to tele")
    time.sleep(0.5)
    tap_After_checking(Map_Ok,15)  # ok
    wait_Idle()
    tap_After_checking(Enter_Holtel)  # enter hotel
    print("Enter hotel")
    wait_Idle()
    print("Tap the host")
    #double_fast_tap(1213, 426)???
    tap_once_After_checking(Tap_Host)
    time.sleep(2)
    tap_Until_Exsit(Comfirm_To_Rest, Middle_Screen)
    print("ok to rest")
    tap_After_checking(Comfirm_To_Rest)
    print("ok")
    tap_Until_Exsit(Menu, Rest_OK)
    print("open world map")
    tap_After_checking(World_Map)
    delay_tap(Wild_Loc[0], Wild_Loc[1])  # tap wild
    double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    tap_After_checking(Map_Ok,15)  # ok
    wait_Idle()
    ##### for brilliant weapon #####
    # print("zoom map")
    # zoom_map()
    # time.sleep(0.5)
    # print("swipe")
    # xp.swipe(1726, 258, 1029, 637, 0.5)
    # time.sleep(0.5)
    # delay_tap(Wild_Loc[0], Wild_Loc[1])  # tap wild
    # double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    # tap_After_checking(Map_Ok,15)  # ok
    # checking_Color(Menu)
    # print("open mini map")
    # delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    # delay_tap(1068, 335)  # get into gate
    # wait_Idle()
    # delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    # delay_tap(643, 423)
    # wait_Idle()
    # double_fast_tap(1134, 502)
    # double_fast_tap(1370, 645)
    # wait_Idle()
    ##### for brilliant weapon #####
    delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    delay_tap(Monster_Loc[0], Monster_Loc[1])  # farm location
    time.sleep(Arrive_In_Sec)

def run_script_battle(characters_array, skills_array,round_per_recover):
    launch_game()
    time.sleep(0.8)
    Locate_Wild()
    battle_count = 0
    cait_encounter_count = 0
    while True:
        common_encounter_count = 0
        while True:
            print("swping")
            swipe_Until_Black()
            wait_Battle()
            while True:
                if xp.matchColor("#962B2B", 267, 123,0.85):
                    print("found cait!")
                    # escape()
                    cait_encounter_count += 1
                    if common_encounter_count > 0:
                        common_encounter_count -= 1
                    swap()
                    boost_Atk()
                    time.sleep(10)
                    wait_Battle()
                    swap()
                    boost_Atk()
                    time.sleep(5)
                    tap_Until_Exsit(Menu, ATK,20)
                    print("finish battle")
                    break
                elif xp.matchColor("#17486A", 291, 102,0.9):
                    print("start battle")
                    select_char_and_skill(characters_array, skills_array,1,1)
                    common_encounter_count += 1
                    battle_count += 1
                    print("start clicking until finsh battle")
                    tap_Until_Exsit(Menu, ATK,20)
                    print("finish battle")
                    break
            xp.toast("normal " + str(battle_count) + "  " + "Cait: " + str(cait_encounter_count))
            if common_encounter_count == round_per_recover:
                break
            ####for continuing going to the farm location
            if common_encounter_count == 1:
                print("open mini map")
                delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
                delay_tap(Monster_Loc[0], Monster_Loc[1])  # farm location
                time.sleep(2)
        # return to hotel
        print("open map")
        tap_After_checking(World_Map,8)
        # delay_tap(224, 452)  # tap world type
        time.sleep(0.5)
        # zoom_map()
        print("tap town")
        delay_tap(Town_Loc[0],Town_Loc[1])  # tap town
        time.sleep(0.4)
        Locate_Wild()

run_script_battle(characters_array, skills_array,round_per_recover)
#local_mat_farm()
