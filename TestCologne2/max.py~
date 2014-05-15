#!/usr/bin/env python
import os,subprocess,sys,shutil,sumolib
from sumolib import checkBinary
import traci,libxml2,random
from libxml2 import xmlAttr

doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Ftout=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
veh=map(xmlAttr.getContent,ctxt.xpathEval("//@id"))


doc=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Fsans=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Flocal=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))

k=i=j=0
while k<len(Ftout):
	Ftout[k]=float(Ftout[k])
	k=k+1
while i<len(Fsans):
	Fsans[i]=float(Fsans[i])
	i=i+1
while j<len(Flocal):
	Flocal[j]=float(Flocal[j])
	j=j+1

print "max local"
print max(Flocal)

print "max tout"
print max(Ftout)
endroit=Ftout.index(max(Ftout))
print veh[endroit]

print "max sans"
print max(Fsans)

