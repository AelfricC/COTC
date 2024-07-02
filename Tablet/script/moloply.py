import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *
play = ["#FEFEFE", 1362, 843]
board_idle = ["#F8F5F4", 514, 877]
after_final_boss = ["#AB8D49", 975, 504]
def battle1():
    double_fast_tap(538, 666)#point left enemy
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[13], [4, 3], [2,0,0,-1,3], [3, 3]]
    skills_array2 = [[0], [100], [0], [100]]
    skills_array3 = [[3,3], [3,3], [-100,0,1], [2,2]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3, 1, 1)
def battle2():
    double_fast_tap(440, 590)#point last left enemy
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[4], [4, 3], [2,3,0,-1,3], [3, 3]]
    skills_array2 = [[4,3], [100], [100], [100]]
    skills_array3 = [[12,3], [3,2], [-100,0,1], [2,2]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3, 1, 1)
def battle3():
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[4], [4, 3], [4,3,0,-1,3], [3, 3]]
    skills_array2 = [[12,2], [-1,3], [100], [2]]
    skills_array3 = [[3,3], [-100], [-100,0,1], [100]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3, 1, 1)
def battle4():
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[4], [4, 3], [4,3,0,-1,3], [-2, 3]]
    skills_array2 = [[4,1], [-1,3], [2], [-3,3]]
    skills_array3 = [[14,3], [-100], [100], [2,2]]
    skills_array4 = [[2,3,0,-1,3,1], [3], [-100, 0, 1], [100]]
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3)
    select_char_and_skill(characters_array, skills_array4, 1, 1)
def dragon_board():
    launch_game()
    ticket_count = 0
    strength_count = 0
    battle_count = 0
    cut_scen = 0
    while True:
        if (xp.matchColor("#D0C4B4", 793, 929) and xp.matchColor("#FEFEFE", 1890, 906)) or (xp.matchColor("#FFFFFF", 1108, 421) and xp.matchColor("#F0EBE8", 1309, 225) and xp.matchColor("#FFFFFF", 1460, 435)):
            double_fast_tap(1893, 902)#play
            print("start adding tickets")
            while True:#putting ticket and strenth
                # double_fast_tap(660, 415)
                # ticket_count = 1
                if not xp.matchColor("#FDFDFD", 791, 421) and not xp.matchColor("#FFFFFF", 773, 439):
                    double_fast_tap(911, 433)
                else:
                    ticket_count = ticket_count+ 1
                if not xp.matchColor("#F9F9F9", 1500, 413) and not xp.matchColor("#E2E2E2", 1481, 446) and not xp.matchColor("#E4E4E4", 1503, 438):
                    double_fast_tap(1608, 432)
                else:
                    strength_count = strength_count + 1
                if strength_count > 0 and ticket_count > 0:
                    ticket_count = 0
                    strength_count = 0
                    break
            tap_once_After_checking(play)
            time.sleep(3)
            press_until_SeeColor(board_idle)
            print("game started")
        if xp.matchColor("#51473A", 1518, 690):#select bonus stregth
            print("select bonus stregth")
            delay_tap(1509, 677)#next page
            time.sleep(1)
            delay_tap(1400, 529)#lv 4
            print("finished lv up")
        elif xp.matchColor("#090908", 335, 967, 0.8) and xp.matchColor("#FFFFFF", 2034, 967, 0.95):
            #Battle
            if battle_count == 0:
                print("1st")
                battle1()
                battle_count += 1
                time.sleep(10)
                print("finished 1st battle" + str(battle_count))
            elif battle_count == 1:
                print("2nd")
                battle2()
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
        elif xp.matchColor("#5A709F", 551, 650) and xp.matchColor("#AA5F50", 550, 490) and xp.matchColor("#AB8D49", 551, 331):
            #collect reward
            print("collect reward")
            double_fast_tap(1157, 940)
        elif xp.matchColor("#CFC3B2", 1528, 443) or xp.matchColor("#D0C4B4", 1898, 199) or xp.matchColor("#D0C4B4", 1454, 181):
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
        elif xp.matchColor("#AB8D49", 743, 387) and xp.matchColor("#AA5F50", 738, 462) and xp.matchColor("#5A709F", 745, 535):
            #final reward gained
            print("gained final reward")
            double_fast_tap(1142, 827)
        # elif xp.matchColor("#FFF6DD", 1212, 564) and xp.matchColor("#FFEFB6", 863, 840):
        #     print("turning left")
        #     delay_tap(1022, 407)  # turn left
        #     time.sleep(2)
        else:
            time.sleep(0.3)
            xp.tap(1136, 326)#turn up
            time.sleep(0.3)
            xp.tap(1782, 860)  # dice
            time.sleep(0.3)
            xp.tap(1007, 432)  # turn left
            time.sleep(0.3)




print("start")
dragon_board()
