#!/usr/bin/env python

#simulation sans reroutage des vehicules : chemin le plus court en temps calcule hors ligne au debut de la simulation

import os,subprocess,sys,shutil,sumolib
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
from sumolib import checkBinary
import libxml2,random
import traci
from libxml2 import xmlAttr
from fonctionLocal2 import listEdgeInc, listEdgeOut

PORT = 8814

doc=libxml2.parseFile("data/map.net.xml")
ctxt=doc.xpathNewContext()
EdgeIncAll=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@type='priority']/@incLanes"))
JuncIdAll=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@type='priority']/@id"))

ListEdgeInc=listEdgeInc(EdgeIncAll)
ListEdgeOut=listEdgeOut(JuncIdAll)
l=len(JuncIdAll)
MaxTime=l * [0]

if not traci.isEmbedded():
	sumoBinary = checkBinary('sumo')
	sumoConfig = "data/mapWO.sumocfg"
	#run simulation
        sumoProcess = subprocess.Popen(" %s -c  %s" % (sumoBinary,sumoConfig),shell=True, stdout=sys.stdout)
        traci.init(PORT)

step=0
number=len(JuncIdAll)*[0]
DifferentSpeed=0
CongestionList=[]
for junction in JuncIdAll:
	CongestionList.append([0,junction])

while step == 0 or traci.simulation.getMinExpectedNumber() > 0:
    	traci.simulationStep()
	for junction in JuncIdAll:
		index=JuncIdAll.index(junction)
		for edge in ListEdgeOut[index]:
			lane=edge+'_0'
			number[index]=len(ListEdgeOut[index])
			MaxSpeedEdgeOut=traci.lane.getMaxSpeed(lane)
			if MaxSpeedEdgeOut <= 13.89:
				threshold = 0.20
			if MaxSpeedEdgeOut > 13.89:
				threshold = 0.16	
			if traci.edge.getLastStepOccupancy(edge)>=threshold:
				CongestionList[index][0]=1+CongestionList[index][0]
	step=step+1

traci.close()

List=[]
for junction in CongestionList[1]:
	index=CongestionList[1].index(junction)
	CongestionList[index][0]=float(CongestionList[index][0])/float(number[index])
CongestionList.sort()
#print CongestionList
for intersection in CongestionList :
	if intersection[0]>0:
		List.append(intersection[1])
#print List
	
sys.stdout.flush()	





