import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

option_xy = [1677, 1030]

dice = ["#F2F5F6", 2625, 1428]
option = ["#4E4437", 1583, 1033]
wealth = ["#40382C", 764, 831]
item_obtained = ["#255B70", 1615, 1532]
quit_game = ["#F7F6F5", 138, 1412]
quit_game2 = ["#CDCDCB", 686, 1474]
quit_game3 = ["#FFFFFF", 1812, 1205]
#-------------------
quit_game4 = ["#326478", 1911, 1207]
def bt_wait_Idle():
    if not xp.matchColor("#F0EBE8", 535, 1545):
        time.sleep(0.4)
        return False
    else:
        print("can dice now")
        time.sleep(0.5)
        return True

def dice_it(count):
    if count > 0:
        double_fast_tap(2695, 1456)
        double_fast_tap(2625, 1428)
    else:
        xp.swipe(2552, 1438, 2635, 1100, 0.4)
        time.sleep(0.4)
def onetime_wait_Battle(count):
    if count > 0 and xp.matchColor("#ABA8A3", 970, 1558):
        print("encounter mobs and now flee")
        time.sleep(2)
        xp.tap(1244, 1566)
        time.sleep(1)
        delay_tap(1960, 1190)
    elif not xp.matchColor("#ABA8A3", 970, 1558):
        return False
    else:
        return True

triangle_characters_array = [1, 2, 3, 4]
triangle_skills_array = [2, 2, 2, 3]

def once_check_Battle():
    if xp.matchColor("#0D0C09", 438, 1573) and xp.matchColor("#9F9C98", 2011, 1607):
        return True
    else:
        return False
def historic_frag_farm():
    count = 0
    print("start script")
    if xp.matchColor("#F0EBE8", 535, 1545):
        print("stopped in the world")
        delay_tap(194, 1417)
        delay_tap(737, 1481)
        delay_tap(1868, 1184)
    while True:
        if xp.matchColor("#F0EBE8", 329, 146):#start game
            count = 0
            print("starting game")
            delay_tap(2722, 1489)
            time.sleep(1)
            delay_tap(733, 745)
            double_fast_tap(1947, 1363)
            while True:
                if bt_wait_Idle():
                    print("drag dicing")
                    xp.swipe(2552, 1438, 2635, 1255, 0.4)
                    time.sleep(0.4)
                    double_fast_tap(2567, 1114)
                if xp.matchColor("#020202", 366, 118):
                    xp.tap(1036, 837,13)
                    time.sleep(7)
                    break
                elif xp.matchColor("#4E4437", 1583, 1033):  # option
                    print("take an option")
                time.sleep(0.4)
                xp.tap(1652, 1081)
        if xp.matchColor("#F0EBE8", 535, 1545):#ready to dice
            dice_it(count)
        elif xp.matchColor("#4E4437", 1583, 1033):#option
            print("take an option")
            tap_Until_Disappear(option)
        elif xp.matchColor("#40382C", 764, 831):#wealth parth
            print("going to wealth")
            tap_Until_Disappear(wealth)
        elif xp.matchColor("#BDBFB4", 1398, 457) and xp.matchColor("#717367", 2173, 473): #first branch
            print("first branch")
            double_fast_tap(2493, 1448)
            double_fast_tap(1665, 847)
        elif xp.matchColor("#D8C79E", 1392, 581) and xp.matchColor("#D7C79E", 1554, 584): #second branch
            print("second branch")
            double_fast_tap(2493, 1448)
            double_fast_tap(1284, 833)
        elif xp.matchColor("#23596F", 1637, 1343):
            print("obtained")
            double_fast_tap(1637, 1343)
        elif xp.matchColor("#F4F2EF", 1039, 621) and xp.matchColor("#E4D3A1", 1157, 516) and not xp.matchColor("#23596F", 1637, 1343):
            print("last branch")
            loopcount = 0
            while True:
                if xp.matchColor("#CECCC8", 462, 1482):
                    print("stopped in the world")
                    delay_tap(194, 1417)
                    delay_tap(737, 1481)
                    delay_tap(1868, 1184)
                    time.sleep(2)
                    delay_tap(1523, 1343)
                    break
                elif onetime_wait_Battle(count):
                    print("encounter mobs and now flee")
                    time.sleep(2)
                    xp.tap(1244, 1566)
                    time.sleep(1)
                    delay_tap(1960, 1190)
                    time.sleep(2)
                    delay_tap(1523, 1343)
                    break
                print("looping")
                delay_tap(1667, 825)#going right
                delay_tap(1583, 1033)#degrade level
                loopcount += 1
                if loopcount > 10:
                    break
                time.sleep(0.3)
        elif onetime_wait_Battle(count):
            print("fight!!!!!!!!!!!!!!!!!")
            boost_Atk()
            time.sleep(0.8)
            count += 1
        elif xp.matchColor("#F0EBE8", 1176, 280) and xp.matchColor("#F0EBE8", 1760, 274): #itme obtained
            print("got item")
            tap_Until_Disappear(item_obtained)
        else:
            xp.tap(1652, 1081)
        print(count)
        time.sleep(0.3)

