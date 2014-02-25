import libxml2
from libxml2 import xmlAttr
doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
routeLength= map(xmlAttr.getContent,ctxt.xpathEval("//@routeLength"))
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
print len(fuel)
print len(duration)
i=0
TotalDuration=0.0
TotalwaitSteps=0.0
TotalRouteLength=0.0
Totalfuel=0.0
while i<len(duration):
	duration[i]=float(duration[i])
	TotalDuration=TotalDuration+duration[i]
	waitSteps[i]=float(waitSteps[i])
	TotalwaitSteps=TotalwaitSteps+waitSteps[i]
	routeLength[i]=float(routeLength[i])
	TotalRouteLength=TotalRouteLength+routeLength[i]
	fuel[i]=float(fuel[i])
	Totalfuel=Totalfuel+fuel[i]
	i=i+1

MeanDuration=(TotalDuration/len(duration))/60
MeanwaitSteps=TotalwaitSteps/len(waitSteps)
MeanRouteLength=TotalRouteLength/len(routeLength)
MeanFuelConso=Totalfuel/len(fuel)

print "Le temps moyen d'attente par vehicule est : " + str(MeanwaitSteps) +" s"
print "Le nombre de vehicule est de : " + str(len(duration))
print "maximum de temps d'attente :" + str(max(waitSteps)) + "s"
print "maximum temps de parcours :" + str(max(duration)/60) + "min"
print "le parcours moyen en km est de :" + str(MeanRouteLength/1000)
print "le temps de parcours moyen est de :"+str(MeanDuration)





