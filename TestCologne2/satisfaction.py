import libxml2
from libxml2 import xmlAttr

#recuperation des temps de trajet des vehicules arrivees avec information partielle

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
identite= map(xmlAttr.getContent,ctxt.xpathEval("//@id"))

#recuperation des temps de trajet des memes vehicules sans information

doc2=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt2=doc2.xpathNewContext()
durationWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@duration"))
identiteWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@id"))

#Liste des vehicules ayant ete reroutes 

ListVehicleGreen=sys.argv[1]
ListVehicleQuick=sys.argv[2]
ListVehicleSmooth=sys.argv[3]

#energistrement de leur satisfaction (rapport des temps sans et avec information)

SatisfactionDurationGreen=[]
SatisfactionDurationQuick=[]
SatisfactionDurationSmooth=[]
for vehID in identite :
	if (vehID in ListVehicleGreen) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		SatisfactionDurationGreen.append(durationWO[j]/duration[i])
	if (vehID in ListVehicleQuick) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		SatisfactionDurationQuick.append(durationWO[j]/duration[i])	
	if (vehID in ListVehicleSmooth) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		SatisfactionDurationSmooth.append(durationWO[j]/duration[i])	

#on calcule la moyenne geometrique des satisfactions
SatisfactionDuration=SatisfactionDurationGreen+SatisfactionDurationQuick+SatisfactionDurationSmooth
result=1
for satisf in SatisfactionDuration:
	result=satisf*result

MeanSatisfaction=pow(result,1.0/float(len(SatisfactionDuration)))





