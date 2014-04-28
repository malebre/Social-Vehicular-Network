#!/usr/bin/env python
import os,subprocess,sys,shutil,sumolib
from sumolib import checkBinary
import traci,libxml2,random
from libxml2 import xmlAttr

doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Ftout=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))


doc=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Fsans=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()

#coordonnees des intersections autre que les feux
Flocal=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))


for i in Flocal:
	i=float(i)
for j in Fsans:
	j=float(j)
for k in Ftout:
	k=float(k)

print "max local"
print max(Flocal)

print "max tout"
print max(Ftout)

print "max sans"
print max(Fsans)

