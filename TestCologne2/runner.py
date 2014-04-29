#!/usr/bin/env python

#simulation avec reroutage des vehicules a chaque pas de temps

import os,subprocess,sys,shutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools")) # tutorial in tests
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools")) # tutorial in docs
from sumolib import checkBinary
import traci
from fonctionLocal2 import intersect

PORT = 8814


ListGreen=sys.argv[1]
ListQuick=sys.argv[2]
ListSmooth=sys.argv[3]
Compromis=sys.argv[4]


	


if not traci.isEmbedded():

	sumoBinary = checkBinary('sumo')
	sumoConfig = "data/map.sumocfg" 	
	#run simulation
        sumoProcess = subprocess.Popen(" %s -c %s" % (sumoBinary,sumoConfig),shell=True, stdout=sys.stdout)
        traci.init(PORT)

#pas de temps
step=0

#Liste des vehicules
ListevehID=[]

#Liste des routes empruntees par les vehicules
ListeCurrentRoad=[]

#debut de la simulation
while step == 0 or traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    if step%5==0:
	    #changement du poids de chaque lien de la carte en fonction de la longueur du lien et de la vitesse moyenne des vehicules presents dessus
	    for edge in traci.edge.getIDList():
		traci.edge.adaptTraveltime(edge,traci.edge.getTraveltime(edge))

	   # reroutage global des vehicules en fonction des nouveaux poids des liens de la carte, reroutage a chaque fois que le vehicule change de lien 
	    for vehID in intersect(traci.vehicle.getIDList(),ListQuick):
			if traci.vehicle.getRoadID(vehID) in traci.vehicle.getRoute(vehID):
	       			traci.vehicle.rerouteTraveltime(vehID)


	    #changement du poids de chaque lien de la carte en fonction de la longueur du lien et de la vitesse moyenne des vehicules presents dessus
	    for edge in traci.edge.getIDList():
		traci.edge.setEffort(edge,traci.edge.getFuelConsumption(edge))

	   # reroutage global des vehicules en fonction des nouveaux poids des liens de la carte, reroutage a chaque fois que le vehicule change de lien 
	    for vehID in intersect(traci.vehicle.getIDList(),ListGreen):
			if traci.vehicle.getRoadID(vehID) in traci.vehicle.getRoute(vehID):
	       			traci.vehicle.rerouteEffort(vehID)
		
	   # reroutage global des vehicules en fonction des nouveaux poids des liens de la carte, reroutage a chaque fois que le vehicule change de lien 
	    for vehID in intersect(traci.vehicle.getIDList(),ListSmooth):
			if traci.vehicle.getRoadID(vehID) in traci.vehicle.getRoute(vehID):
				#changement du poids de chaque lien de la carte
		    		for edge in traci.edge.getIDList():
						r=Compromis[ListSmooth.index(vehID)]
						measure=r*traci.edge.getTraveltime(edge)+(1-r)*traci.edge.getFuelConsumption(edge)	
						traci.edge.setEffort(edge,measure)
		       		traci.vehicle.rerouteEffort(vehID)

    if step==900:
	break
    step=step+1
traci.close()
sys.stdout.flush()

