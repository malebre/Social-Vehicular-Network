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
	listeCoeff=[[0,100,0]]
#[0,100,0],[12, 88, 0],[14, 82, 4],[18, 65, 17] [26, 49, 25],[62, 20, 18],[62, 30, 8],[70, 13, 17],[84, 2, 14],[97, 1, 2],[0,100,0],[39, 20, 41],[28, 16, 56],[29, 0, 71],[5, 4, 91],[0,0,100]]

	b=0
	while b< len(listeCoeff):

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
			RateMinWaitGreen=MinWG/WMinWG


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
			RateMinWaitQuick=MinWQ/WMinWQ
			

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
			RateMinWaitSmooth=MinWS/WMinWS


		
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
		RateMinWait=MinW/WMinW

##############################################################################################################

#Avec toutes la connaissance

##############################################################################################################


		#simulation avec toutes la connaissance dans le reseau
		changeValueDensity("data/map.sumocfg",density)
		sys.argv=["runner.py",ListGreen,ListQuick,ListSmooth,CompromisTempsConso]
		execfile("runner.py")
		time.sleep(2)


##############################################################################################################

#Avec toute la connaissance : Resultats en moyenne arithmetique (rapport avec sans connaissance)

##############################################################################################################

		#resultat : on compare au cas sans connaissance
		execfile("summary.py")

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
		RateMinWaitAll=MinTAll/WMinT

##############################################################################################################

#Satisfaction : moyenne geometrique (rapport avec sans connaissance)

##############################################################################################################

		time.sleep(2)
		#resultat satisfaction
		sys.argv=["satisfaction.py",ListGreen,ListQuick,ListSmooth]
		execfile("satisfaction.py")
		time.sleep(2)

		#satisfaction de la connaissance locale par rapport a sans connaissance
		RateSatisfactionGreen=MeanSatisfactionGreen
		RateSatisfactionQuick=MeanSatisfactionQuick
		RateSatisfactionSmooth=MeanSatisfactionSmooth

		#satisfaction de la connaissance totale par rapport a sans connaissance
		RateSatisfactionGreenAll=MeanSatisfactionGreenAll
		RateSatisfactionQuickAll=MeanSatisfactionQuickAll
		RateSatisfactionSmoothAll=MeanSatisfactionSmoothAll


##############################################################################################################

#Diagramme Radar

##############################################################################################################

		#resultat : diagramme radar
RadarG=[[RateSatisfactionQuick,RateTravelTimeLocalQuick,RateConsoLocalQuick,RateWaitLocalQuick,RateMinFuelQuick,RateMaxFuelQuick,RateMinTimeQuick,RateMaxTimeQuick,RateMinWaitQuick,RateMaxWaitQuick],[RateSatisfactionQuickAll,RateTravelTimeAll,RateConsoAll,RateWaitAll,RateMaxFuelAll,RateMaxWaitAll,RateMaxTimeAll,RateMinFuelAll,RateMinWaitAll,RateMinTimeAll],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
		print RadarG 



		#show figure
		sys.argv=["test.py",RadarG]
		execfile("test.py")

	