def triangle_secret_route():
    print("start script")
    #moloply_game_restart()
    while True:
        count = 1
        black_screen_count = 0
        if xp.matchColor("#F0EBE8", 329, 146):#start game
            print("starting game")
            delay_tap(2722, 1489)
            time.sleep(1)
            while True:
                if not xp.matchColor("#FFFFFF", 925, 739) and not xp.matchColor("#F1F1F1", 924, 770):
                    xp.tap(1118, 748)
                    print("add one ticket")
                if not xp.matchColor("#FFFFFF", 2030, 727) and not xp.matchColor("#F8F8F8", 2010, 741):#xp.matchColor("#FEFEFE", 2026, 729) and not xp.matchColor("#FCFCFC", 2030, 784):
                    xp.tap(2200, 759)
                    print("add one dificulty")
                if xp.matchColor("#D5D5D4", 927, 741) and xp.matchColor("#FFFFFF", 921, 768) and xp.matchColor("#FFFFFF", 2008, 741) and xp.matchColor("#FFFFFF", 2002, 780):#xp.matchColor("#FFFFFF", 2029, 728) and xp.matchColor("#DCDCDC", 2031, 783) and xp.matchColor("#CACACA", 920, 774):
                    double_fast_tap(1889, 1365)
                    print("enter game now")
                    time.sleep(4)
                    break
                time.sleep(0.3)
            while True:
                if not xp.matchColor("#F0EBE8", 535, 1545):#ready to dice
                    print("start holding")
                    xp.tap(1036, 837,6)
                    time.sleep(6)
                    black_screen_count += 1
                if black_screen_count > 2:
                    print("in the board now")
                    break
        elif xp.matchColor("#F0EBE8", 535, 1545):#ready to dice
            print("dice")
            dice_it(count)
        elif xp.matchColor("#180804", 311, 626) and xp.matchColor("#190E08", 396, 500):
            print("first branch")
            double_fast_tap(1489, 1102)
        elif xp.matchColor("#262648", 1500, 1159) and xp.matchColor("#0D1B16", 1573, 1441):
            print("secret branch")
            double_fast_tap(1473, 582)
        elif xp.matchColor("#326478", 1372, 1285):
            print("obtained")
            double_fast_tap(1637, 1343)
        elif once_check_Battle():
            print("enter battle")
            select_char_and_skill(triangle_characters_array, triangle_skills_array)
            boost_Atk()
            wait_Battle()
            boost_Atk()
            wait_Battle()
            boost_Atk()
        elif xp.matchColor("#6B5542", 1970, 1175) and xp.matchColor("#6F5944", 1904, 1175):
            print("last conversation")
            xp.tap(1036, 837, 6)
            time.sleep(6)
            break
        else:
            print("auto click")
            xp.tap(1652, 1081)
        time.sleep(0.3)
triangle_secret_route()



