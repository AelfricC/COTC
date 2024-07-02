import time
from xiaopy import *

# X,Y with color
Map_Proceed = ["#1E5167", 2561, 1550] #["#23586F", 2549, 1557]
Map_Ok = ["#22576E", 2022, 1213]
Comfirm_To_Rest = ["#326378", 1944, 1219]
World_Map = ["#DADAD7", 1991, 1468]
Menu = ["#EFEFEE", 2460, 1472]
Battle_Screen = ["#6D6D6D", 2870, 1597]
atk = ["#FFFFFF", 2572, 1584]
game_loc = ["#000000", 1561, 1735]
black_screen = ["#000000", 1441, 1092]
moloply_restart_confirm = ["#D3D8DA", 1809, 1207]
confirm_return_memory_book = ["#F6F6F6", 1501, 1020]
ultimate = ["#CCC3B9", 1455, 579]
pet_use = ["#3F7787", 2264, 1306]
ally = ["#EEEAE5", 1522, 1556]
divine_tap = ["#989590", 2217, 371]
confirm_beast = ["#326478", 1919, 1492]
zoom_icon = ["#171615", 2810, 1611]
battle_icon_InTower = ["#F5F6F6", 1880, 953]
battle_icon_InTower_confirm = ["#FCFCFC", 1391, 804]
# X,Y with no color
ATK = [2796, 1579]
Boost = [1989, 1580]
Escape = [1251, 1634]
Middle_Screen = [1453, 1089]
Mini_Map = [2458, 334]
Rest_OK = [1439, 1205]
battle_icon_InTower_xy = [2617, 1551]
close_window = [2846, 127]


def delay_tap(x, y):
    time.sleep(0.4)
    xp.tap(x, y)
    time.sleep(0.3)


def double_tap(x, y):
    xp.tap(x, y)
    time.sleep(0.3)
    xp.tap(x, y)


def double_fast_tap(x, y):
    xp.tap(x, y)
    time.sleep(0.3)
    xp.tap(x, y)


def tap_once_After_checking(val, input_count=-1):
    count = 0
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            time.sleep(1)
            delay_tap(x, y)
            return True
        elif count == input_count:
            break
        else:
            print(str(val) + "not found after checking, cant tap")
            time.sleep(0.5)
            count += 1


def wait_Battle():
    time.sleep(1)
    while True:
        if xp.matchColor("#FFFFFF", 2500, 1584,0.9) and xp.matchColor("#E0DCD7", 694, 1576,0.95):
            print("ready to fight now")
            return True
        else:
            time.sleep(0.7)


def escape(val=0):
    if val == 1:
        print("Died in jjc")
        double_fast_tap(1175, 964)
        double_fast_tap(1440, 724)
        tap_After_checking(confirm_return_memory_book, -1)
        return True
    if val == 2:
        print("Died in the tower")
        double_fast_tap(1175, 964)
        double_fast_tap(1440, 724)
        checking_Color(battle_icon_InTower)
        time.sleep(2)
        checking_Color(battle_icon_InTower)
    else:
        # Daily Farming
        tap_Until_Exsit(Menu, Escape)


def check_death(val):
    print("checking death")
    if xp.matchColor("#787674", 2689, 257) or xp.matchColor("#787674", 2690, 588) or xp.matchColor("#787674", 2689,
                                                                                                   913) or xp.matchColor(
            "#787674", 2690, 1244):
        print("someone died")
        escape(val)
        time.sleep(1)


def tap_Until_Exsit(val, tap_where,limit = 100):
    color, x, y = val
    x2, y2 = tap_where
    count = 0
    while True:
        if not xp.matchColor(color, x, y,0.9) and count < limit:
            xp.tap(x2, y2)  # where I should tap
            time.sleep(0.4)
            count += 1
        else:
            print("found it and stop tapping, count = " + str(count))
            time.sleep(1)
            break


def tap_After_checking(val, input_count = -1):
    count = 0
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            xp.tap(x, y)
            while True:
                if not xp.matchColor(color, x, y, 0.8):
                    print("chekced and clicked, go to proceed")
                    return True
                else:
                    xp.tap(x, y)
                    time.sleep(0.4)
                if count == input_count:
                    break
        else:
            print(str(val) + "not found after checking, cant tap")
            time.sleep(0.5)
            count += 1


def find_lv70_cat():
    ret = xp.matchColor("#151518", 266, 101, 0.9)
    if ret:
        return True
    else:
        return False


def checking_Color(val):
    color, x, y = val
    count = 0
    while True:
        if xp.matchColor(color, x, y, 0.9):
            print("checked")
            time.sleep(0.2)
            return True
        else:
            print("not there")
            count += 1
            if count > 60:
                return False  # changed from break, might impact other things???
            time.sleep(1)


def checking_color_once(val):
    color, x, y = val
    if xp.matchColor(color, x, y, 0.95):
        print("checked")
        return True


def swipe_Until_Black(va=1):
    # va = 1: left right, 2: up down
    count = 0
    flip = 1
    while True:
        if xp.matchColor("#000000", 1132, 584) and xp.matchColor("#000000", 1909, 205):
            print("black screen now and stop swiping")
            break
        else:
            if va == 1:
                if flip % 2 == 0:
                    xp.swipe(588, 1141, 1514, 701, 0.3)
                    flip += 1
                elif flip % 2 != 0:
                    xp.swipe(1514, 701, 588, 1141, 0.3)
                    flip += 1
            elif va == 2:#up down
                if flip % 2 == 0:
                    xp.swipe(1190, 380, 1235, 1295, 0.3)
                    flip += 1
                elif flip % 2 != 0:
                    xp.swipe(1235, 1295, 1190, 380, 0.3)
                    flip += 1
            time.sleep(0.3)
            count += 1
            if count >= 40:
                print("reached maximum swping")
                break



