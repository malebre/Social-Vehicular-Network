#!/usr/bin/env python
import os,subprocess,sys,shutil,sumolib
from sumolib import checkBinary
import traci,libxml2,random
from libxml2 import xmlAttr

def CreateProgramTrafficLights(Program,BusRedOutRedInGreen,BusRedOutRedInYellow,BusRedOutGreenInRed,BusRedOutYellowInRed,BusRedOutRedInRed):
	i=1
	while i<=52:
		if i<=15:
			Program.append(BusRedOutRedInGreen)
		if 15<i<=18:
			Program.append(BusRedOutRedInYellow)
		if 18<i<=21:		
			Program.append(BusRedOutRedInRed)
		if 21<i<=46:
			Program.append(BusRedOutGreenInRed)
		if 46<i<=49:
			Program.append(BusRedOutYellowInRed)
		if 49<i<=52:
			Program.append(BusRedOutRedInRed)
		i=i+1
	return Program

def CreateProgramBusTrafficLights(Program,BusGreen,BusYellow,BusRedOutRedInGreen,BusRedOutRedInYellow,BusRedOutGreenInRed,BusRedOutYellowInRed,BusRedOutRedInRed):
	i=1
	while i<=24:
		if i==1:
			Program.append(BusRedOutYellowInRed)
		if i==2:
			Program.append(BusRedOutRedInYellow)
		if 3<=i<=19:
			Program.append(BusGreen)
		if 19<=i<=21:
			Program.append(BusYellow)
		if i==22:
			Program.append(BusRedOutGreenInRed)
		if i==23:
			Program.append(BusRedOutRedInGreen)
		if i==24:
			Program.append(BusRedOutRedInRed)
		i=i+1
	return Program



def InitialBusTrafficLights(feu,ProgWithBus,check):
	statutactuel=traci.trafficlights.getRedYellowGreenState(feu)
	programPointeur=ProgWithBus.index(statutactuel)
	b=programPointeur
        a=len(ProgWithBus)-3
        c=len(ProgWithBus)-2
	if c-b==0:
		traci.trafficlights.setRedYellowGreenState(feu,ProgWithBus[1])
	elif a-b==0:
		traci.trafficlights.setRedYellowGreenState(feu,ProgWithBus[0])
	check='ok'
	return check

def ChangeBusTrafficLights(feu,i,ProgWithBus)
		traci.trafficlights.setRedYellowGreenState(feu,ProgWithBus[i])
		i=i+1
	return i

def TrafficLight(feu,i,Program)
		traci.trafficlights.setRedYellowGreenState(feu,Program[i])
		i=i+1
	return i


   

    a=len(Prog)-3
    c=len(Prog)-2
    if no==0 and check=='ok':
	if i==len(ProgInitial)-1:
		traci.trafficlights.setRedYellowGreenState(feu,ProgInitial[i])
		i=0
	else:
		traci.trafficlights.setRedYellowGreenState(feu,ProgInitial[i])
		i=i+1
    if no > 0 and check=='':
	if counter!=0:
		if c-b==0:
			traci.trafficlights.setRedYellowGreenState(feu,Prog[1])
			counter=counter-1
		elif a-b==0:
			traci.trafficlights.setRedYellowGreenState(feu,Prog[0])
			counter=counter-1
	else :
		programPointer=programPointer+1
		i=programPointer
		if i==len(Prog)-3:
                	check='ok'
			i=0
		else:
			traci.trafficlights.setRedYellowGreenState(feu,Prog[i])
    if no==0 and check=='':
	i=i+1
	if i==len(Prog)-3:
		check='ok'
		programPointer=len(Prog)-3
		i=0
	else:
        	traci.trafficlights.setRedYellowGreenState(feu,Prog[i])	
		
    if no > 0 and check=='ok':
	check=''
	statutactuel=traci.trafficlights.getRedYellowGreenState(feu)
	programPointeur=Prog.index(statutactuel)
	b=programPointeur
	if c-b==0:
		traci.trafficlights.setRedYellowGreenState(feu,Prog[1])
		counter=2
	elif a-b==0:
		traci.trafficlights.setRedYellowGreenState(feu,Prog[0])
		counter=2
	else:
		counter=0
	programPointer=1
    return check,programPointer,i,counter,b




#Liste des coordonnees de chaque intersection

def listInter(X,Y):
	i=0
	ListInter=[]
	while i<len(X):
		ListInter.append([X[i],Y[i]])
		i=i+1
	return ListInter

