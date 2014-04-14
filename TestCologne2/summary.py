import libxml2
from libxml2 import xmlAttr

#recuperation des donnees de tous les vehicules
doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()
#en temps
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
#en attente
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
#en conso
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))

i=0
TotalDuration=0.0
TotalwaitSteps=0.0
TotalRouteLength=0.0
Totalfuel=0.0
#somme de resultats de chaque vehicule
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

#moyenne arithmetique
MeanDurationAll=(TotalDuration/len(duration))/60
MeanwaitStepsAll=TotalwaitSteps/len(waitSteps)
MeanFuelConsoAll=Totalfuel/len(fuel)
#maximum
MaxFAll=max(fuel)
MaxWAll=max(waitSteps)
MaxTAll=max(duration)
#minimu
MinFAll=min(fuel)
MinWAll=min(waitSteps)
MinTAll=min(duration)








