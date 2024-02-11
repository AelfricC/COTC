
import time
import subprocess
from xiaopy import *
from cotc import COTC


def delay_tap(x,y):
    time.sleep(1)
    xp.tap(x,y)
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
def press_until_Start:
    while True:
        if not xp.matchColor("#250209", 187, 1496, 1):  # bottom left red
            xp.tap(x, y,5)#anywhere middle
            time.sleep(1)
        else:
            break
def wait_Battle():
    time.sleep(1)
    while True:
        if not xp.matchColor("#250209", 187, 1496, 1):  # bottom left red
            time.sleep(1)
        else:
            time.sleep(1)
            break
def wait_Idle():
    while True:
        if not xp.matchColor("#EEEEED", 1671, 1441, 1): #check menu
            time.sleep(1)
        else:
            time.sleep(1)
            break

def select_char_and_skill(characters, skills):
    for char, skill in zip(characters, skills):
        select_char(char)
        select_skill(skill)

characters_array = [1, 2, 3, 4]
skills_array = [3, 0, 0, 4]

characters_array2 = [1, 2, 3, 4]
skills_array2 = [3, 0, 0, 4]

characters_array3 = [1, 2, 3, 4]
skills_array3 = [3, 0, 0, 4]

characters_array4 = [1, 2, 3, 4]
skills_array4 = [3, 0, 0, 4]

def main():
    delay_tap()#start
    delay_tap()#confirm
    press_until_Start()
    select_char_and_skill(characters_array, skills_array)
    delay_tap(2361, 1551)  # atk
    wait_Battle()
    select_char_and_skill(characters_array2, skills_array2)
    delay_tap(1994, 1562)  # boost
    delay_tap(2361, 1551)  # atk
    #######phaese 2
    press_until_Start()
    select_char_and_skill(characters_array3, skills_array3)
    delay_tap(2361, 1551)  # atk
    wait_Battle()
    select_char_and_skill(characters_array4, skills_array4)
    delay_tap(1994, 1562)  # boost
    delay_tap(2361, 1551)  # atk
