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


 
Density=["0.1"]
#,"0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1"]
NumVeh=[]
TravelWithDevice=[]
TravelWithout=[]
TravelLocal=[]


iteration=0
for density in Density:
	iteration=iteration+1
	changeValueDensity("data/map.sumocfg",density)
	execfile("runner.py")
	execfile("summary.py")
	TravelTime=MeanDuration
	NumberVehicle=len(duration)
	NumVeh.append(NumberVehicle)
	TravelWithDevice.append(float(TravelTime))


	changeValueDensity("data/mapWO.sumocfg",density)
	execfile("runnerWO.py")
	execfile("summaryWO.py")
	TravelTimeWO=MeanDuration
	TravelWithout.append(float(TravelTimeWO))
	
	X=[]
	Y=[]
	Z=[]
	b=0
	while b<1:


		changeValueDensity("data/mapLocal.sumocfg",density)
		green=random.randint(0,100)
		quick=random.randint(0,100)
		while green+quick>100:
			quick=random.randint(0,100)
	
		smooth=100-green-quick
		sys.argv=["runnerLocal2.py",green,quick,smooth]
		execfile("runnerLocal2.py")	
		execfile("summaryLocal.py")
		TravelTimeLocal=MeanDuration
		#TravelLocal.append(TravelTimeLocal)
		T=float(TravelTimeLocal)/float(green+quick+smooth)
		X.append(green*T)
		Y.append(quick*T)
		Z.append(smooth*T)
		print b
		print X
	
		b=b+1
	Sum=[]
	N = b
	r=0
	while r<len(X):
		Sum.append(X[r]+Y[r])
		r=r+1


	ind = np.arange(N)    
	width = 0.2      # the width of the bars


	WO=[]
	Tot=[]
	for indice in list(ind):
		Tot.append([indice,TravelWithDevice[iteration-1]])
		WO.append([indice,TravelWithout[iteration-1]])

	



	p1 = plt.bar(ind, X, width, color='g')
	p2 = plt.bar(ind, Y, width, color='r',bottom=X)
	p3 = plt.bar(ind, Z, width, color='b', bottom=Sum)

	plt.plot(*zip(*WO), color='m', label='without')
	plt.plot(*zip(*Tot), color='y', label='Total')
	#plt.plot(*zip(*Local), color='m', label='Local')


	plt.ylabel('TravelTime min')
	plt.title(str(NumVeh[iteration-1])+" cars, density = "+ str(Density[iteration-1]))
	#plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
	#plt.yticks(np.arange(0,81,10))
	plt.legend( (p1[0],p2[0],p3[0]), ('GreenWay', 'QuickWay','SmoothWay') )

	plt.figure()

plt.show()

