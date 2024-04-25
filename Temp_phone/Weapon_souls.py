import time
from xiaopy import *
from Phone_COTC import *

found_soul = ["#191919", 783, 822]
set_new_soul = [1373, 839]
set_soul = ["#FEFEFE", 1907, 917]

launch_game()
while True:
    double_fast_tap(1814, 921) #enchant
    double_fast_tap(1381, 982) #ok
    time.sleep(3)
    checking_Color(found_soul)
    tap_once_After_checking(found_soul, -1)  # click new soul
    double_fast_tap(1181, 959) #ok
    double_fast_tap(1181, 959)  # ok
    tap_Until_Exsit(set_soul,set_new_soul)