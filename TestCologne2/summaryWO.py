import libxml2
from libxml2 import xmlAttr
doc=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt=doc.xpathNewContext()

doc2=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt2=doc2.xpathNewContext()
identite=map(xmlAttr.getContent,ctxt2.xpathEval("//@id"))

identiteWO=map(xmlAttr.getContent,ctxt.xpathEval("//@id"))
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
routeLength= map(xmlAttr.getContent,ctxt.xpathEval("//@routeLength"))
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
i=0
TotalDuration=0.0
TotalwaitSteps=0.0
Totalfuel=0.0
Duration=[]

while i<len(duration):
	if identiteWO[i] in identite :
		duration[i]=float(duration[i])
		TotalDuration=TotalDuration+duration[i]
		waitSteps[i]=float(waitSteps[i])
		TotalwaitSteps=TotalwaitSteps+waitSteps[i]
		fuel[i]=float(fuel[i])
		Totalfuel=Totalfuel+fuel[i]
		Duration.append(duration[i])
	i=i+1

MeanDuration=(TotalDuration/len(Duration))/60
MeanwaitSteps=TotalwaitSteps/len(Duration)
MeanFuelConso=Totalfuel/len(Duration)

print "le temps moyen de parcours est de " + str(MeanDuration)
print "le temps d'attente moyen est de " + str(MeanwaitSteps)
print "Le nombre de vehicule est de : " + str(len(Duration))

