#!/usr/bin/env python

#simulation avec reroutage des vehicules sur un pourcentage d'intersection


import os,subprocess,sys,shutil,sumolib
from sumolib import checkBinary
import traci,libxml2,random
from libxml2 import xmlAttr
from fonctionLocal2 import rateOfJunctionChosen,listInter,save,listEdgeInc,listEdgeOut,juncVisitedVehID,slowEdge,currentTravelEdgeOut,occupancyEdgeOut, listVehApplications,routeWeight,intersect,consoEdgeOut,badConsoEdge,slowAndbadConsoEdge,communication


PORT = 8814

	


if not traci.isEmbedded():
	sumoBinary = checkBinary('sumo')
	sumoConfig = "data/mapLocal.sumocfg"
	#run simulation
        sumoProcess = subprocess.Popen(" %s -c  %s" % (sumoBinary,sumoConfig),shell=True, stdout=sys.stdout)
        traci.init(PORT)

#taux d'intersection touchees par le reroutage

#rate=sys.argv[1]
Liste1=['cluster_1770563573_354673595', '36454807#3-AddedOnRampNode', '367149', 'cluster_26721794_26820111_286525444_286525446_68732804_68732817', 'cluster_1672368131_26820077']

a=len(Liste1)-1
#float(len(Liste))
r = random.randint(1,int(a))
l=0
Liste=[]
while l<=r:
	k=random.randint(1,int(a))
	if k<=r:
		Liste.append(Liste1[k])
	l=l+1
#Liste=['cluster_1142037858_1142037884_443339'] camarche 
#Liste=['354652760', '831212705', '1352594']
Liste=['cluster_1770563573_354673595', '359626', '367149', '36454807#3-AddedOnRampNode', 'cluster_26721794_26820111_286525444_286525446_68732804_68732817', 'cluster_1672368131_26820077']


#Choix des intersections ou le reroutage s'effectura

JunctionChosen=rateOfJunctionChosen(Liste)
XJunc=JunctionChosen[0]
YJunc=JunctionChosen[1]
EdgeInc=JunctionChosen[2]
JuncId=JunctionChosen[3]

#Liste des coordonnees des intersecions

ListInter=listInter(XJunc,YJunc)


#On enregistre la Liste d'intersections choisies dans un fichier

#save("data/ListeInterLocal",JuncId)

#Liste des liens entrants de chaque intersection

ListEdgeInc=listEdgeInc(EdgeInc)

#Liste des liens sortants de chaque intersection
#si elle ne comunique pas on les considere distinctement, sinon on ne fait qu'une grande liste
ListEdgeOut=communication(str(sys.argv[4]),JuncId)

#initialisation des liens visites

JuncVisitedVehID=juncVisitedVehID(ListInter)

#Liste des vehicules avec choix des applications
rateGreenWay=int(sys.argv[1])
rateQuickWay=int(sys.argv[2])
rateSmoothWay=int(sys.argv[3])

ListVehApplications=listVehApplications(rateGreenWay,rateQuickWay,rateSmoothWay)
ListGreenWay=ListVehApplications[0]
ListQuickWay=ListVehApplications[1]
ListSmoothWay=ListVehApplications[2]


#initialisation des listes de donnees enregistrees en temps reel a chaque intersection
MaxSpeedEdgeOut=len(ListInter)*['']
OccupancyEdgeOut=len(ListInter)*['']
ConsoEdgeOut=len(ListInter)*['']
MinConsoEdgeOut=len(ListInter)*['']
SlowEdge=len(ListInter)*['']
BadConsoEdge=len(ListInter)*['']
SlowAndbadConsoEdge=len(ListInter)*['']

#compromis pour les vehicules ayant choisis smoothway
Compromis=len(ListSmoothWay)*[0]
i=0
while i<len(ListSmoothWay):
	Compromis[i]=random.uniform(0,1)
	i=i+1
	

#pas de temps

step=0

#Liste des vehicules

ListvehID=[]

#vehicule changeant de route pour mesurer la Satisfaction

changeVehGreen=[]
changeVehQuick=[]
changeVehSmooth=[]


