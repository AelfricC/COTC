import time
import subprocess
from xiaopy import *
from Phone_COTC import *

read = ["#EEEFF0", 2586, 697]
confirm_read = ["#F9FAFA", 1848, 1464]
nut_rewards = ["#2C5F74", 1370, 1363]

# ui = xp.ui()
# book_name = ui.stringValue("book_name")
# if book_name == "Nut":
#     nut()
# else:
#     else()
def nut():
    launch_game()
    characters_array = [1, 2, 3, 0]
    battle_count = 0
    while True:
        start_time = time.time()
        #tap_After_checking(read,20)
        double_tap(2561, 1613)
        xp.toast(str(battle_count))
        tap_After_checking(confirm_read,20)
        press_until_SeeColor(Battle_Screen)
        skills_array = [[0], [3], [3], [0]]
        select_char_and_skill(characters_array, skills_array)
        boost_Atk()
        time.sleep(10)
        # 22222222222222222222222222222
        press_until_SeeColor(Battle_Screen)
        skills_array = [[2], [3], [3], [0]]
        select_char_and_skill(characters_array, skills_array)
        boost_Atk()
        time.sleep(15)
        # End
        press_until_SeeColor(nut_rewards)
        battle_count += 1
        xp.toast(str(battle_count))
        tap_Until_Disappear(nut_rewards)
        double_fast_tap(1506, 1387)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Your program took {elapsed_time} seconds to run.")



nut()
#print(xp.getColor(1518, 1362))