import libxml2
from libxml2 import xmlAttr
doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
routeLength= map(xmlAttr.getContent,ctxt.xpathEval("//@routeLength"))
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
i=0
TotalDuration=0.0
while i<len(duration):
	duration[i]=float(duration[i])
	TotalDuration=TotalDuration+duration[i]
	i=i+1

MeanDuration=(TotalDuration/len(duration))/60
print "Le parcours moyen en temps est " + str(MeanDuration) +" min"
j=0
TotalwaitSteps=0.0
while j<len(waitSteps):
	waitSteps[j]=float(waitSteps[j])
	TotalwaitSteps=TotalwaitSteps+waitSteps[j]
	j=j+1

MeanwaitSteps=TotalwaitSteps/len(waitSteps)

print "Le temps moyen d'attente par vehicule est : " + str(MeanwaitSteps) +" s"
print "Le nombre de vehicule est de : " + str(len(duration))
print "maximum de temps d'attente :" + str(max(waitSteps)) + "s"
print "maximum temps de parcours :" + str(max(duration)/60) + "min"