def wait_Idle():
    time.sleep(1)
    while True:
        if checking_Color(Menu):
            break
        else:
            time.sleep(0.7)


def press_until_SeeColor(val):
    time.sleep(1.5)
    count = 0
    while True:
        if checking_color_once(val):
            # if not xp.matchColor("#EEEEED", 1671, 1441, 0.8): #check menu
            print("stop pressing as I see the color")
            break
        elif count > 20:
            break
        else:
            print("keep pressing: " + str(count))
            xp.tap(ATK[0], ATK[1], 3)
            count += 1
            time.sleep(3)


def boost_Atk():
    delay_tap(Boost[0], Boost[1])  # boost
    only_atk()
    # double_tap(ATK[0],ATK[1])  # atk.


def swap():
    delay_tap(1735, 1568)  # swap


def select_char_and_skill(characters, skills, atk_mode=1, end=0, divine_beast=0):
    for char, skill in zip(characters, skills):
        select_char(char, skill)
        #if char != 4:
        select_skill(char, skill)
    if divine_beast == 1:
        divine_beast()
    if atk_mode == 1:
        only_atk()
    elif atk_mode == 2:
        boost_Atk()
    if end != 1:
        time.sleep(5)
        wait_Battle()
    else:
        time.sleep(5)


def select_char(va, skill):
    if skill[0] != 0:
        delay_tap(2570,259 + (va -1) * 336 )


def only_atk():
    tap_After_checking(atk, 50)


# skills_array = [-1,3,4,1,1]
# skills_array = [Skill location, BP, point_to skill(1-4) ,pet , pet BP,pet point to]
# swap row: -
# Ultimate:100
def select_skill(char, value):
    va = value[0]
    bp = value[1] if len(value) > 1 else 0
    point_to = value[2] if len(value) > 2 else 0
    pet = value[3] if len(value) > 3 else 0
    pet_bp = value[4] if len(value) > 4 else 0
    pet_point_to = value[5] if len(value) > 5 else 0

    skill_slot_x = 2000
    skill_slot_y = 544
    pet_skill_slot_x = 1447
    pet_skill_slot_y = 789

    #for pointing to teammate
    char_banner_x = 2570
    char_banner_y = 259

    # select pet skill first
    if pet != 0:
        if pet < 0:
            delay_tap(2558, 1544)
            time.sleep(0.5)
        delay_tap(1623, 264)
        double_tap(2107, 578)
        if pet_bp == 0 and pet > 0:
            delay_tap(2203, 1299)
        elif pet_bp >= 1:
            xp.swipe(pet_skill_slot_x, pet_skill_slot_y, pet_skill_slot_x + 235 + (pet_bp * 190),
                     pet_skill_slot_y, 0.5)
            time.sleep(0.65)
            delay_tap(2203, 1299)
        if pet_point_to != 0:
            delay_tap(char_banner_x, char_banner_y + ((pet_point_to - 1) * 336))
        wait_Battle()
        select_char(char, value)
        # do i need this twice???
    #   if va < 0:
    #       delay_tap(1951, 962)
    #       va = abs(va)
    #       time.sleep(0.5)
    # swap rows
    if va < 0:
        delay_tap(2558, 1544)
        va = abs(va)
        time.sleep(0.8)
    # normal skill selection
    # point to enemy
    if point_to > 10:
        if point_to == 31:
            double_fast_tap(495, 591)
        elif point_to == 32:
            double_fast_tap(773, 707)
        elif point_to == 33:
            double_fast_tap(998, 516)
    #####Elrica shift style
    if va > 10 and va < 20:
        double_fast_tap(2205, 178)
        time.sleep(3)
        va = va - 10
    ######Char select skill######
    if bp == 0 and va > 0 and va < 10:
        delay_tap(skill_slot_x, skill_slot_y + ((va - 1) * 247))
    elif bp >= 1 and va > 0 and va < 10:
        xp.swipe(skill_slot_x, skill_slot_y + ((va - 1) * 247), skill_slot_x + 231 + (bp * 227),
                 skill_slot_y + ((va - 1) * 247), 0.5)
        time.sleep(0.7)
    #######ultimate######
    if va == 100:# when there is pet tab
        delay_tap(1615, 290)  # open box
        delay_tap(1657, 572)  # ult window
        delay_tap(2174, 1308)  # activate
        time.sleep(0.5)
    elif va == 101: #in the tower, no pet
        delay_tap(1615, 290)  # open box
        delay_tap(2132, 1143)  # activate
        time.sleep(0.5)
    #######pointing to teammate's skill######
    if point_to > 0 and point_to < 10:
        delay_tap(char_banner_x, char_banner_y + ((point_to - 1) * 336))


# characters_array = [1, 2, 3, 4]
# skills_array = [[2,1], [2,1], [2,1], [2,1]]
# select_char_and_skill(characters_array, skills_array,1,1)

def divine_beast():
    double_fast_tap(1490, 1564)
    double_fast_tap(2256, 362)
    delay_tap(1457, 602)


def launch_game():
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")
    time.sleep(1)

def zoom_map():
    tap_once_After_checking(zoom_icon, -1)


def game_restart(va):
    xp.home()
    time.sleep(2)
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")
    if va == 1:
        tap_Until_Exsit(moloply_restart_confirm, Middle_Screen)
        tap_After_checking(moloply_restart_confirm, -1)
    elif va == 2:
        tap_Until_Exsit(Menu, Middle_Screen)


def check_here_tap_there(check_va, tap_val):
    while True:
        if checking_Color(check_va):
            print("Found color and going to tap")
            tap_once_After_checking(tap_val)
            break
        else:
            print("Can't see it yet")
            time.sleep(0.5)