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
        elif xp.matchColor("#F7F8F8", 1962, 1411) and xp.matchColor("#FDFEFE", 1848, 1408) and xp.matchColor("#FBFBFC", 1762, 1402):
            double_fast_tap(1796, 1425)
            print("accept mission")
            time.sleep(0.5)
            double_fast_tap(1132, 1256)
            time.sleep(0.5)
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
        elif xp.matchColor("#4C4944", 601, 960) and xp.matchColor("#524E48", 875, 957) and xp.matchColor("#4C4944", 962, 974):
            print("chapter begins")
            double_fast_tap(1068, 897)
        elif xp.matchColor("#E2E6E8", 1484, 1421) and xp.matchColor("#FFFFFF", 1441, 1415):
            print("accept reward")
            double_fast_tap(1493, 1395)
            double_fast_tap(567, 726)
        elif xp.matchColor("#F0ECE7", 2430, 587) and xp.matchColor("#FFAB1C", 2545, 528) and xp.matchColor("#FFFFFF", 2476, 1549):
            print("battle")
            delay_tap(1996, 1578)
            double_fast_tap(2515, 1583)
        elif xp.matchColor("#F0EBE8", 217, 209) and xp.matchColor("#F0EBE8", 556, 205) and xp.matchColor("#C4A830", 667, 991):
            print("battle finished")
            double_fast_tap(1058, 949)
            double_fast_tap(1058, 949)
            double_fast_tap(1058, 949)
            time.sleep(1.5)
        time.sleep(0.3)
auto_story()