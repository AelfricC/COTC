import time
from xiaopy import *

#X,Y with color
Map_Proceed = []
Map_Ok = []
Enter_Holtel = []
Tap_Host = []
Comfirm_To_Rest = []
World_Map = []
Menu = ["#EEEEED", 1671, 1441]
Battle_Screen = []

#X,Y with no color
Mini_Map = []
Wild_Loc = []
Town_Loc = []
Monster_Loc = []
Middle_Screen = []



def delay_tap(x,y):
    time.sleep(0.5)
    xp.tap(x,y)
    time.sleep(0.5)

def double_tap(x,y):
    delay_tap(x,y)
    delay_tap(x,y)

def select_char(va):
    if va == 1:
        delay_tap(2570, 259)
    elif va == 2:
        delay_tap(2638, 521)
    elif va == 3:
        delay_tap(2653, 920)
    elif va == 4:
        delay_tap(2736, 1241)

def select_skill(va):
    if va == 2:
        delay_tap(1696, 778)
    elif va == 3:
        delay_tap(1803, 1020)
    elif va == 4:
        delay_tap(1748, 1273)
    elif va == 5:
        delay_tap(1747, 1496)
    elif va == 1:
        delay_tap(1775, 551)

def select_char_and_skill(characters, skills):
    for char, skill in zip(characters, skills):
        select_char(char)
        select_skill(skill)

def Tap_After_checking(val):
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            # while True:
            delay_tap(x,y)
            print("Tapped")
                  # if not xp.matchColor(color, x, y, 0.8):
                  #       print("cant see it anymore")
                  #       break
        else:
            time.sleep(1)

def escape():
    while True:
        if not Checking_Color(Menu):  # menu location
            delay_tap(1261, 1571)
        else:
            break
        
def tap_until_finishBattle():
    count = 0
    while count < 50:
        if not Checking_Color(Menu):  # menu location
            xp.tap(1785, 671)  # middle of the screen
            time.sleep(0.5)
            count += 1
            print(count)
        else:
            break
        
                
def Tap_Until_Exsit(val,tap_where):
    color, x, y = val
    x2,y2 = tap_where
    count = 0
    while True:
        if not xp.matchColor(color, x, y, 0.8) and count < 70:
            xp.tap(x2,y2) #middle of screen 
            time.sleep(0.5)
            count += 1
        else:
            print("found it and stop tapping")
            time.sleep(1.5)
            break
        
def Tap_Until_Disappear(val):
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            xp.tap(x, y)
            time.sleep(0.4)
        else:
            print("disappeared and stop tapping")
            time.sleep(1.5)
            break
        
def Checking_Color(val):
    color, x, y = val
    while True:
        if xp.matchColor(color, x, y, 0.8):
            print("checked")
            time.sleep(1.5)
            return True
        else:
            print("not there")
            time.sleep(1)

def wait_Battle():
    time.sleep(2)
    while True:
        #if not xp.matchColor("#250209", 187, 1496, 0.8):  # bottom left red
        if not Checking_Color(Battle_Screen):
            time.sleep(1)
            print("not ready to fight")
        else:
            print("ready to fight now")
            time.sleep(1.5)
            break
        
def wait_Idle():
    time.sleep(2)
    while True:
        if not Checking_Color(Menu):
        #if not xp.matchColor("#EEEEED", 1671, 1441, 0.8): #check menu
            print("not yet back to world")
            time.sleep(1)
        else:
            print("in the world now")
            time.sleep(1.5)
            break
        
def Boost_Atk():
    delay_tap(1994, 1562)#boost
    double_tap(2361, 1551)#atk.

def swap():
    delay_tap(1743, 1563)#swap


def Locate_Wild():
    time.sleep(6)
    Tap_After_checking(Map_Proceed)  # proceed
    Tap_After_checking(Map_Ok)  # ok
    time.sleep(10)
    xp.toast("进入旅店")
    Tap_After_checking(Enter_Holtel)  # enter hotel
    time.sleep(7)
    xp.toast("点击旅店老板")
    Tap_Until_Disappear(Tap_Host)  # click host
    Tap_Until_Exsit(Comfirm_To_Rest,Middle_Screen)
    xp.toast("ok to rest")
    Tap_Until_Disappear(Comfirm_To_Rest)
    xp.toast("ok")
    Tap_Until_Exsit(Menu,Middle_Screen)
    xp.toast("open world map")
    Tap_Until_Disappear(World_Map)
    double_tap(203, 691)  # tap Hell type
    double_tap(Wild_Loc[0],Wild_Loc[1])  # tap wild
    Tap_After_checking(Map_Proceed)  # proceed
    Tap_After_checking(Map_Ok)  # ok
    # arrive wild
    Checking_Color(Menu)
    xp.toast("open mini map") 
    delay_tap(Mini_Map[0],Mini_Map[1]) #open mini map
    delay_tap(Monster_Loc[0],Monster_Loc[1])  # farm location
    time.sleep(4)