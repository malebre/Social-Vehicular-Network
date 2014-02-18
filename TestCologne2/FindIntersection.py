#!/usr/bin/env python
import os,subprocess,sys,shutil,sumolib
Wait=1000
Duration=1000
L=[]
execfile("summaryLocal.py")
number=sys.argv[1]
y=0
while y<int(number):
	execfile("runnerLocal2.py")
	print "les resultats sont :" 
	execfile("summaryLocal.py")
	if MeanDuration<Duration and MeanwaitSteps<Wait:
		Duration=MeanDuration
		Wait=MeanwaitSteps
		L=Liste
	y=y+1
print L
