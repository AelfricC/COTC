import time
from xiaopy import *
from Phone_COTC import *

characters_array = [1, 2, 3, 4]
skills_array = [[4], [3], [2], [4]]


def auto_story():
    launch_game()
    print("started")
    while True:
        if xp.findColor("#D0C4B4", "79|27|#D0C4B4, 116|90|#D0C4B4", 70, 133, 2920, 1727):
            double_fast_tap(1208, 423)
        elif xp.matchColor("#255A70", 1615, 1411):#confirm story reward
            print("4")
            double_fast_tap(1615, 1411)
            double_fast_tap(1576, 1268)
        elif xp.matchColor("#51473A", 2074, 1178):
            double_fast_tap(1934, 1137)
        # elif xp.matchColor("#51473A", 2136, 1163,1):#battle
        #     print("there is battle")
        #     select_char_and_skill(characters_array, skills_array, 2, 1)
        elif xp.matchColor("#F0EBE8", 217, 163) and xp.matchColor("#F0EBE8", 466, 202) and xp.matchColor("#F0EBE8", 598, 203):
            print("battle finished")
            double_fast_tap(Middle_Screen[0], Middle_Screen[1])
            double_fast_tap(Middle_Screen[0], Middle_Screen[1])
            double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        elif xp.matchColor("#545049", 599, 938) and xp.matchColor("#4C4944", 832, 950):
            print("story finished")
            double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        time.sleep(0.3)
auto_story()