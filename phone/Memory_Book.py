import time
import subprocess
from xiaopy import *
from Phone_COTC import *

# rewards = ["#FFFFFF", 1518, 1364]
rewards = ["#D8DCDE", 1507, 1366]
read = ["#EEEFF0", 2586, 697]
confirm_read = ["#F9FAFA", 1848, 1464]

# ui = xp.ui()
# Book == ui.stringValue("Book")
# if Book == "NUT":
#     nut()

def battle_wait(characters_array, skills_array):
    select_char_and_skill(characters_array, skills_array)
    only_atk()
    wait_Battle()
    if check_death(1):
        return True

def book():
    launch_game()
    print("start book")
    characters_array = [1, 2, 3, 4]
    battle_count = 0
    skills_array1 = [[1,1], [2], [2], [-4,3]]
    skills_array2 = [[-2], [-2,3], [4,2], [-4,3]]
    skills_array3 = [[-3], [-3,2], [-4,3], [-3]]
    skills_array4 = [[3], [2], [-2], [-100]]
    skills_array5 = [[2,3], [100], [100], [3]]
    skills_array6 = [[2,3], [4,3], [2,3], [-3,4]]
    # skills_array7 = [[4, 3], [2, 3], [1], [3, 3]]
    # skills_array8 = [[2, 2], [1], [0], [100]]
    while True:
        #tap_After_checking(read,20)
        double_tap(2572, 532)
        tap_After_checking(confirm_read,20)
        press_until_SeeColor(Battle_Screen)
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
        select_char_and_skill(characters_array, skills_array6)
        only_atk()
        time.sleep(15)
        # # 77777
        # if battle_wait(characters_array, skills_array7):
        #     continue
        # # 88888
        # select_char_and_skill(characters_array, skills_array8)
        # only_atk()
        # End
        press_until_SeeColor(rewards)
        battle_count += 1
        xp.toast(str(battle_count))
        tap_Until_Disappear(rewards)
        double_fast_tap(1506, 1387)

book()
# press_until_SeeColor(rewards)

#print(xp.getColor(2870, 1597))
