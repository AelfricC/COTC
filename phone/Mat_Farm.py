import time
import subprocess
from xiaopy import *
#from cotc import COTC
from Phone_COTC import *

characters_array = [1, 0, 0, 0]
skills_array = [[4], [0], [0], [0]]

characters_array_Cait = [0, 0, 0, 0]
skills_array_Cait = [0, 0, 0, 0]

round_per_recover = 13

run_script_battle(characters_array, skills_array,round_per_recover)