while step == 0 or traci.simulation.getMinExpectedNumber() > 0:
    	traci.simulationStep()
	index=0
	
	for vehID in intersect(traci.vehicle.getIDList(),ListSmoothWay):
			#initialisation du chemin des compromis
			if not(vehID in ListvehID):
				ListvehID.append(vehID)
				r=Compromis[ListSmoothWay.index(vehID)]
				routeWeight(r,traci.edge.getIDList())
				traci.vehicle.rerouteEffort(vehID)

	#initialisation du chemin selon la conso
	routeWeight('Conso',traci.edge.getIDList())

	for vehID in intersect(traci.vehicle.getIDList(),ListGreenWay):
			#initialisation du chemin selon la conso
			if not(vehID in ListvehID):
				ListvehID.append(vehID)
				traci.vehicle.rerouteEffort(vehID)

	
				
				



        #a chaque pas de temps pour chaque intersection :
	for CoordInter in ListInter:
        	index=ListInter.index(CoordInter)
		CoordInterX=float(CoordInter[0])
		CoordInterY=float(CoordInter[1])

		#Liste des Vitesses Maximales de chaque lien sortant de l'intersection et leur taux d'occupation
		MeasureTimeEdgeOut=occupancyEdgeOut(ListEdgeOut[index],step)
		MaxSpeedEdgeOut[index]=MeasureTimeEdgeOut[1]
		OccupancyEdgeOut[index]=MeasureTimeEdgeOut[0]

		#Liste des consos de chaque lien sortant de l'intersection et leur conso minimum
		MeasureConsoEdgeOut=consoEdgeOut(ListEdgeOut[index],step)
		ConsoEdgeOut[index]=MeasureConsoEdgeOut[0]
		MinConsoEdgeOut[index]=MeasureConsoEdgeOut[1]

		#Liste des liens sortant depassant le seuil de cout en temps
		Slow=slowEdge(OccupancyEdgeOut[index],MaxSpeedEdgeOut[index],ListEdgeOut[index],JuncId)
		SlowEdge[index]=Slow[0]
		#Liste des liens sortant depassant le seuil de cout en conso
		BadConsoEdge[index]=badConsoEdge(ConsoEdgeOut[index],MinConsoEdgeOut[index],ListEdgeOut[index],JuncId)
		
		
#GREENWAY	
		#changement du poids des liens sortant les plus consommateur a l'intersection
		for edge in BadConsoEdge[index]:
			traci.edge.setEffort(edge,920000000000)	
		
		for vehID in intersect(traci.vehicle.getIDList(),ListGreenWay):
			coordVehx=traci.vehicle.getPosition(vehID)[0]
			coordVehy=traci.vehicle.getPosition(vehID)[1]
			
			#on considere les vehicules sur les liens entrants presents a l'intersection
			if (coordVehx>=CoordInterX-40) and (coordVehx<=CoordInterX+40) and (coordVehy>=CoordInterY-40) and (coordVehy<=CoordInterY+40) and (traci.vehicle.getRoadID(vehID) in ListEdgeInc[index]) and not(vehID in JuncVisitedVehID[index]):

				#enregistrement du passage du vehicule pour eviter les boucles infinies
				JuncVisitedVehID[index].append(vehID)
				
				#on retient la position
				position=traci.vehicle.getRoute(vehID).index(traci.vehicle.getRoadID(vehID))
				Route=traci.vehicle.getRoute(vehID)[position:(len(traci.vehicle.getRoute(vehID)))]

				#recalcule chemin
				traci.vehicle.rerouteEffort(vehID)

				#on test si il ya changement de route:
				if  Route!=traci.route.getEdges(traci.vehicle.getRouteID(vehID)):
					if not(vehID in changeVehGreen):
						changeVehGreen.append(vehID)
		
		#initialisation des poids 
		routeWeight('Conso',ListEdgeOut[index])



