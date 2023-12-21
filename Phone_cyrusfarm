import time
import subprocess
from xiaopy import *
from cotc import COTC

c = COTC("en")
round_per_recover = 6

def delay_tap(x,y):
    time.sleep(1)
    xp.tap(x,y)

def find_lv70_cat():
    ret = xp.matchColor("#80854C", 363, 236,1)
    if ret:
        return True
    else:
        return False

def wait_Battle():
    time.sleep(2)
    while True:
        if not xp.matchColor("#250209", 187, 1496, 1):  # bottom left red
            time.sleep(1)
        else:
            time.sleep(1)
            break
def wait_Idle():
    time.sleep(2)
    while True:
        if not xp.matchColor("#EEEEED", 1671, 1441, 1): #check menu
            time.sleep(1)
        else:
            break
def Locate_Wild():
    delay_tap(2388, 1507)  # proceed
    delay_tap(1838, 1199)  # ok
    time.sleep(10)
    xp.toast("进入旅店")
    xp.tap(1467, 523)  # enter hotel
    time.sleep(7)
    xp.toast("点击旅店老板")
    delay_tap(1611, 761)  # click host
    delay_tap(1611, 761)  # click host
    delay_tap(1611, 761)  # click host
    xp.toast("before")
    time.sleep(3)
    time.sleep(2)
    xp.toast("ok to rest")
    delay_tap(1786, 1228)  # ok to rest
    time.sleep(8)
    xp.toast("ok")
    xp.tap(1584, 1205)  # ok
    time.sleep(3)
    xp.toast("open world map")
    delay_tap(1986, 1514)
    delay_tap(203, 691)  # tap Hell type
    time.sleep(1)
    delay_tap(1333, 1111)  # tap wild
    time.sleep(1)
    delay_tap(2388, 1507)  # proceed
    delay_tap(1838, 1199)  # ok
    time.sleep(6)
    # arrive wild
    xp.toast("open mini map")
    delay_tap(2464, 469)
    delay_tap(1688, 1238)  # farm location
    time.sleep(4)


def tap_until_finishBattle():
    count = 0
    while count < 50:
        if not xp.matchColor("#EEEEED", 1671, 1441,1):  # menu location
            xp.tap(1785, 671)  # middle of the screen
            time.sleep(0.5)
            count += 1
            print(count)
        else:
            break


def select_char(va):
    if va == 1:
        delay_tap(2570, 259)
    elif va == 2:
        delay_tap(2638, 521)
    elif va == 3:
        delay_tap(2653, 920)
    elif va == 4:
        delay_tap(2736, 1241)

def select_skill(va):
    if va == 2:
        delay_tap(1696, 778)
    elif va == 3:
        delay_tap(1803, 1020)
    elif va == 4:
        delay_tap(1748, 1273)
    elif va == 5:
        delay_tap(1747, 1496)
    elif va == 1:
        delay_tap(1775, 551)

def select_char_and_skill(characters, skills):
    for char, skill in zip(characters, skills):
        select_char(char)
        select_skill(skill)


def escape():
    while True:
        if not xp.matchColor("#EEEEED", 1671, 1441, 1):  # menu location
            delay_tap(1261, 1571)
        else:
            break
characters_array = [1, 0, 0, 4]
skills_array = [3, 0, 0, 4]

characters_array_Cait = [0, 0, 0, 0]
skills_array_Cait = [0, 0, 0, 0]
def run_script_battle():
    Locate_Wild()
    while True:
        total_encounter_count = 0
        common_encounter_count = 0
        cait_encounter_count = 0
        while True:
            c.swipe_until_black_screen([206, 434], [1200, 700])
            time.sleep(6)
            if find_lv70_cat():
                time.sleep(4)
                #select_char_and_skill(characters_array_Cait, skills_array_Cait)
                delay_tap(1994, 1562)#boost
                delay_tap(2361, 1551)#atk

                print("start loolking")
                wait_Battle()
                print("passed")
                delay_tap(1743, 1563)#swap
                #select_char_and_skill(characters_array_Cait, skills_array_Cait)
                delay_tap(1994, 1562)  # boost
                delay_tap(2361, 1551)  # atk
                cait_encounter_count += 1
            elif xp.matchColor("#250209", 187, 1496,1):  # bottom left red
                print("start battle")
                # c.flee_battle()
                select_char_and_skill(characters_array, skills_array)
                delay_tap(1994, 1562)#boost
                delay_tap(2361, 1551)#atk
            common_encounter_count += 1
            # print("检测主界面")
            # check this
            tap_until_finishBattle()
            print("finish battle")
            total_encounter_count += 1
            if common_encounter_count >= round_per_recover:
                break
        # return to hotel
        xp.toast("open world map")
        delay_tap(1986, 1514)
        delay_tap(224, 452)  # tap world type
        time.sleep(1)
        delay_tap(1615, 713)  # tap wild
        Locate_Wild()


run_script_battle()
