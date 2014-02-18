import libxml2
from libxml2 import xmlAttr
doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
i=0
TotalDuration=0.0
TotalwaitSteps=0.0
Totalfuel=0.0
while i<len(duration):
	duration[i]=float(duration[i])
	TotalDuration=TotalDuration+duration[i]
	waitSteps[i]=float(waitSteps[i])
	TotalwaitSteps=TotalwaitSteps+waitSteps[i]
	fuel[i]=float(fuel[i])
	Totalfuel=Totalfuel+fuel[i]
	i=i+1

MeanDuration=(TotalDuration/len(duration))/60
MeanwaitSteps=TotalwaitSteps/len(waitSteps)
MeanFuelConso=Totalfuel/len(fuel)

#print "la conso moyenne est de" + str(MeanFuelConso) + "ml"
#print "Le parcours moyen en temps est " + str(MeanDuration) +" min"
#print "Le temps moyen d'attente par vehicule est : " + str(MeanwaitSteps) +" s"
#print "Le nombre de vehicule est de : " + str(len(duration))
#print "maximum de temps d'attente :" + str(max(waitSteps)) + "s"
#print "maximum temps de parcours :" + str(max(duration)/60) + "min"




