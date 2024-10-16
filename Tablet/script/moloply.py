import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *
play = ["#FFFFFF", 2633, 1474]
board_idle = ["#F6F4F2", 517, 1438]
after_final_boss = ["#FFFFFF", 1391, 710]
def battle1():
    double_fast_tap(538, 666)#point left enemy
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[2,3], [4, 3], [100,0,1,1,3], [12,3]]
    select_char_and_skill(characters_array, skills_array1, 1, 1)
def battle3():
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[-4], [4, 3], [-4,3,0,1,3], [4,1]]
    skills_array2 = [[-2,3], [100], [-100,0,4], [13,3]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2, 1, 1)
def battle4():
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[-4], [4, 3], [-4,3,0,1,3], [4]]
    skills_array2 = [[2,3], [2], [100], [2,3]]
    skills_array3 = [[100], [100], [3], [1100]]
    skills_array4 = [[-2,3], [0], [-100, 0, 4,1,3,4], [2,3]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3)
    select_char_and_skill(characters_array, skills_array4, 1, 1)
def dragon_board():
    launch_game()
    battle_count = 0
    cut_scen = 0
    while True:
        if xp.matchColor("#F0EBE8", 1163, 435) and xp.matchColor("#F0EBE8", 1295, 426) and xp.matchColor("#F0EBE8", 1441, 450) and xp.matchColor("#F0EBE8", 1646, 437) and xp.matchColor("#F0EBE8", 1734, 437) and xp.matchColor("#666057", 551, 1554):
            double_fast_tap(2592, 1464)#play
            print("start adding tickets")
            while True:#putting ticket and strenth
                if xp.matchColor("#FFFFFF", 925, 743) and xp.matchColor("#FFFFFF", 953, 766) and xp.matchColor("#FFFFFF", 950, 742) and xp.matchColor("#FFFFFF", 923, 772) and xp.matchColor("#FFFFFF", 2029, 727) and xp.matchColor("#FFFFFF", 2010, 737) and xp.matchColor("#FFFFFF", 2034, 762) and xp.matchColor("#FFFFFF", 2007, 782):
                    break
                else:
                    double_fast_tap(1145, 748)
                    double_fast_tap(2199, 758)
                    double_fast_tap(1145, 748)
                    double_fast_tap(2199, 758)
                    double_fast_tap(1145, 748)
                    double_fast_tap(2199, 758)
                    double_fast_tap(1145, 748)
                    double_fast_tap(2199, 758)
                    double_fast_tap(1145, 748)
                    double_fast_tap(2199, 758)
            double_fast_tap(1820, 1381)#play the game now
            time.sleep(3)
            press_until_SeeColor(board_idle)
            print("game started")
        if xp.matchColor("#51473A", 2162, 932):#select bonus stregth
            print("select bonus stregth")
            delay_tap(1926, 1171)#next page
            time.sleep(1)
            double_fast_tap(1940, 919)#lv 4
            print("finished lv up")
        elif xp.matchColor("#FFFFFF", 2500, 1584,0.9) and xp.matchColor("#E0DCD7", 694, 1576,0.95):
            #Battle
            if battle_count == 0:
                print("1st")
                battle1()
                battle_count += 1
                time.sleep(10)
                print("finished 1st battle" + str(battle_count))
            elif battle_count == 1:
                print("2nd")
                battle1()
                battle_count += 1
                time.sleep(10)
                print("finished 2nd battle" + str(battle_count))
            elif battle_count == 2:
                print("3rd")
                battle3()
                battle_count += 1
                time.sleep(10)
            elif battle_count == 3:
                print("4th")
                battle4()
                battle_count = 0
                time.sleep(10)
        elif xp.matchColor("#F0EBE8", 1470, 300) and xp.matchColor("#F0EBE8", 1760, 297) and xp.matchColor("#F0EBE8", 1178, 293) and xp.matchColor("#F0EBE8", 1302, 302):
            #collect reward
            print("collect reward")
            double_fast_tap(1500, 1520)
        elif xp.matchColor("#D0C4B4", 1614, 725) or xp.matchColor("#D0C4B4", 816, 306) or xp.matchColor("#D0C4B4", 2188, 462) or xp.matchColor("#D0C4B4", 1552, 784) or xp.matchColor("#D0C4B4", 1552, 784):
            if cut_scen == 0:#final boss cut scen
                print("#final boss cut scen")
                press_until_SeeColor(Battle_Screen)
                cut_scen += 1
                print("cut scen =" + str(cut_scen))
            else:
                print("finishing up")
                press_until_SeeColor(after_final_boss)
                print("ok, finshed holding")
                cut_scen = 0
        elif xp.matchColor("#F0EBE8", 1120, 431) and xp.matchColor("#F0EBE8", 1542, 432) and xp.matchColor("#F0EBE8", 1828, 430):
            #final reward gained
            print("gained final reward")
            double_fast_tap(1464, 1349)
        # elif xp.matchColor("#FFF6DD", 1212, 564) and xp.matchColor("#FFEFB6", 863, 840):
        #     print("turning left")
        #     delay_tap(1022, 407)  # turn left
        #     time.sleep(2)
        else:
            time.sleep(0.3)
            xp.tap(1475, 1079)#go down
            time.sleep(0.3)
            xp.tap(2799, 1399)  # dice
            # 2267, 1477
            # 2212, 1575
            #
            # 2784, 1661
            # 2843, 1574
            time.sleep(0.3)
            xp.tap(1261, 779)  # turn left




print("start")
dragon_board()
