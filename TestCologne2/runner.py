#!/usr/bin/env python

#simulation avec reroutage des vehicules a chaque pas de temps

import os,subprocess,sys,shutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
from sumolib import checkBinary
import traci


sumoBinary = checkBinary('sumo')
sumoConfig = "data/map.sumocfg" 	
#run simulation
sumoProcess = subprocess.Popen(" %s -c %s" % (sumoBinary,sumoConfig),shell=True, stdout=sys.stdout)
sys.stdout.flush()










