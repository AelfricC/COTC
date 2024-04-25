import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

characters_array = [1, 2, 0, 0]
skills_array = [[4], [0], [0], [0]] #abosorb
skills_array1 = [[4], [4,0,1], [0], [0]] #recover
skills_array2 = [[4], [3,0], [0], [0]] #abosorb
characters_array_Cait = [0, 0, 0, 0]
skills_array_Cait = [0, 0, 0, 0]

round_per_recover = 18
run_script_battle(characters_array, skills_array,round_per_recover)
#local_mat_farm()