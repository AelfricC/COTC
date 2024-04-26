import time
import subprocess
from xiaopy import *
from Phone_COTC import *


ui = xp.ui()
tower_name = ui.stringValue("tower_name")

battle = ["#F5F6F6", 1880, 953]
battle_xy = [1880, 953]
battle_confirm = ["#FEFEFE", 1392, 721]
def Master():
    count = 0
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[-3,3], [3], [2], [4,3]]
    skills_array2 = [[-2], [-2,3], [3], [2]]
    skills_array3 = [[2,2], [-4,2], [4,2], [1]]
    skills_array4 = [[0], [0], [2], [0]]
    while True:
        tap_After_checking(battle,-1)
        tap_After_checking(battle_confirm,-1)
        wait_Battle()
        select_char_and_skill(characters_array, skills_array1)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array2)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array3)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array4)
        boost_Atk()
        time.sleep(10)
        count += 1
        tap_Until_Exsit(battle,battle_xy)
        time.sleep(4)
        xp.toast("this is " + str(count))

def Elite_sword():
    count = 0
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[2,3], [4], [3,3], [-4,3]]
    skills_array2 = [[4], [4,1], [-4], [-3]]
    skills_array3 = [[3], [4,2], [0], [2,3]]
    skills_array4 = [[1], [13,3], [3,3], [4]]
    skills_array5 = [[2,3], [12], [4], [-4,3]]
    skills_array6 = [[1], [4], [0], [-3]]
    skills_array7 = [[0], [13,1], [0], [2,3]]
    skills_array8 = [[0], [3,3], [3, 3], [0]]
    skills_array9 = [[2,3], [12], [4], [1,3]]
    skills_array10 = [[0], [-1], [2], [-4,3]]
    skills_array11 = [[0], [0], [1], [3]]
    skills_array12 = [[3], [4], [2], [-3]]
    skills_array13 = [[2,3], [13,3], [3,3], [2,3]]
    skills_array14 = [[4], [12], [4], [-4,3]]
    skills_array15 = [[1], [0], [0], [0]]
    skills_array16 = [[100], [100], [100], [-3]]
    skills_array17 = [[2,3], [13,3], [4,2], [2,3]]
    skills_array18 = [[1], [3,2], [4,3], [2,2]]
    skills_array19 = [[4], [14], [0], [100]]
    skills_array20 = [[1], [13,3], [4,3], [2,3]]
    while True:
        tap_After_checking(battle,-1)
        tap_After_checking(battle_confirm,-1)
        wait_Battle()
        select_char_and_skill(characters_array, skills_array1)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array2)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array3)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array4)
        only_atk()
        select_char_and_skill(characters_array, skills_array5)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array6)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array7)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array8)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array9)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array10)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array11)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array12)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array13)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array14)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array15)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array16)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array17)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array18)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array19)
        only_atk()
        wait_Battle()
        select_char_and_skill(characters_array, skills_array20)
        only_atk()
        time.sleep(10)
        count += 1
        tap_Until_Exsit(battle,battle_xy)
        time.sleep(4)
        xp.toast("this is " + str(count))

if tower_name == "Master":
    Master()
elif tower_name == "Elite_sword":
    Elite_sword()
