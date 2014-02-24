#!/usr/bin/env python
import libxml2
from libxml2 import xmlAttr
import os,subprocess,sys,shutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
from sumolib import checkBinary
import traci
import CreateListAndProgram
from CreateListAndProgram import ChangeBusTrafficLights, CreateProgramTrafficLights, CreateProgramBusTrafficLights


doc=libxml2.parseFile("data/RondPoint.rou.xml")
ctxt=doc.xpathNewContext()
ListeVeh= map(xmlAttr.getContent,ctxt.xpathEval("//@id"))
print "le nombre de vehicules est de " + str(len(ListeVeh))
	
PORT = 8815

BusGreen = 'rrrrrGGGGrrr' 
BusYellow = 'rrrrryyyyrrr'
BusRedOutRedInGreen = 'GGGGGrrrrrrr' 
BusRedOutRedInYellow ='yyyyyrrrrrrr' 
BusRedOutGreenInRed = 'rrrrrrrrrGGG'
BusRedOutYellowInRed = 'rrrrrrrrryyy'
BusRedOutRedInRed = 'rrrrrrrrrrrr'

BusGreen2 = 'GGrrrrrrrrrrGG' 
BusYellow2 = 'yyrrrrrrrrrryy'
BusRedOutRedInGreen2 = 'rrrrrrrGGGGGrr' 
BusRedOutRedInYellow2 ='rrrrrrryyyyyrr' 
BusRedOutGreenInRed2 = 'rrGGGGGrrrrrrr'
BusRedOutYellowInRed2 = 'rryyyyyrrrrrrr'
BusRedOutRedInRed2 = 'rrrrrrrrrrrrrr'


if not traci.isEmbedded():
    sumoBinary = checkBinary('sumo-gui')
    sumoConfig = "data/RondPoint.sumocfg"
    sumoProcess = subprocess.Popen("%s -c %s" % (sumoBinary, sumoConfig), shell=True, stdout=sys.stdout)
    traci.init(PORT)
    
ProgramInitial1=CreateProgramTrafficLights([],BusRedOutRedInGreen,BusRedOutRedInYellow,BusRedOutGreenInRed,BusRedOutYellowInRed,BusRedOutRedInRed)
Program1= CreateProgramBusTrafficLights([],BusGreen,BusYellow,BusRedOutRedInGreen,BusRedOutRedInYellow,BusRedOutGreenInRed,BusRedOutYellowInRed,BusRedOutRedInRed)
programPointer1=len(Program1)-3

ProgramInitial2=CreateProgramTrafficLights([],BusRedOutRedInGreen2,BusRedOutRedInYellow2,BusRedOutGreenInRed2,BusRedOutYellowInRed2,BusRedOutRedInRed2)
Program2= CreateProgramBusTrafficLights([],BusGreen2,BusYellow2,BusRedOutRedInGreen2,BusRedOutRedInYellow2,BusRedOutGreenInRed2,BusRedOutYellowInRed2,BusRedOutRedInRed2)
programPointer2=len(Program2)-3

step = 0
i1=i2=0
check1=check2='ok'
counter1=counter2=0
b1=b2=0




while step==0 or traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    result1=ChangeBusTrafficLights("3","0","1214943442",step,check1,Program1,programPointer1,i1,ProgramInitial1,counter1,b1)
    check1=result1[0]
    programPointer1=result1[1]
    i1=result1[2]
    counter1=result1[3]
    b1=result1[4]

    result2=ChangeBusTrafficLights("2","1","2479049221",step,check2,Program2,programPointer2,i2,ProgramInitial2,counter2,b2)
    check2=result2[0]
    programPointer2=result2[1]
    i2=result2[2]
    counter2=result2[3]
    b2=result2[4]

    
    
  
    
    step += 1

traci.close()
sys.stdout.flush()