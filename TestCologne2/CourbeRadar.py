#!/usr/bin/env python
import os,subprocess,sys,shutil,sumolib
import libxml2
from libxml2 import xmlAttr
from numpy import arange,array,ones,linalg
from pylab import plot,show
from ChangeValueDensity import changeValueDensity
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.pyplot as plt
import time



#communication=sys.argv[1]

##############################################################################################################

#Initialisation

##############################################################################################################

#Densite des vehicules par rapport aux donnees brutes
Density=["0.8"]

#Nombre de vehicules arrives a destination
NumVeh=[]

#Temps de parcours avec toutes les infos
TravelWithDevice=[]
#Temps de parcours donnees brutes
TravelWithout=[]

#Consommation avec toutes les infos
ConsoWithDevice=[]
#Temps de parcours donnees brutes
ConsoWithout=[]

#Temps d'attente avec toutes les infos
WaitWithDevice=[]
#Temps d'attente sans les infos
WaitWithout=[]

##############################################################################################################

#Simulation

##############################################################################################################

for density in Density:

##############################################################################################################

#Sans connaissance

##############################################################################################################

	#simulation des donnees brutes : sans informations
	changeValueDensity("data/mapWO.sumocfg",density)
	execfile("runnerWO.py")
	time.sleep(2)



	#repartition selon les applis : [Green,Quick,Smooth]
	listeCoeff=[[100,0,0],[12, 88, 0],[14, 82, 4],[18, 65, 17],[26, 49, 25]]
#[100,0,0],[12, 88, 0],[14, 82, 4],[18, 65, 17] [26, 49, 25],[62, 20, 18],[62, 30, 8],[70, 13, 17],[84, 2, 14],[97, 1, 2],[0,100,0],[39, 20, 41],[28, 16, 56],[29, 0, 71],[5, 4, 91],[0,0,100]]

	b=0
	while b<len(listeCoeff):

		#permet de changer la densite : plus ou moins de congestion
		changeValueDensity("data/mapLocal.sumocfg",density)

		#pourcentage de vehicule dans Green, Quick et Smooth		
		green=listeCoeff[b][0]
		quick=listeCoeff[b][1]
		smooth=listeCoeff[b][2]

##############################################################################################################

#Avec connaissance locale

##############################################################################################################


		#simulation avec connaissance locale
		sys.argv=["runnerLocal2.py",green,quick,smooth,'no']
		execfile("runnerLocal2.py")

		#Liste des vehicule ayant choisi Green,Quick ou Smooth
		ListGreen=ListGreenWay
		ListQuick=ListQuickWay
		ListSmooth=ListSmoothWay
		#parametre de compromis temps/conso pour Smooth : 0<r<1 choisi au hasard pour chaque vehicule
		CompromisTempsConso=Compromis

##############################################################################################################

#Avec connaissance locale : Resultats en moyenne arithmetique (rapport avec sans connaissance)

##############################################################################################################


		time.sleep(2)
		#resultat : on compare au cas sans connaissance
		sys.argv=["summaryLocal.py",ListGreen,ListQuick,ListSmooth]
		execfile("summaryLocal.py")
		time.sleep(2)
		
		#pour Green
		if len(ListGreen)>0:

			#temps
			RateTravelTimeLocalGreen=MeanDurationGreen/MeanDurationGreenW
			RateMaxTimeGreen=MaxTG/WMaxTG
			RateMinTimeGreen=MinTG/WMinTG
			#conso
			RateConsoLocalGreen=MeanFuelConsoGreen/MeanFuelConsoGreenW
			RateMaxFuelGreen=MaxFG/WMaxFG
			RateMinFuelGreen=MinFG/WMinFG
			#attente
			RateWaitLocalGreen=MeanwaitStepsGreen/MeanwaitStepsGreenW
			RateMaxWaitGreen=MaxWG/WMaxWG



		#pour Quick
		if len(ListQuick)>0:


			#temps
			RateTravelTimeLocalQuick=MeanDurationQuick/MeanDurationQuickW
			RateMaxTimeQuick=MaxTQ/WMaxTQ
			RateMinTimeQuick=MinTQ/WMinTQ
			#conso
			RateConsoLocalQuick=MeanFuelConsoQuick/MeanFuelConsoQuickW
			RateMaxFuelQuick=MaxFQ/WMaxFQ
			RateMinFuelQuick=MinFQ/WMinFQ
			#attente
			RateWaitLocalQuick=MeanwaitStepsQuick/MeanwaitStepsQuickW
			RateMaxWaitQuick=MaxWQ/WMaxWQ

			

		#pour Smooth
		if len(ListSmooth)>0:


			#temps
			RateTravelTimeLocalSmooth=MeanDurationSmooth/MeanDurationSmoothW
			RateMaxTimeSmooth=MaxTS/WMaxTS
			RateMinTimeSmooth=MinTS/WMinTS
			#conso
			RateConsoLocalSmooth=MeanFuelConsoSmooth/MeanFuelConsoSmoothW
			RateMaxFuelSmooth=MaxFS/WMaxFS
			RateMinFuelSmooth=MinFS/WMinFS
			#attente
			RateWaitLocalSmooth=MeanwaitStepsSmooth/MeanwaitStepsSmoothW
			RateMaxWaitSmooth=MaxWS/WMaxWS



		
		#total
		#temps
		RateTravelTimeLocal=MeanDuration/MeanDurationW
		RateMaxTime=MaxT/WMaxT
		RateMinTime=MinT/WMinT
		#conso
		RateConsoLocal=MeanFuelConso/MeanFuelConsoW
		RateMaxFuel=MaxF/WMaxF
		RateMinFuel=MinF/WMinF
		#attente
		RateWaitLocal=MeanwaitSteps/MeanwaitStepsW
		RateMaxWait=MaxW/WMaxW


