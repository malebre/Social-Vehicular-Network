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

 
Density=["0.8"]
NumVeh=[]
TravelWithDevice=[]
TravelWithout=[]
TravelLocal=[]
ConsoWithDevice=[]
ConsoWithout=[]
ConsoLocal=[]
ValueApp=[]


iteration=0
for density in Density:
	iteration=iteration+1
	changeValueDensity("data/map.sumocfg",density)
	execfile("runner.py")
	time.sleep(2)
	execfile("summary.py")
	TravelTime=MeanDuration
	Conso=MeanFuelConso
	NumberVehicle=len(duration)
	NumVeh.append(NumberVehicle)
	TravelWithDevice.append(float(TravelTime))
	ConsoWithDevice.append(float(MeanFuelConso))


	changeValueDensity("data/mapWO.sumocfg",density)
	execfile("runnerWO.py")
	time.sleep(2)
	execfile("summaryWO.py")
	TravelTimeWO=MeanDuration
	ConsoWO=MeanFuelConso
	TravelWithout.append(float(TravelTimeWO))
	ConsoWithout.append(float(ConsoWO))

	GTravel=[]
	QTravel=[]
	STravel=[]

	GConso=[]
	QConso=[]
	SConso=[]
	listeCoeff=[[12, 88, 0],[14, 82, 4],[70, 13, 17],[39, 20, 41],[28, 16, 56],[29, 0, 71],[5, 4, 91]]
	b=0
	while b<len(listeCoeff):


		changeValueDensity("data/mapLocal.sumocfg",density)
		
		#green=random.randint(0,100)
		#quick=random.randint(0,100)
		#while green+quick>100:
			#quick=random.randint(0,100)
	
		#smooth=100-green-quick
		
		green=listeCoeff[b][0]
		quick=listeCoeff[b][1]
		smooth=listeCoeff[b][2]
		sys.argv=["runnerLocal2.py",green,quick,smooth]
		execfile("runnerLocal2.py")
		time.sleep(2)	
		execfile("summaryLocal.py")
		TravelTimeLocal=MeanDuration
		ConsoLocal=MeanFuelConso
		#TravelLocal.append(TravelTimeLocal)
		T=float(TravelTimeLocal)/float(green+quick+smooth)
		C=float(ConsoLocal)/float(green+quick+smooth)
		GTravel.append(green*T)
		QTravel.append(quick*T)
		STravel.append(smooth*T)

		GConso.append(green*C)
		QConso.append(quick*C)
		SConso.append(smooth*C)
		print b
		ValueApp.append([green,quick,smooth,density])

	
		b=b+1
	Sum1=[]
	Sum2=[]
	N = b
	r=0
	while r<len(GTravel):
		Sum1.append(GTravel[r]+QTravel[r])
		Sum2.append(GConso[r]+QConso[r])
		r=r+1


	ind = np.arange(N)   
	width = 0.2      # the width of the bars


	WOTotal=[]
	TotTotal=[]
	WOConso=[]
	TotConso=[]
	list(ind)[len(list(ind))-1] = list(ind)[len(list(ind))-1]+0.2
	for indice in list(ind):
		TotTotal.append([indice,TravelWithDevice[iteration-1]])
		WOTotal.append([indice,TravelWithout[iteration-1]])
		TotConso.append([indice,ConsoWithDevice[iteration-1]])
		WOConso.append([indice,ConsoWithout[iteration-1]])


	
	p1 = plt.bar(ind, GTravel, width, color='g')
	p2 = plt.bar(ind, QTravel, width, color='r',bottom=GTravel)
	p3 = plt.bar(ind, STravel, width, color='b', bottom=Sum1)

	plt.plot(*zip(*WOTotal), color='m', label='without')
	plt.plot(*zip(*TotTotal), color='y', label='Total')
	
	

	plt.ylabel('TravelTime')
	plt.title(str(NumVeh[iteration-1])+" cars, density = "+ str(Density[iteration-1]))
	plt.legend( (p1[0],p2[0],p3[0]), ('GreenWay', 'QuickWay','SmoothWay') )

	plt.figure()


	p4 = plt.bar(ind, GConso, width, color='g')
	p5 = plt.bar(ind, QConso, width, color='r',bottom=GConso)
	p6 = plt.bar(ind, SConso, width, color='b', bottom=Sum2)

	plt.plot(*zip(*WOConso), color='m', label='without')
	plt.plot(*zip(*TotConso), color='y', label='Total')
	

	plt.ylabel('Conso')
	plt.title(str(NumVeh[iteration-1])+" cars, density = "+ str(Density[iteration-1]))
	plt.legend( (p4[0],p5[0],p6[0]), ('GreenWay', 'QuickWay','SmoothWay') )
	
	plt.figure()


plt.show()
print ValueApp

