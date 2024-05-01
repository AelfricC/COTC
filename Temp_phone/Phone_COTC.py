import time
from xiaopy import *

# X,Y with color
Map_Proceed = ["#1E5167", 1750, 915]
Map_Ok = ["#FFFFFF", 1354, 733]
Comfirm_To_Rest = ["#FFFFFF", 1355, 730]
World_Map = ["#C9C9C7", 1478, 898]
Menu = ["#F6F6F6", 275, 862]
Battle_Screen = ["#FFFFFF", 2034, 963]
atk = ["#FFFFFF", 1893, 972]
game_loc = ["#000000", 1561, 1735]
black_screen = ["#000000", 1441, 1092]
moloply_restart_confirm = ["#D3D8DA", 1809, 1207]
confirm_return_memory_book = ["#FEFEFE", 1192, 605]
ultimate = ["#F8F8F8", 2195, 1299]
pet_use = ["#F2F3F3", 1735, 782]
ally = ["#EAE7E2", 1246, 960]
divine_tap = ["#3B566E", 1530, 533]
confirm_beast = ["#FDFEFE", 1352, 922]
zoom_icon = ["#0B0B0B", 1988, 971]
battle_icon_InTower = ["#F5F6F6", 1880, 953]
battle_icon_InTower_confirm = ["#FCFCFC", 1391, 804]
# X,Y with no color
ATK = [1954, 959]
Boost = [1589, 960]
Escape = [1087, 962]
Middle_Screen = [1251, 462]
Mini_Map = [1927, 148]
Rest_OK = [1141, 729]
battle_icon_InTower_xy = [1880, 953]


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
            print("Tapped")
            break
        elif count == input_count:
            break
        else:
            print(str(val) + "not found after checking, cant tap")
            time.sleep(0.5)
            count += 1


def wait_Battle():
    time.sleep(1)
    while True:
        if xp.matchColor("#FFFFFF", 2035, 975) and xp.matchColor("#FFFFFF", 1926, 974) and xp.matchColor("#0E0D09", 336, 966):
            print("ready to fight now")
            return True
        else:
            print("not ready to fight")
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
    if xp.matchColor("#787674", 2123, 108) or xp.matchColor("#787674", 2122, 322) or xp.matchColor("#787674", 2120,
                                                                                                   537) or xp.matchColor(
            "#787674", 2122, 753):
        print("someone died")
        escape(val)
        time.sleep(1)


def tap_Until_Exsit(val, tap_where):
    color, x, y = val
    x2, y2 = tap_where
    count = 0
    while True:
        if not xp.matchColor(color, x, y, 0.95) and count < 70:
            xp.tap(x2, y2)  # where I should tap
            time.sleep(0.5)
            count += 1
        else:
            print("found it and stop tapping")
            time.sleep(1)
            break


def tap_After_checking(val, input_count = -1):
    count = 0
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            xp.tap(x, y)
            print("Tapped")
            while True:
                if not xp.matchColor(color, x, y, 0.8):
                    print("chekced and clicked, go to proceed")
                    return
                else:
                    print("need to tap again, still can see it")
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
        if not xp.matchColor("#000000", 1135, 604):
            if va == 1:
                if flip % 2 == 0:
                    xp.swipe(941, 330, 1623, 660, 0.3)
                    flip += 1
                elif flip % 2 != 0:
                    xp.swipe(1627, 251, 809, 649, 0.3)
                    flip += 1
            elif va == 2:
                if flip % 2 == 0:
                    xp.swipe(871, 699, 871, 315, 0.3)
                    flip += 1
                elif flip % 2 != 0:
                    xp.swipe(871, 315, 871, 699, 0.3)
                    flip += 1
            time.sleep(0.4)
            count += 1
            if count >= 15:
                break
        else:
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
    delay_tap(1430, 957)  # swap


def select_char_and_skill(characters, skills, atk_mode=1, end=0, divine_beast=0):
    for char, skill in zip(characters, skills):
        select_char(char, skill)
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
        delay_tap(1937, 128 + (va - 1) * 223)


def only_atk():
    tap_After_checking(atk, 50)


# skills_array = [-1,3,4,1,1]
# skills_array = [Skill location, BP, point_to skill(1-4) ,pet , pet BP]
# swap row: -
# Ultimate:100
def select_skill(char, value):
    va = value[0]
    bp = value[1] if len(value) > 1 else 0
    point_to = value[2] if len(value) > 2 else 0
    pet = value[3] if len(value) > 3 else 0
    pet_bp = value[4] if len(value) > 4 else 0

    skill_slot_x = 1587
    skill_slot_y = 300
    pet_skill_slot_x = 1265
    pet_skill_slot_y = 457

    # select pet skill first
    if pet != 0:
        if pet < 0:
            delay_tap(1951, 962)
            time.sleep(0.5)
        delay_tap(1365, 126)
        double_tap(1631, 329)
        if pet_bp == 0 and pet > 0:
            tap_After_checking(pet_use, 10)
        elif pet_bp >= 1:
            xp.swipe(pet_skill_slot_x, pet_skill_slot_y, pet_skill_slot_x + 135 + (pet_bp * 145),
                     pet_skill_slot_y, 0.5)
            time.sleep(0.65)
            tap_After_checking(pet_use, 10)
        wait_Battle()
        select_char(char, value)
        # do i need this twice???
    #   if va < 0:
    #       delay_tap(1951, 962)
    #       va = abs(va)
    #       time.sleep(0.5)
    # swap rows
    if va < 0:
        delay_tap(1951, 962)
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
        double_fast_tap(1735, 38)
        time.sleep(3.5)
        va = va - 10
    ######Char select skill######
    if bp == 0 and va > 0 and va < 10:
        delay_tap(skill_slot_x, skill_slot_y + ((va - 1) * 162))
    elif bp >= 1 and va > 0 and va < 10:
        xp.swipe(skill_slot_x, skill_slot_y + ((va - 1) * 162), skill_slot_x + 144 + (bp * 120),
                 skill_slot_y + ((va - 1) * 162), 0.5)
        time.sleep(0.7)
    #######ultimate######
    if va == 100:
        delay_tap(1427, 118)  # open box
        double_tap(1413, 329)  # ult window
        delay_tap(1701, 695)  # activate
        time.sleep(0.5)
    elif va == 101: #in the tower, no pet
        delay_tap(1339, 124)  # open box
        delay_tap(1717, 695)  # activate
        time.sleep(0.5)
    #######pointing to teammate's skill######
    if point_to > 0 and point_to < 10:
        char_banner_x = 1974
        char_banner_y = 121
        delay_tap(char_banner_x, char_banner_y + ((point_to - 1) * 217))


# characters_array = [1, 2, 3, 4]
# skills_array = [[0], [0], [0], [-12,3]]
# select_char_and_skill(characters_array, skills_array)

def divine_beast():
    double_fast_tap(1322, 965)
    double_fast_tap(1158, 445)
    delay_tap(1428, 920)


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