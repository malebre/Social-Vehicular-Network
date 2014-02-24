import libxml2
from libxml2 import xmlAttr
doc=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
routeLength= map(xmlAttr.getContent,ctxt.xpathEval("//@routeLength"))
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


