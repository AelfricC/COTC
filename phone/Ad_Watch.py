import time
import subprocess
from xiaopy import *
from Phone_COTC import *
cait_exist = ["#FFFFFF", 2305, 1445]
click_Cait = ["#4E4E4E", 1192, 879]
click_Cait2= ["#3D3D3C", 1213, 873]

######################################
click_trasure = ["#EEEEEE", 2000, 867]
######################################


confirm_watch_ad = ["#21546A", 1707, 1236]
confirm_Cait = ["#295D73", 1594, 1080]
confirm_Cait2 = ["#FFFFFF", 1485, 1071]
normal_ad = ["#202124", 2881, 64]
normal_half_ad = ["#1F1F1F", 2818, 637]
normal_half_ad2 = ["#1F1F1F", 2812, 579]


def close_ad(invalidcount):
    while True:
        ret1 = xp.findColor("#8F8F8F", "13|-13|#8F8F8F", 2681, 579, 2926, 941)
        ret2 = xp.findColor("#222126", "6|-8|#202124", 2848, 55, 2889, 95)
        if ret1:
            print("found " + str(ret1))
            time.sleep(0.5)
            double_fast_tap(ret1.x, ret1.y)
            time.sleep(3)
            break
        elif ret2:
            print("found " + str(ret2))
            time.sleep(0.5)
            double_fast_tap(ret2.x, ret2.y)
            time.sleep(3)
            break
        elif invalidcount > 100:
            break
        else:
            print(invalidcount)
            invalidcount += 1
            time.sleep(0.7)
def ad_cait():
    count = 0
    print("Start")
    while True:
        if count < 6:
            invalidcount = 0
            print("check available ads")
            tap_After_checking(cait_exist,15)
            time.sleep(1)
            # if not xp.matchColor("#454444", 1193, 880): #if not 0
            #     print("cait")
            #     time.sleep(0.5)
            #     double_fast_tap(1066, 879)
            #     time.sleep(0.5)
            #     double_fast_tap(1464, 1291)#confirm to watch
            #     time.sleep(35)
            #     close_ad(invalidcount)
            #     tap_After_checking(confirm_Cait,20)
            #     wait_Battle()
            #     boost_Atk()
            #     wait_Battle()
            #     swap()
            #     boost_Atk()
            #     wait_Battle()
            #     swap()
            #     boost_Atk()
            #     tap_Until_Exsit(Menu,ATK)
            # else:
            print("treasure")
            time.sleep(0.5)
            double_fast_tap(1918, 877)  #click treasure
            time.sleep(0.5)
            double_fast_tap(1464, 1291)  # confirm to watch
            time.sleep(35)
            print("wait for click")
            close_ad(invalidcount)
            check_any_of_this([confirm_Cait,confirm_Cait2],1)
            #double_fast_tap(2881, 64)
            # tap_Until_Disappear(confirm_Cait)
            print("finished")
            count += 1
            time.sleep(1)
# print(xp.getColor(1191, 870))
ad_cait()
