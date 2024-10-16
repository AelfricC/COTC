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
        # elif xp.matchColor("#FFFFFF", 2500, 1584, 0.9) and xp.matchColor("#E0DCD7", 694, 1576, 0.95):
        #     print("battle")
        #     # Battle
        #     characters_array = [1, 2, 3, 4]
        #     skills_array1 = [[2], [2], [2], [2]]
        #     select_char_and_skill(characters_array, skills_array1, 2, 1)
        elif xp.matchColor("#F7F8F8", 1962, 1411) and xp.matchColor("#FDFEFE", 1848, 1408) and xp.matchColor("#FBFBFC", 1762, 1402):
            double_fast_tap(1796, 1425)
            print("accept mission")
        elif xp.matchColor("#282828", 110, 179,0.9) and xp.matchColor("#606060", 106, 1654,0.9):
            print("grey box text")
            clickcount = 0
            while True:
                if clickcount <= 7:
                    double_fast_tap(236, 233)
                    clickcount += 1
                    print("looping grey box lick" + str(clickcount))
                else:
                    break
        elif xp.matchColor("#51473A", 2131, 1032) :
            print("choose text box")
            double_fast_tap(2131, 1032)
        elif xp.matchColor("#51473A", 1759, 1197):
            print("choose text box2")
            double_fast_tap(1759, 1197)
        elif xp.matchColor("#DFB75B", 1522, 1465) and xp.matchColor("#D2AC54", 1233, 1472) and xp.matchColor("#CAA750", 1674, 1477):
            print("story completed")
            double_fast_tap(1438, 1415)
        elif xp.matchColor("#524E48", 598, 943) and xp.matchColor("#4C4944", 687, 974) and xp.matchColor("#4C4944", 745, 952) and xp.matchColor("#4C4944", 874, 955):
            print("traveler stoty started")
            double_fast_tap(1438, 1415)
        time.sleep(0.3)

auto_story()