#Creation des listes de donnees utiles

def createList(FichierMapXml):
	doc=libxml2.parseFile(FichierMapXml)
	ctxt=doc.xpathNewContext()

	#coordonnees des intersections autre que les feux
	XJunc1=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='2479049221']/@x"))
	YJunc1=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='2479049221']/@y"))
	XJunc2=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943442']/@x"))
	YJunc2=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943442']/@y"))

	#nom des liens entrant sur chaque intersection
	LaneInc1=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='2479049221']/@incLanes"))
	LaneInc2=map(xmlAttr.getContent,ctxt.xpathEval("//junction[@id='1214943442']/@incLanes"))

	return XJunc1,YJunc1,XJunc2,YJunc2,LaneInc1,LaneInc2

#Choix des intersections ou le reroutage s'effectura

def rateOfJunctionChosen(rate):
	CreateList=createList("data/map.net.xml")
	XJuncAll=CreateList[0]
	YJuncAll=CreateList[1]
	EdgeIncAll=CreateList[2]
	JuncIdAll=CreateList[3]
	XJunc=[]
	YJunc=[]
	EdgeInc=[]
	JuncId=[]
	N=0
	rate=float(rate)
	while N<len(XJuncAll):
		rand=random.uniform(0,1)
		if rand<rate:
			XJunc.append(XJuncAll[N])
			YJunc.append(YJuncAll[N])		
			EdgeInc.append(EdgeIncAll[N])
			JuncId.append(JuncIdAll[N])
			N=N+1
		else:
			N=N+1
	return XJunc,YJunc,EdgeInc,JuncId



#Sauvegarde des identifiants des intersections ou s'effectue le reroutage

def save(Fichier,JuncId):
	f = open(Fichier, "w")

	for element in JuncId:
		f.write(element+' ')
		f.write('\n')
	f.close()

#Liste des liens sortants de chaque intersection

def listEdgeOut(JuncId):
	doc=libxml2.parseFile("data/RondPoint.net.xml")
	ctxt=doc.xpathNewContext()
	EdgeOut1=map(xmlAttr.getContent,ctxt.xpathEval("//edge[@from='1214943442']/@id"))
	EdgeOut2=map(xmlAttr.getContent,ctxt.xpathEval("//edge[@from='2479049221']/@id"))
	return EdgeOut1,EdgeOut2

#initialisation de la liste des vehicules visitant chaque intersection

def juncVisitedVehID(ListInter):
	JuncVisitedVehID=len(ListInter)*range(1)
	i=0
	while i<len(JuncVisitedVehID):
		JuncVisitedVehID[i]=[]
		i=i+1
	return JuncVisitedVehID


#Liste des temps de passage de chaque lien sortant de l'intersection

def currentTravelEdgeOut(index,ListEdgeOut,step):
	CurrentTravelEdgeOut=[]
	for edge in ListEdgeOut[index]:
		#on recupere temps de passage sans vehicule (cas ideal)
		lane=edge+'_0'
		L=traci.lane.getLength(lane)
		S=traci.lane.getMaxSpeed(lane)
		#poids initial : longueur/Vitesse max
		T=L/S
		traci.edge.adaptTraveltime(edge,traci.edge.getTraveltime(edge))
		CurrentTravelEdgeOut.append(traci.edge.getAdaptedTraveltime(edge,step)-T)
	return CurrentTravelEdgeOut


#Liste des liens sortant les plus longs en temps de passage

def slowEdge(CurrentTravelEdgeOut,index,ListEdgeOut):
	l=0
	SlowEdge=[]
	#Liens sortant les plus rapides : la valeur 0 signifie qu'il n'y a personne sur la voie
	Min=min(CurrentTravelEdgeOut)
	#Liens sortant les plus longs : temps d'ecart avec la situation sans voiture
	Max=max(CurrentTravelEdgeOut)		
	while l<len(ListEdgeOut[index]):
		if (CurrentTravelEdgeOut[l]>Min):
			SlowEdge.append(ListEdgeOut[index][l])
		l=l+1
	return SlowEdge


#initialisation des poids des liens modifies a l'intersection

def updateEdgeWeight(SlowEdge,index):
	for edge in SlowEdge:
		lane=edge+'_0'
		L=traci.lane.getLength(lane)
		S=traci.lane.getMaxSpeed(lane)
		#poids initial : longueur/Vitesse max
		T=L/S
		traci.edge.adaptTraveltime(edge,T)
		



