import time
import subprocess
from xiaopy import *
from Phone_COTC import *

# rewards = ["#FFFFFF", 1518, 1364]
rewards = ["#ECEEEF", 1238, 830]
read = ["#EEEFF0", 2586, 697]
confirm_read = ["#F9FAFA", 1848, 1464]

# ui = xp.ui()
# Book == ui.stringValue("Book")
# if Book == "NUT":
#     nut()

def battle_wait(characters_array, skills_array, beast = 0):
    select_char_and_skill(characters_array, skills_array)
    if beast != 0:
        divine_beast()
    only_atk()
    time.sleep(10)
    wait_Battle()
    if check_death(1):
        return True

def book():
    launch_game()
    print("start book")
    characters_array = [1, 2, 3, 4]
    battle_count = 0
    skills_array1 = [[-2,3], [2,0,0,-1,3], [-4,3], [2]]
    skills_array2 = [[-3], [0], [-3,3], [0]]
    skills_array3 = [[0], [3,0,32], [2], [0]]
    skills_array4 = [[3,2], [2,0,31], [-100], [4,2]]
    skills_array5 = [[3,3], [-100,0,1], [-4,3,32], [2,3,33]]
    skills_array6 = [[0], [-2,0,33], [-4,3], [0]]
    skills_array7 = [[0], [2,0,32], [3,0], [0]]
    skills_array8 = [[0], [2,0,33], [-100], [100,0,0,-1,1]]
    skills_array9 = [[3,3,0,1], [100], [4,3,31], [2,3,31]]
    while True:
        #tap_After_checking(read,20)
        double_tap(1839, 270)
        double_fast_tap(1321, 894)
        # tap_After_checking(confirm_read,20)
        press_until_SeeColor(Battle_Screen)
        double_fast_tap(487, 584)
        #111111111111111111111111111
        if battle_wait(characters_array, skills_array1):
            continue
        #22222222222222222222222222
        if battle_wait(characters_array, skills_array2):
            continue
        # 33333333333333333
        if battle_wait(characters_array, skills_array3):
            continue
        # 4444444444444444444444444
        if battle_wait(characters_array, skills_array4):
            continue
        # 55555555555555555
        if battle_wait(characters_array, skills_array5):
            continue
        # 66666666666666666666666
        if battle_wait(characters_array, skills_array6):
            continue
        # # 7777777777
        if battle_wait(characters_array, skills_array7):
            continue
        # 888888888888888
        if battle_wait(characters_array, skills_array8,1):
            continue
        # 999999999999
        select_char_and_skill(characters_array, skills_array9)
        only_atk()
        time.sleep(15)
        # End
        press_until_SeeColor(rewards)
        battle_count += 1
        xp.toast(str(battle_count))
        tap_Until_Disappear(rewards)
        double_fast_tap(1214, 607)

book()
# press_until_SeeColor(rewards)

#print(xp.getColor(2870, 1597))