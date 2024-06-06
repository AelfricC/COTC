import time
import subprocess
from xiaopy import *
from Phone_COTC import *

ui = xp.ui()
tower_name = ui.stringValue("tower_name")


def Master():
    count = 0
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[3], [3], [4,3], [4, 3]]
    skills_array2 = [[4,3], [12,3], [1], [2]]
    while True:
        tap_After_checking(battle_icon_InTower, -1)
        tap_After_checking(battle_icon_InTower_confirm, -1)
        wait_Battle()
        select_char_and_skill(characters_array, skills_array1)
        select_char_and_skill(characters_array, skills_array2, 1, 1)
        count += 1
        tap_Until_Exsit(battle_icon_InTower, battle_icon_InTower_xy)
        time.sleep(4)
        xp.toast("this is " + str(count))

def Job():
    count = 0
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[2], [2], [2], [2]]
    while True:
        tap_After_checking(battle_icon_InTower, -1)
        double_tap(1377, 666)
        tap_Until_Exsit(Battle_Screen,Middle_Screen)
        wait_Battle()
        double_fast_tap(528, 733)
        select_char_and_skill(characters_array, skills_array1,2, 1)
        count += 1
        tap_Until_Exsit(battle_icon_InTower, battle_icon_InTower_xy)
        time.sleep(9)
        xp.toast("this is " + str(count))


def Elite_1ST(): #21-x(turn =
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[-2,3], [3,3], [4,3], [-3,3]]
    skills_array2 = [[-4], [-3,3], [-101], [-4,2]]
    skills_array3 = [[2,3], [-4,3], [-4,3], [4,3]]
    skills_array4 = [[-4], [0], [-5,3], [4,1]]
    skills_array5 = [[3,3], [3,3], [5,3], [4,2]]
    skills_array6 = [[101], [-101], [101], [12,3]]
    skills_array7 = [[4], [-4,3], [101], [2,3]]
    skills_array8 = [[1], [1], [-4,3], [14]]
    skills_array9 = [[4], [3,2], [-101], [4,1]]
    skills_array10 = [[0], [101], [5,3], [4,2]]
    skills_array11 = [[0], [4,3], [-101,0,4], [12,3]]
    skills_array12 = [[3,3], [0], [-101], [14]]
    skills_array13 = [[4], [4,3], [-4,3], [4,2]]
    skills_array14 = [[0], [3], [-101], [12,3]]
    skills_array15 = [[3,3], [4], [-2,3], [14]]
    skills_array16 = [[4], [101], [-5,3], [13,1]]
    skills_array17 = [[2,3], [4,3], [-101,0,4], [2,3]]
    skills_array18 = [[-4], [4,3], [-101], [2,3]]
    skills_array19 = [[0], [1], [0], [14]]
    skills_array20 = [[1], [1], [1], [13,3]]
    tap_After_checking(battle_icon_InTower, -1)
    tap_After_checking(battle_icon_InTower_confirm, -1)
    wait_Battle()
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3)
    select_char_and_skill(characters_array, skills_array4)
    select_char_and_skill(characters_array, skills_array5)
    select_char_and_skill(characters_array, skills_array6)
    select_char_and_skill(characters_array, skills_array7)
    select_char_and_skill(characters_array, skills_array8)
    select_char_and_skill(characters_array, skills_array9)
    select_char_and_skill(characters_array, skills_array10)
    select_char_and_skill(characters_array, skills_array11)
    select_char_and_skill(characters_array, skills_array12)
    select_char_and_skill(characters_array, skills_array13)
    select_char_and_skill(characters_array, skills_array14)
    select_char_and_skill(characters_array, skills_array15)
    select_char_and_skill(characters_array, skills_array16)
    select_char_and_skill(characters_array, skills_array17)
    select_char_and_skill(characters_array, skills_array18)
    select_char_and_skill(characters_array, skills_array19)
    select_char_and_skill(characters_array, skills_array20, 1, 1)
    # tap_Until_Exsit(battle_icon_InTower, battle_icon_InTower_xy)


def Elite_2ND():
    print("start")
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[3,3], [-4,3], [4,3], [4]]
    skills_array2 = [[101], [-3,3], [-101], [12,2]]
    skills_array3 = [[4], [101], [-101,0,4], [3,3]]
    skills_array4 = [[], [], [], []]
    skills_array5 = [[], [], [], []]
    skills_array6 = [[], [], [], []]
    skills_array7 = [[], [], [], []]
    skills_array8 = [[], [], [], []]
    skills_array9 = [[], [], [], []]
    skills_array10 = [[], [], [], []]
    skills_array11 = [[], [], [], []]
    skills_array12 = [[], [], [], []]
    skills_array13 = [[], [], [], []]
    skills_array14 = [[], [], [], []]
    skills_array15 = [[], [], [], []]
    skills_array16 = [[], [], [], []]
    skills_array17 = [[], [], [], []]
    skills_array18 = [[], [], [], []]
    skills_array19 = [[], [], [], []]
    skills_array20 = [[], [], [], []]
    tap_After_checking(battle_icon_InTower, -1)
    tap_After_checking(battle_icon_InTower_confirm, -1)
    wait_Battle()
    select_char_and_skill(characters_array, skills_array1)
    select_char_and_skill(characters_array, skills_array2)
    select_char_and_skill(characters_array, skills_array3, 1, 1)
    # select_char_and_skill(characters_array, skills_array4)
    # select_char_and_skill(characters_array, skills_array5)
    # select_char_and_skill(characters_array, skills_array6)
    # select_char_and_skill(characters_array, skills_array7)
    # select_char_and_skill(characters_array, skills_array8)
    # select_char_and_skill(characters_array, skills_array9)
    # select_char_and_skill(characters_array, skills_array10)
    # select_char_and_skill(characters_array, skills_array11)
    # select_char_and_skill(characters_array, skills_array12)
    # select_char_and_skill(characters_array, skills_array13)
    # select_char_and_skill(characters_array, skills_array14)
    # select_char_and_skill(characters_array, skills_array15)
    # select_char_and_skill(characters_array, skills_array16)
    # select_char_and_skill(characters_array, skills_array17)
    # select_char_and_skill(characters_array, skills_array18)
    # select_char_and_skill(characters_array, skills_array19)
    # select_char_and_skill(characters_array, skills_array20)
    tap_Until_Exsit(battle_icon_InTower, battle_icon_InTower_xy)
    time.sleep(4)



battle_icon_InTower = ["#F5F6F6", 1880, 953]
if tower_name == "Elite_1ST" or tower_name == "Elite_2ND":
    battle_icon_InTower_confirm = ["#FCFCFC", 1391, 804]
elif tower_name == "Master":
    battle_icon_InTower_confirm = ["#EBEDEE", 1393, 718]
elif tower_name == "Job":
    battle_icon_InTower_confirm = ["#FCFCFC", 1391, 645]
launch_game()
if tower_name == "Master":
    Master()
elif tower_name == "Elite_1ST":
    Elite_1ST()
elif tower_name == "Elite_2ND":
    Elite_2ND()
elif tower_name == "Job":
    Job()