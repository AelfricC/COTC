import time
import subprocess
from xiaopy import *
from Phone_COTC import *

if xp.findColor("#585B36", "8|6|#515233", 286, 96, 296, 102):  # xp.matchColor("#962B2B", 267, 123,0.85):
    print("1")
elif xp.findColor("#184666", "5|1|#163F5D, 2|3|#184C70",274, 93,293, 114):
    print("2")
else:
    print("none")