#SMOOTHWAY	
		
		for vehID in intersect(traci.vehicle.getIDList(),ListSmoothWay):
			coordVehx=traci.vehicle.getPosition(vehID)[0]
			coordVehy=traci.vehicle.getPosition(vehID)[1]
			
			#on considere les vehicules sur les liens entrants presents a l'intersection
			if (coordVehx>=CoordInterX-40) and (coordVehx<=CoordInterX+40) and (coordVehy>=CoordInterY-40) and (coordVehy<=CoordInterY+40) and (traci.vehicle.getRoadID(vehID) in ListEdgeInc[index]) and not(vehID in JuncVisitedVehID[index]):

				#enregistrement du passage du vehicule pour eviter les boucles infinies
				JuncVisitedVehID[index].append(vehID)
				#compromis temps conso choisi par vehID
				r=Compromis[ListSmoothWay.index(vehID)]			
				#Liste des liens sortant depassant le seuil compromis temps conso				
				SlowAndbadConsoEdge[index]=slowAndbadConsoEdge(r,OccupancyEdgeOut[index],ConsoEdgeOut[index],MinConsoEdgeOut[index],ListEdgeOut[index],JuncId,MaxSpeedEdgeOut[index])

				#calcule des poids dans le reseau
				routeWeight(r,traci.edge.getIDList())

				#changement du poids des liens sortant les plus consommateur a l'intersection
				for edge in SlowAndbadConsoEdge[index]:
					traci.edge.setEffort(edge,920000000000)

				#on retient la position
				position=traci.vehicle.getRoute(vehID).index(traci.vehicle.getRoadID(vehID))
				Route=traci.vehicle.getRoute(vehID)[position:(len(traci.vehicle.getRoute(vehID)))]


				#recalcule chemin
				traci.vehicle.rerouteEffort(vehID)

				#on test si il ya changement de route:
				if  Route!=traci.route.getEdges(traci.vehicle.getRouteID(vehID)):
					if not(vehID in changeVehSmooth):
						changeVehSmooth.append([vehID,r])

		
		#initialistion des poids pour l'appli greenway
		routeWeight('Conso',traci.edge.getIDList())


#QUICKWAY

		#changement du poids des liens sortant les plus long a l'intersection
		for edge in SlowEdge[index]:
			traci.edge.adaptTraveltime(edge,920000000000)

		for vehID in intersect(traci.vehicle.getIDList(),ListQuickWay):
			coordVehx=traci.vehicle.getPosition(vehID)[0]
			coordVehy=traci.vehicle.getPosition(vehID)[1]

			#on considere les vehicules sur les liens entrants presents a l'intersection
			if (coordVehx>=CoordInterX-40) and (coordVehx<=CoordInterX+40) and (coordVehy>=CoordInterY-40) and (coordVehy<=CoordInterY+40) and (traci.vehicle.getRoadID(vehID) in ListEdgeInc[index]) and not(vehID in JuncVisitedVehID[index]):

				#enregistrement du passage du vehicule pour eviter les boucles infinies
				JuncVisitedVehID[index].append(vehID)

				#on retient la position
				position=traci.vehicle.getRoute(vehID).index(traci.vehicle.getRoadID(vehID))
				Route=traci.vehicle.getRoute(vehID)[position:(len(traci.vehicle.getRoute(vehID)))]
				
				#recalcule du plus court chemin 
				traci.vehicle.rerouteTraveltime(vehID)

				#on test si il ya changement de route:
				if  Route!=traci.route.getEdges(traci.vehicle.getRouteID(vehID)):
					if not(vehID in changeVehQuick):
						changeVehQuick.append(vehID)

		
		#initialistion des poids 
		routeWeight('Time',ListEdgeOut[index])







	step=step+1

	if step==901:
		break

	

traci.close()
#print step
#compte = {}.fromkeys(set(IntersectionCongestion),1)
#for valeur in IntersectionCongestion:
#   	compte[valeur] += 1
#from operator import itemgetter
#compte = compte.items()
#compte.sort(key=itemgetter(1),reverse=True)
#print changeVeh
#print compte
#InterCongSelect=[]
#for valeur in compte:
#	if valeur[1]>(step/9.5):
		#InterCongSelect.append(valeur[0])
#print InterCongSelect

sys.stdout.flush()







