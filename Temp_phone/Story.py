import time
from xiaopy import *
from Phone_COTC import *

characters_array = [1, 2, 3, 4]
skills_array = [[4], [3], [2], [4]]


def auto_story():
    launch_game()
    print("started")
    while True:
        if xp.findColor("#D0C4B4", "79|27|#D0C4B4, 116|90|#D0C4B4", 190, 41, 2058, 939):
            double_fast_tap(1208, 423)
        # elif xp.matchColor("#4C4944", 601, 937) and xp.matchColor("#57524B", 838, 935):#traveller screen
        #     print("1")
        #     double_fast_tap(Middle_Screen[0],Middle_Screen[1])
        # elif xp.matchColor("#1F5267", 2037, 1415):
        #     print("2")
        #     double_fast_tap(2037, 1415)
        #     double_fast_tap(2023, 1282) #prioritize
        # elif xp.matchColor("#255A70", 1615, 1411):#confirm story reward
        #     print("4")
        #     double_fast_tap(1615, 1411)
        #     double_fast_tap(1576, 1268)
        # elif xp.matchColor("#A48E37", 1668, 1486):
        #     double_fast_tap(1668, 1486)
        # elif xp.matchColor("#51473A", 2136, 1163,1):#battle
        #     print("there is battle")
        #     double_fast_tap(2136, 1163)
        #     time.sleep(3)
        #     while True:
        #         if not checking_color_once(Battle_Screen):
        #             xp.tap(Middle_Screen[0],Middle_Screen[1])
        #             time.sleep(0.3)
        #         else:
        #             break
        #     print("battle started here")
        #     select_char_and_skill(characters_array, skills_array)
        #     boost_Atk()
        # elif xp.matchColor("#F0EBE8", 217, 163) and xp.matchColor("#F0EBE8", 466, 202) and xp.matchColor("#F0EBE8", 598, 203):
        #     print("battle finished")
        #     double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        #     double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        #     double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        # elif xp.matchColor("#545049", 599, 938) and xp.matchColor("#4C4944", 832, 950):
        #     print("story finished")
        #     double_fast_tap(Middle_Screen[0], Middle_Screen[1])
        time.sleep(0.25)
auto_story()