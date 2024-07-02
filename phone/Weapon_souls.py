import time
from xiaopy import *
from Phone_COTC import *

found_soul = ["#191919", 783, 822]
set_new_soul = ["#191919", 932, 748]
set_old_soul = ["#1D1D1C", 889, 471]
set_soul = ["#FEFEFE", 1907, 917]
set_another_soul = [1372, 719]
set_another_soul_new = [1389, 839]

ui = xp.ui()
Keep_Which = ui.stringValue("Keep_Which")

launch_game()
while True:
    double_fast_tap(1814, 921) #enchant
    double_fast_tap(1381, 982) #ok
    time.sleep(3)
    checking_Color(found_soul)
    if Keep_Which == "Keep_Old":
        check_here_tap_there(found_soul,set_old_soul)  # click new soul
        double_fast_tap(1181, 959)  # ok
        double_fast_tap(1181, 959)
        print("tap until done")
        tap_Until_Exsit(set_soul, set_another_soul)
        print("done")
    elif Keep_Which == "Keep_New":
        check_here_tap_there(found_soul,set_new_soul)  # click new soul
        print("tapped")
        double_fast_tap(1181, 959)  # ok
        double_fast_tap(1181, 959)
        print("tap until done")
        tap_Until_Exsit(set_soul, set_another_soul_new)
        print("done")
