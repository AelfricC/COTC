import time
from xiaopy import *


# X,Y with color
Map_Proceed = ["#1E5167", 1750, 915] #["#23586F", 2549, 1557]
Map_Ok = ["#FFFFFF", 1354, 733]
Enter_Holtel = ["#FFFFFF", 1145, 309]
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
# X,Y with no color
ATK = [1954, 959]
Boost = [1589, 960]
Escape = [1087, 962]
Middle_Screen = [1098, 474]
Mini_Map = [1927, 148]
Rest_OK = [1141, 729]

#farm const
Tap_Host = ["#F6F6F6", 275, 862]
Wild_Loc = [1188, 205]
Town_Loc = [433, 948]
Monster_Loc = [893, 422]
Arrive_In_Sec = 4.5

def delay_tap(x, y):
    time.sleep(0.4)
    xp.tap(x, y)
    time.sleep(0.3)


def double_tap(x, y):
    xp.tap(x, y)
    time.sleep(0.3)
    xp.tap(x, y)

def double_fast_tap(x,y):
    count = 0
    while True:
        if count < 3:
            xp.tap(x, y)
            time.sleep(0.3)
            count += 1
        else:
            break
def tap_After_checking(val,input_count):
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
                    time.sleep(0.3)
        elif count == input_count :
            break
        else:
            print(str(val) + "not found after checking, cant tap")
            time.sleep(0.5)
            count += 1
def tap_once_After_checking(val,input_count):
    count = 0
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            time.sleep(1)
            xp.tap(x, y)
            print("Tapped")
            break
        elif count == input_count :
            break
        else:
            print(str(val) + "not found after checking, cant tap")
            time.sleep(0.5)
            count += 1
def wait_Battle():
    time.sleep(1)
    count = 0
    while True:
        if checking_Color(Battle_Screen):
            print("ready to fight now")
            return True
        elif count >= 2:
            return False
        else:
            print("not ready to fight")
            time.sleep(0.7)



def escape(val = 0):
    if val == 1:
        print("jjc")
        double_fast_tap(1175, 964)
        double_fast_tap(1440, 724)
        tap_After_checking(confirm_return_memory_book,-1)
        return True
    else:
        tap_Until_Exsit(Menu,Escape)
def check_death(val):
    print("checking death")
    if xp.matchColor("#787674", 2123, 108) or xp.matchColor("#787674", 2122, 322) or xp.matchColor("#787674", 2120,537) or xp.matchColor("#787674", 2122, 753):
        print("someone died")
        if val == 1:
            escape(val)
            time.sleep(1.5)
            return True


def tap_until_finishBattle():
    count = 0
    while count < 150:
        if not checking_Color(Menu):  # menu location
            xp.tap(1785, 671)  # middle of the screen
            time.sleep(0.5)
            count += 1
            print(count)
        else:
            break


def tap_Until_Exsit(val, tap_where):
    color, x, y = val
    x2, y2 = tap_where
    count = 0
    while True:
        if not xp.matchColor(color, x, y,0.95) and count < 70:
            xp.tap(x2, y2)  # middle of screen
            time.sleep(0.5)
            count += 1
        else:
            print("found it and stop tapping")
            time.sleep(1.2)
            break


def tap_Until_Disappear(val):
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.9):
            xp.tap(x, y)
            time.sleep(0.4)
        else:
            print("disappeared and stop tapping")
            time.sleep(0.5)#was 1
            break

def find_lv70_cat():
    ret = xp.matchColor("#151518", 266, 101,0.9)
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
                break
            time.sleep(1)

def checking_color_once(val):
    color, x, y = val
    if xp.matchColor(color, x, y,0.95):
        print("checked")
        return True

