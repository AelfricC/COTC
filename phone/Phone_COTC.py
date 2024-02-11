import time
from xiaopy import *


# X,Y with color
Map_Proceed = ["#1E5167", 2561, 1550] #["#23586F", 2549, 1557]
Map_Ok = ["#22576E", 2022, 1213]
Enter_Holtel = ["#FFFFFF", 1494, 643]
Enter_Holtel_hell = ["#FFFFFF", 1494, 643]
Comfirm_To_Rest = ["#326378", 1944, 1219]
World_Map = ["#DADAD7", 1991, 1468]
Menu = ["#EFEFEE", 2460, 1472]
Battle_Screen = ["#6D6D6D", 2870, 1597]
# Battle_Screen = ["#B8B7B2", 452, 1572]
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
# X,Y with no color
ATK = [2796, 1579]
Boost = [1989, 1580]
Escape = [1251, 1634]
Middle_Screen = [1453, 1089]
Mini_Map = [2458, 334]
Rest_OK = [1439, 1205]

#farm const
Tap_Host = ["#EEE6DD", 1780, 724]
Wild_Loc = [1441, 722]
Town_Loc = [1463, 1117]
Monster_Loc = [1105, 697]
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
def select_char_and_skill(characters, skills):
    for char, skill in zip(characters, skills):
        select_char(char,skill)
        select_skill(char,skill)

def select_char(va,skill):
    if skill[0] != 0:
        delay_tap(2570,259 + (va -1) * 336 )

def only_atk():
    tap_After_checking(atk,50)
def select_skill(char,value):
    va = value[0]
    bp = value[1] if len(value) > 1 else 0
    pet = value[2] if len(value) > 2 else 0
    pet_bp = value[3] if len(value) > 3 else 0
    skill_slot_x = 2000
    skill_slot_y = 544
    pet_skill_slot_x = 1447
    pet_skill_slot_y = 789
    if va < 0:
        delay_tap(2563, 1557)
        time.sleep(0.5)
    if pet > 0:
        delay_tap(1621, 270)
        if pet_bp == 0 and pet > 0:
            tap_After_checking(pet_use,10)
        elif pet_bp >= 1:
            xp.swipe(pet_skill_slot_x, pet_skill_slot_y, pet_skill_slot_x + 235 + (pet_bp * 190),
                     pet_skill_slot_y, 0.5)
            tap_After_checking(pet_use, 10)
        time.sleep(2)
        select_char(char, value)
        if va < 0:
            delay_tap(2563, 1557)
            va = abs(va)
            time.sleep(0.5)
    if bp == 0 and va > 0:
        delay_tap(skill_slot_x,skill_slot_y + ((va - 1)  * 247))
    elif bp >= 1 :
        xp.swipe(skill_slot_x,skill_slot_y + ((va - 1) * 247),skill_slot_x + 231 + (bp * 190),skill_slot_y + ((va - 1) * 247),0.5)
        time.sleep(0.7)
    if va == 100:
        tap_After_checking(ultimate,20)
        delay_tap(1593, 265)
        time.sleep(0.5)
        delay_tap(2168, 1140)
# characters_array = [1, 2, 3, 4]
# skills_array = [[-1,3,1], [2,2], [2,1], [1,0]]
# select_char_and_skill(characters_array, skills_array)

def divine_beast():
    tap_After_checking(ally,-1)
    tap_After_checking(divine_tap,-1)
    double_fast_tap(1534, 551)
    tap_After_checking(confirm_beast,-1)


def escape(val):
    if val == 1:
        print("jjc")
        double_fast_tap(1259, 1575)
        double_fast_tap(1900, 1207)
        tap_After_checking(confirm_return_memory_book,-1)
        return True
    else:
        tap_Until_Exsit(Menu,Escape)
def check_death(val):
    if xp.matchColor("#787674", 2689, 257) or xp.matchColor("#787674", 2690, 588) or xp.matchColor("#787674", 2689, 913) or xp.matchColor("#787674", 2690, 1244):
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
        if not xp.matchColor(color, x, y, 0.9) and count < 70:
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
    ret = xp.matchColor("#701F1F", 1366, 247,1)
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

def swipe_Until_Black():
    count = 0
    flip = 1
    while True:
        if not xp.matchColor("#000000", 1469, 1000):
            if flip % 2 == 0:
                xp.swipe(588, 1141,1514, 701,0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            else:
                xp.swipe(1514, 701, 588, 1141, 0.3)
                # time.sleep(0.3)
                flip += 1
                count += 1
            time.sleep(0.4)
        elif count > 30:
            game_restart(2)
            tap_Until_Disappear(World_Map)
            time.sleep(0.5)
            delay_tap(Town_Loc[0],Town_Loc[1])  # tap town
            run_script_battle()
        else:
            time.sleep(0.4)
            break
def wait_Battle():
    time.sleep(1)
    while True:
        if checking_Color(Battle_Screen):
            print("ready to fight now")
            return True
        else:
            print("not ready to fight")
            time.sleep(0.7)


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
            xp.tap(Middle_Screen[0], Middle_Screen[1], 3)
            count += 1
            time.sleep(3)
def boost_Atk():
    delay_tap(Boost[0],Boost[1])  # boost
    double_tap(ATK[0],ATK[1])  # atk.


def swap():
    delay_tap(1743, 1563)  # swap

def wait_BlackScreen():
    if xp.matchColor("#000000", 1429, 1128,1):
        time.sleep(1)
        print("waiting")
    else:
        wait_Idle()

def launch_game():
    xp.launchApp("com.square_enix.android_googleplay.octopathw", "com.epicgames.ue4.SplashActivity")

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
    tap_Until_Disappear(Tap_Host)  # click host
    tap_Until_Exsit(Comfirm_To_Rest, Middle_Screen)
    print("ok to rest")
    tap_Until_Disappear(Comfirm_To_Rest)
    print("ok")
    tap_Until_Exsit(Menu, Rest_OK)
    print("open world map")
    tap_Until_Disappear(World_Map)
    delay_tap(203, 691)  # tap Hell type
    delay_tap(Wild_Loc[0], Wild_Loc[1])  # tap wild
    double_fast_tap(Map_Proceed[1],Map_Proceed[2])  # proceed
    tap_After_checking(Map_Ok,15)  # ok
    # arrive wild
    checking_Color(Menu)
    print("open mini map")
    delay_tap(Mini_Map[0], Mini_Map[1])  # open mini map
    delay_tap(Monster_Loc[0], Monster_Loc[1])  # farm location
    time.sleep(Arrive_In_Sec)

def run_script_battle(characters_array, skills_array,round_per_recover):
    launch_game()
    Locate_Wild()
    battle_count = 0
    cait_encounter_count = 0
    while True:
        common_encounter_count = 0
        while True:
            print("swping")
            swipe_Until_Black()
            wait_Battle()
            if find_lv70_cat():
                print("found cait!")
                cait_encounter_count += 1
                if common_encounter_count > 0:
                    common_encounter_count -= 1
                swap()
                boost_Atk()
                #wait_Battle()
                time.sleep(10)
                wait_Battle()
                print("fight 2nd roung")
                swap()
                boost_Atk()
                tap_Until_Exsit(Menu, ATK)
                print("finish battle")
            else:
                print("start battle")
                select_char_and_skill(characters_array, skills_array)
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
        delay_tap(Town_Loc[0],Town_Loc[1])  # tap town
        Locate_Wild()