##############################################################################################################

#Avec toutes la connaissance

##############################################################################################################


		#simulation avec toutes la connaissance dans le reseau
		changeValueDensity("data/map.sumocfg",density)
		sys.argv=["runner.py",ListGreen,ListQuick,ListSmooth,CompromisTempsConso]
		execfile("runner.py")
		time.sleep(4)


##############################################################################################################

#Avec toute la connaissance : Resultats en moyenne arithmetique (rapport avec sans connaissance)

##############################################################################################################

		#resultat : on compare au cas sans connaissance
		sys.argv=["summary.py",ListGreen,ListQuick,ListSmooth]
		execfile("summary.py")

		#pour Green
		if len(ListGreen)>0:

			#temps
			RateTravelTimeGreenAll=MeanDurationGreenAll/MeanDurationGreenW
			RateMaxTimeGreenAll=MaxTGAll/WMaxTG
			RateMinTimeGreenAll=MinTGAll/WMinTG
			#conso
			RateConsoGreenAll=MeanFuelConsoGreenAll/MeanFuelConsoGreenW
			RateMaxFuelGreenAll=MaxFGAll/WMaxFG
			RateMinFuelGreenAll=MinFGAll/WMinFG
			#attente
			RateWaitGreenAll=MeanwaitStepsGreenAll/MeanwaitStepsGreenW
			RateMaxWaitGreenAll=MaxWGAll/WMaxWG



		#pour Quick
		if len(ListQuick)>0:


			#temps
			RateTravelTimeQuickAll=MeanDurationQuickAll/MeanDurationQuickW
			RateMaxTimeQuickAll=MaxTQAll/WMaxTQ
			RateMinTimeQuickAll=MinTQAll/WMinTQ
			#conso
			RateConsoQuickAll=MeanFuelConsoQuickAll/MeanFuelConsoQuickW
			RateMaxFuelQuickAll=MaxFQAll/WMaxFQ
			RateMinFuelQuickAll=MinFQAll/WMinFQ
			#attente
			RateWaitQuickAll=MeanwaitStepsQuickAll/MeanwaitStepsQuickW
			RateMaxWaitQuickAll=MaxWQAll/WMaxWQ

			

		#pour Smooth
		if len(ListSmooth)>0:


			#temps
			RateTravelTimeSmoothAll=MeanDurationSmoothAll/MeanDurationSmoothW
			RateMaxTimeSmoothAll=MaxTSAll/WMaxTS
			RateMinTimeSmoothAll=MinTSAll/WMinTS
			#conso
			RateConsoSmoothAll=MeanFuelConsoSmoothAll/MeanFuelConsoSmoothW
			RateMaxFuelSmoothAll=MaxFSAll/WMaxFS
			RateMinFuelSmoothAll=MinFSAll/WMinFS
			#attente
			RateWaitSmoothAll=MeanwaitStepsSmoothAll/MeanwaitStepsSmoothW
			RateMaxWaitSmoothAll=MaxWSAll/WMaxWS





		#total
		#temps
		RateTravelTimeAll=MeanDurationAll/MeanDurationW
		RateMaxTimeAll=MaxTAll/WMaxT
		RateMinTimeAll=MinTAll/WMinT
		#conso
		RateConsoAll=MeanFuelConsoAll/MeanFuelConsoW
		RateMaxFuelAll=MaxFAll/WMaxF
		RateMinFuelAll=MinFAll/WMinF
		#attente
		RateWaitAll=MeanwaitStepsAll/MeanwaitStepsW
		RateMaxWaitAll=MaxWAll/WMaxW