def swipe_Until_Black(va = 1):
    #va = 1: left right, 2: up down
    count = 0
    flip = 1
    while True:
        if not xp.matchColor("#000000", 1239, 427):
            if flip % 2 == 0 and va == 1:
                xp.swipe(941, 330,1623, 660,0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            elif flip % 2 != 0 and va == 1:
                xp.swipe(1627, 251, 809, 649, 0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            elif flip % 2 == 0 and va == 2:
                xp.swipe(871, 699,871, 315,0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            elif flip % 2 != 0 and va == 2:
                xp.swipe(871, 315, 871, 699, 0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            time.sleep(0.4)
        elif count > 30:
            game_restart(2)
            # time.sleep(0.5)
            # delay_tap(Town_Loc[0],Town_Loc[1])  # tap town
            local_mat_farm()
        else:
            time.sleep(0.4)
            break


def wait_Idle():
    time.sleep(1)
    while True:
        if checking_Color(Menu):
            print("in the world now")
            break
        else:
            print("not yet back to world")
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
    delay_tap(Boost[0],Boost[1])  # boost
    double_tap(ATK[0],ATK[1])  # atk.


def swap():
    delay_tap(1430, 957)  # swap

def wait_BlackScreen():
    if xp.matchColor("#000000", 1429, 1128,1):
        time.sleep(1)
        print("waiting")
    else:
        wait_Idle()
def select_char_and_skill(characters, skills):
    for char, skill in zip(characters, skills):
        select_char(char,skill)
        select_skill(char,skill)

def select_char(va,skill):
    if skill[0] != 0:
        delay_tap(1937,128 + (va -1) * 223 )

def only_atk():
    tap_After_checking(atk,50)
# skills_array = [-1,3,4,1,1]
# skills_array = [Skill location, BP, point_to skill(1-4) ,pet , pet BP]
# swap row: -
# Ultimate:100
def select_skill(char,value):
    skill_slot_x = 1587
    skill_slot_y = 300
    pet_skill_slot_x = 1265
    pet_skill_slot_y = 457

    va = value[0]
    bp = value[1] if len(value) > 1 else 0
    point_to = value[2] if len(value) > 2 else 0
    pet = value[3] if len(value) > 3 else 0
    pet_bp = value[4] if len(value) > 4 else 0

    #select pet skill first
    if pet != 0:
        if pet < 0:
            delay_tap(1951, 962)
            time.sleep(0.5)
        delay_tap(1365, 126)
        double_tap(1631, 329)
        if pet_bp == 0 and pet > 0:
            tap_After_checking(pet_use,10)
        elif pet_bp >= 1:
            xp.swipe(pet_skill_slot_x, pet_skill_slot_y, pet_skill_slot_x + 135 + (pet_bp * 145),
                     pet_skill_slot_y, 0.5)
            time.sleep(0.65)
            tap_After_checking(pet_use, 10)
        wait_Battle()
        select_char(char, value)
        if va < 0:
            delay_tap(1951, 962)
            va = abs(va)
            time.sleep(0.5)
    #swap rows
    if va < 0:
        delay_tap(1951, 962)
        va = abs(va)
        time.sleep(0.8)
    #normal skill selection
    #point to enemy
    if point_to > 10:
        if point_to == 31:
            double_fast_tap(495, 591)
        elif point_to == 32:
            double_fast_tap(773, 707)
        elif point_to == 33:
            double_fast_tap(998, 516)
    if bp == 0 and va > 0 and va < 10:
        delay_tap(skill_slot_x,skill_slot_y + ((va - 1)  * 162))
    elif bp >= 1 and va > 0 and va < 10:
        xp.swipe(skill_slot_x,skill_slot_y + ((va - 1) * 162),skill_slot_x + 144 + (bp * 120),skill_slot_y + ((va - 1) * 162),0.5)
        time.sleep(0.7)
    #ultimate
    if va == 100:
        delay_tap(1427, 118)#open box
        double_tap(1413, 329)#ult window
        delay_tap(1791, 782)#activate
        # tap_After_checking(ultimate,20)
        # delay_tap(1593, 265)
        time.sleep(0.5)
        # delay_tap(2168, 1140)
    #pointing to teammate's skill
    if point_to > 0 and point_to < 10:
        char_banner_x = 1974
        char_banner_y = 121
        delay_tap(char_banner_x,char_banner_y + ((point_to - 1) * 217))

# characters_array = [1, 2, 3, 4]
# skills_array = [[2], [2], [1], [1]]
# select_char_and_skill(characters_array, skills_array)

def divine_beast():
    double_fast_tap(1322, 965)
    double_fast_tap(1158, 445)
    delay_tap(1428, 920)
def launch_game():
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")
def zoom_map():
    tap_once_After_checking(zoom_icon,-1)
def game_restart(va):
    xp.home()
    time.sleep(2)
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")
    if va == 1:
        tap_Until_Exsit(moloply_restart_confirm, Middle_Screen)
        tap_After_checking(moloply_restart_confirm,-1)
    elif va == 2:
        tap_Until_Exsit(Menu, Middle_Screen)
def check_any_of_this(positions,count = 0):
    clickcount = 0
    if count != 0:
        clickcount = len(positions) - count
    while clickcount < len(positions):
        for position in positions:
            color, x, y = position
            if xp.matchColor(color, x, y,0.9):
                print("tap "+str(position))
                xp.tap(x,y)
                time.sleep(0.7)
                clickcount += 1
                print("count = "+str(clickcount))
            elif clickcount == len(positions):
                break
            else:
                print("found nothing " + str(position))
                time.sleep(0.4)
def Locate_Wild():
    #time.sleep(6)
    double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    print("procced, gonna click ok to tele")
    tap_After_checking(Map_Ok,15)  # ok
    wait_Idle()
    tap_Until_Disappear(Enter_Holtel)  # enter hotel
    print("Enter hotel")
    wait_Idle()
    print("Tap the host")
    double_fast_tap(1213, 426)
    time.sleep(2)
    tap_Until_Exsit(Comfirm_To_Rest, Middle_Screen)
    print("ok to rest")
    tap_Until_Disappear(Comfirm_To_Rest)
    print("ok")
    tap_Until_Exsit(Menu, Rest_OK)
    print("open world map")
    tap_Until_Disappear(World_Map)
    ##### for brilliant weapon
    print("zoom map")
    zoom_map()
    time.sleep(0.5)
    print("swipe")
    xp.swipe(1726, 258, 1029, 637, 0.5)
    time.sleep(0.5)
    delay_tap(Wild_Loc[0], Wild_Loc[1])  # tap wild
    double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    tap_After_checking(Map_Ok,15)  # ok
    checking_Color(Menu)
    print("open mini map")
    delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    delay_tap(1068, 335)  # get into gate
    wait_Idle()
    delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    delay_tap(643, 423)
    wait_Idle()
    double_fast_tap(1134, 502)
    double_fast_tap(1370, 645)
    wait_Idle()
    ##### for brilliant weapon
    # delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    # delay_tap(Monster_Loc[0], Monster_Loc[1])  # farm location
    # time.sleep(Arrive_In_Sec)

def run_script_battle(characters_array, skills_array,round_per_recover):
    launch_game()
    time.sleep(0.8)
    Locate_Wild()
    battle_count = 0
    cait_encounter_count = 0
    while True:
        common_encounter_count = 0
        while True:
            print("swping")
            swipe_Until_Black(2)
            wait_Battle()
            if not xp.matchColor("#1A5175", 252, 107,0.8):#find_lv70_cat():
                print("found cait!")
                escape()
                # cait_encounter_count += 1
                # if common_encounter_count > 0:
                #     common_encounter_count -= 1
                # swap()
                # boost_Atk()
                # time.sleep(10)
                # wait_Battle()
                # print("fight 2nd roung")
                # swap()
                # boost_Atk()
                # time.sleep(5)
                # wait_Battle()
                # swap()
                # boost_Atk()
                # tap_Until_Exsit(Menu, ATK)
                # print("finish battle")
            else:
                print("start battle")
                # select_char_and_skill(characters_array, skills_array)
                delay_tap(1943, 118)
                delay_tap(1416, 781)
                boost_Atk()
                common_encounter_count += 1
                battle_count += 1
                print("start clicking until finsh battle")
                tap_Until_Exsit(Menu, ATK)
                print("finish battle")
            xp.toast("normal " + str(battle_count) + "  " + "Cait: " + str(cait_encounter_count))
            if common_encounter_count == round_per_recover:
                break
            if common_encounter_count == 1:
                print("open mini map")
                delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
                delay_tap(Monster_Loc[0], Monster_Loc[1])  # farm location
                time.sleep(2)
        # return to hotel
        tap_Until_Disappear(World_Map)
        # delay_tap(224, 452)  # tap world type
        time.sleep(0.5)
        zoom_map()
        delay_tap(Town_Loc[0],Town_Loc[1])  # tap town
        Locate_Wild()

def local_mat_farm():
    launch_game()
    characters_array = [1, 2, 0, 0]
    skills_array1 = [[4], [4, 0, 1], [0], [0]]  # recover
    skills_array2 = [[4], [3, 0], [0], [0]]  # abosorb
    battle_count = 0
    cait_encounter_count = 0
    while True:
        print("swping")
        swipe_Until_Black()
        print("stop siwping")
        wait_Battle()
        if find_lv70_cat():
            boost_Atk()
            # wait_Battle()
            time.sleep(10)
            wait_Battle()
            print("fight 2nd roung")
            swap()
            boost_Atk()
            time.sleep(10)
            wait_Battle()
            boost_Atk()
            tap_Until_Exsit(Menu, ATK)
            cait_encounter_count += 1
            print("finish battle")
        else:
            if battle_count % 3 == 0:
                select_char_and_skill(characters_array, skills_array2) #absorb
                boost_Atk()
            else:
                select_char_and_skill(characters_array, skills_array1) #recover
                boost_Atk()
            battle_count += 1
            print("start clicking until finsh battle")
            tap_Until_Exsit(Menu, ATK)
            print("finish battle")
        xp.toast("normal " + str(battle_count) + "  " + "Cait: " + str(cait_encounter_count))