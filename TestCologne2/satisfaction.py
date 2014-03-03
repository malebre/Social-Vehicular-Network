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

ListVehicle=sys.argv[1]


#energistrement de leur satisfaction (rapport des temps sans et avec information)

SatisfactionDuration=[]
for vehID in identite :
	if (vehID in ListVehicle) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[i]=float(durationWO[i])
		SatisfactionDuration.append(durationWO[i]/duration[i])

#on calcule la moyenne geometrique des satisfactions

result=1
for satisf in SatisfactionDuration:
	result=satisf*result

MeanSatisfaction=pow(result,1.0/float(len(SatisfactionDuration)))





