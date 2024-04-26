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
    skills_array1 = [[-3,3], [3], [2], [4,3]]
    skills_array2 = [[-2], [-2,3], [3], [2]]
    skills_array3 = [[2,2], [-4,2], [4,2], [1]]
    skills_array4 = [[0], [0], [2], [0]]
    while True:
        tap_After_checking(battle_icon_InTower,-1)
        tap_After_checking(battle_icon_InTower_confirm,-1)
        select_char_and_skill(characters_array, skills_array1)
        select_char_and_skill(characters_array, skills_array2)
        select_char_and_skill(characters_array, skills_array3)
        select_char_and_skill(characters_array, skills_array4,2,1)
        count += 1
        tap_Until_Exsit(battle_icon_InTower,battle_icon_InTower_xy)
        time.sleep(4)
        xp.toast("this is " + str(count))

def Elite_sword():
    print("start")
    characters_array = [1, 2, 3, 4]
    skills_array1 = [[], [], [], []]
    skills_array2 = [[], [], [], []]
    skills_array3 = [[], [], [], []]
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
tap_After_checking(battle_icon_InTower,-1)
tap_After_checking(battle_icon_InTower_confirm,-1)
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
select_char_and_skill(characters_array, skills_array20,1,1)
count += 1
tap_Until_Exsit(battle_icon_InTower,battle_icon_InTower_xy)
time.sleep(4)
xp.toast("this is " + str(count))

def Elite_fire():
    print("start")


   

if tower_name == "Master":
    Master()
elif tower_name == "Elite_sword":
    Elite_sword()
elif tower_name == "Elite_fire":
    Elite_fire()
[[], [], [], []]