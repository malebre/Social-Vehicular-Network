#!/usr/bin/env python
import libxml2
from libxml2 import xmlAttr
import os,subprocess,sys,shutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
from sumolib import checkBinary
import traci
import fonction
from fonction import ChangeBusTrafficLights,InitialBusTrafficLights,CreateProgramTrafficLights,TrafficLight,CreateProgramBusTrafficLights,


doc=libxml2.parseFile("data/RondPoint.rou.xml")
ctxt=doc.xpathNewContext()
ListeVeh= map(xmlAttr.getContent,ctxt.xpathEval("//@id"))
print "le nombre de vehicules est de " + str(len(ListeVeh))
	
PORT = 8813

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
ProgramWithBus1= CreateProgramBusTrafficLights([],BusGreen,BusYellow,BusRedOutRedInGreen,BusRedOutRedInYellow,BusRedOutGreenInRed,BusRedOutYellowInRed,BusRedOutRedInRed)
programPointer1=len(Program1)-3

ProgramInitial2=CreateProgramTrafficLights([],BusRedOutRedInGreen2,BusRedOutRedInYellow2,BusRedOutGreenInRed2,BusRedOutYellowInRed2,BusRedOutRedInRed2)
ProgramWithBus2= CreateProgramBusTrafficLights([],BusGreen2,BusYellow2,BusRedOutRedInGreen2,BusRedOutRedInYellow2,BusRedOutGreenInRed2,BusRedOutYellowInRed2,BusRedOutRedInRed2)
programPointer2=len(Program2)-3

step = 0
#i1=i2=0
#check1=check2='ok'
#counter=0
#b=0

doc=libxml2.parseFile("data/RondPoint.net.xml")
ctxt=doc.xpathNewContext()
XJunc1=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='2479049221']/@x"))
YJunc1=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='2479049221']/@y"))
XJunc2=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943442']/@x"))
YJunc2=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943442']/@y"))
XJunc3=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943548']/@x"))
YJunc3=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943548']/@y"))
XJunc4=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='431399475']/@x"))
YJunc4=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='431399475']/@y"))

ListCoordJunc=[[XJunc1,YJunc1],[XJunc2,YJunc2],[XJunc3,YJunc3],[XJunc4,YJunc4]]
LaneInc1 = [["-440_0","-440_1", "-440_2"],["229259796_0","229259796_1"]]
LaneInc1Bus = ['240120119_0','-240120122_0']
LaneInc2=[['-1365_0','-1365_1', '-1365_2'],['240143210_0','240143210_1','240143210_2']]
LaneInc2Bus=['-240120119_0','-1277_0']

JuncIdBus=["2479049221","1214943442"]

LaneOut1=[['239331353_0'],['105490279_0','105490279_1'],['105490284_0']]
LaneOut2=[['105490284_0'],['105490271_0','105490271_1'],['239331353_0']]
LaneOut1Bus=['-240120119_0','240120122_0']
LaneOut2Bus=['240120119_0','--1277_0']

JuncId=["1214943548","431399475"]


check=''
out=''

while step==0 or traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
 	




    
    #result1=ChangeBusTrafficLights("3","0","1214943442",step,check1,Program1,programPointer1,i1,ProgramInitial1,counter,b)
    #check1=result1[0]
    #programPointer1=result1[1]
    #i1=result1[2]
    #counter=result1[3]
    #b=result1[4]
		
    	#for vehID in traci.vehicle.getListID():
		#if traci.vehicle.getTypeID(vehID)=="Vehicle":
			#RoadVeh=traci.vehicle.getRoadID(vehID)
			#VehX=traci.vehicle.getPosition(vehID)[0]
			#VehY=traci.vehicle.getPosition(vehID)[1]
			#if Roadveh in EdgeIn:
				#if abs(VehX-Xjunc1)<20 and  abs(VehY-Yjunc1)<20:
					#if density>valeur:
					#	ChangeBusTrafficLights(JuncId[0])
				#elif abs(VehX-Xjunc2)<20 and  abs(VehY-Yjunc2)<20:
					#if density>valeur:
						#ChangeBusTrafficLights(JuncId[1])
    Occupancy=len(LaneInc1)*[0]
    for Edge in LaneInc1:
	for lane in Edge
		Occupancy[j]=Occupancy[j] + traci.lane.getLastStepOccupancy(lane)

	for vehID in traci.vehicle.getListID():		
		if traci.vehicle.getTypeID(vehID)=="Bus":
			LaneBus=traci.vehicle.getLaneID(vehID)
			BusX=traci.vehicle.getPosition(vehID)[0]
			BusY=traci.vehicle.getPosition(vehID)[1]
			if (abs(BusX-Xjunc1)<20 and  abs(BusY-Yjunc1)<20):
				if (LaneBus in LaneInc1Bus):
					if check!='ok':
						check=InitialBusTrafficLights(JuncId[0],ProgramWithBus1,check)
						i=3
		               		 else:
						i=ChangeBusTrafficLights(feu,i,ProgWithBus)
				if check=='ok':
					i=ChangeBusTrafficLights(feu,i,ProgWithBus)
				if (LaneBus in LaneOut1Bus) and out !='ok':
					traci.trafficlights.setRedYellowGreenState(feu,ProgramWithBus[24])
					out=='ok'
  					if Occupancy[0]>Occupancy[1]:
						i=0
					elif:
						i=22

	if traci.trafficlights.getRedYellowGreenState(JuncId[0])=='GGGGGrrrrrrr'
		if Occupancy[0]>Occupancy[1]:
			traci.trafficlights.setRedYellowGreenState(JuncId[0],'GGGGGrrrrrrr')
		else:
			i=16

	if traci.trafficlights.getRedYellowGreenState(JuncId[0])=='rrrrrrrrrGGG'
		if Occupancy[1]>Occupancy[0]:
			traci.trafficlights.setRedYellowGreenState(JuncId[0],'rrrrrrrrrGGG')
		else:
			i=47	
	i=TrafficLight(JuncId[0],i,Program)


		
			
		
		


   #result1=ChangeBusTrafficLights("3","0","1214943442",step,check1,Program1,programPointer1,i1,ProgramInitial1,counter,b)
   # check1=result1[0]
    #programPointer1=result1[1]
    #i1=result1[2]
    #counter=result1[3]
    #b=result1[4]

   #result2=ChangeBusTrafficLights("2","1","2479049221",step,check2,Program2,programPointer2,i2,ProgramInitial2,counter,b)
   # check2=result2[0]
    #programPointer2=result2[1]
    #i2=result2[2]
    #counter=result2[3]
    #b=result2[4]



    
    
  
    
    step += 1

traci.close()
sys.stdout.flush()