##############################################################################################################

#Satisfaction : moyenne geometrique (rapport avec sans connaissance)

##############################################################################################################

		time.sleep(2)
		#resultat satisfaction
		sys.argv=["satisfaction.py",ListGreen,ListQuick,ListSmooth,CompromisTempsConso]
		execfile("satisfaction.py")
		time.sleep(2)

		#satisfaction de la connaissance locale par rapport a sans connaissance Green
		RateSatisfactionGreen=MeanSatisfactionGreen
		RateSatisfactionQuick=MeanSatisfactionQuick
		RateSatisfactionSmooth=MeanSatisfactionSmooth

		#satisfaction de la connaissance totale par rapport a sans connaissance Quick
		RateSatisfactionGreenAll=MeanSatisfactionGreenAll
		RateSatisfactionQuickAll=MeanSatisfactionQuickAll
		RateSatisfactionSmoothAll=MeanSatisfactionSmoothAll

		#satisfaction de la connaissance totale par rapport a sans connaissance Smooth
		RateSatisfaction=MeanSatisfaction
		RateSatisfactionAll=MeanSatisfactionAll



##############################################################################################################

#Diagramme Radar

##############################################################################################################

		#resultat : diagramme radar

		#Green
		if len(ListGreen)>0:
			RadarG=[[RateSatisfactionGreen,RateTravelTimeLocalGreen,RateConsoLocalGreen,RateWaitLocalGreen,RateMinFuelGreen,RateMaxFuelGreen,RateMinTimeGreen,RateMaxTimeGreen,RateMaxWaitGreen],[RateSatisfactionGreenAll,RateTravelTimeGreenAll,RateConsoGreenAll,RateWaitGreenAll,RateMinFuelGreenAll,RateMaxFuelGreenAll,RateMinTimeGreenAll,RateMaxTimeGreenAll,RateMaxWaitGreenAll],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
			print "Green"
			print RadarG
		else: 
			RadarG=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


		#Quick
		if len(ListQuick)>0:
			RadarQ=[[RateSatisfactionQuick,RateTravelTimeLocalQuick,RateConsoLocalQuick,RateWaitLocalQuick,RateMinFuelQuick,RateMaxFuelQuick,RateMinTimeQuick,RateMaxTimeQuick,RateMaxWaitQuick],[RateSatisfactionQuickAll,RateTravelTimeQuickAll,RateConsoQuickAll,RateWaitQuickAll,RateMinFuelQuickAll,RateMaxFuelQuickAll,RateMinTimeQuickAll,RateMaxTimeQuickAll,RateMaxWaitQuickAll],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
			print "Quick"
			print RadarQ
		else :
			RadarQ=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


		#Smooth
		if len(ListSmooth)>0:
			RadarS=[[RateSatisfactionSmooth,RateTravelTimeLocalSmooth,RateConsoLocalSmooth,RateWaitLocalSmooth,RateMinFuelSmooth,RateMaxFuelSmooth,RateMinTimeSmooth,RateMaxTimeSmooth,RateMaxWaitSmooth],[RateSatisfactionSmoothAll,RateTravelTimeSmoothAll,RateConsoSmoothAll,RateWaitSmoothAll,RateMinFuelSmoothAll,RateMaxFuelSmoothAll,RateMinTimeSmoothAll,RateMaxTimeSmoothAll,RateMaxWaitSmoothAll],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
			print "Smooth"
			print RadarS
		else:
			RadarS=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


		#total
		RadarAll=[[RateSatisfaction,RateTravelTimeLocal,RateConsoLocal,RateWaitLocal,RateMinFuel,RateMaxFuel,RateMinTime,RateMaxTime,RateMaxWait],[RateSatisfactionAll,RateTravelTimeAll,RateConsoAll,RateWaitAll,RateMinFuelAll,RateMaxFuelAll,RateMinTimeAll,RateMaxTimeAll,RateMaxWaitAll],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
		print "All"
		print RadarAll


		#show figure
		sys.argv=["test.py",RadarG,RadarQ,RadarS,RadarAll,listeCoeff[b]]
		execfile("test.py")

		b=b+1

plt.show()

	



