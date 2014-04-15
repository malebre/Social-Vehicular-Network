import libxml2
from libxml2 import xmlAttr

#recuperation des donnees de tous les vehicules
#####################################################################
doc=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt=doc.xpathNewContext()
#en temps
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
#en attente
waitSteps= map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
#en conso
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
#id des vehicules
veh=map(xmlAttr.getContent,ctxt.xpathEval("//@id"))

####################################################################

#Liste des indentifiants des vehicules dans chaque applications

ListGreen=sys.argv[1]
ListQuick=sys.argv[2]
ListSmooth=sys.argv[3]

####################################################################

#Initialisation des donnees

i=0
#temps Green/Quick/Smooth/total 
TotalDurationGreen=TotalDurationQuick=TotalDurationSmooth=TotalDuration=0.0
#attente
TotalwaitStepsGreen=TotalwaitStepsQuick=TotalwaitStepsSmooth=TotalwaitSteps=0.0
#conso
TotalfuelGreen=TotalfuelQuick=TotalfuelSmooth=Totalfuel=0.0
#maximum
MaxTAll=MaxWAll=MaxFAll=MaxTGAll=MaxWGAll=MaxFGAll=MaxTQAll=MaxWQAll=MaxFQAll=MaxTSAll=MaxWSAll=MaxFSAll=0.0
#minimum
MinTAll=MinWAll=MinFAll=MinTGAll=MinWGAll=MinFGAll=MinTQAll=MinWQAll=MinFQAll=MinTSAll=MinWSAll=MinFSAll=1000000.0

####################################################################

#somme de resultats de chaque vehicule
while i<len(duration):

	
	#Green
	if veh[i] in ListGreen:
		#temps
		duration[i]=float(duration[i])
		if duration[i]>MaxTGAll:
			MaxTGAll=duration[i]
		if duration[i]<MinTGAll:
			MinTGAll=duration[i]
		TotalDurationGreen=TotalDurationGreen+duration[i]
		TotalDuration=TotalDuration+duration[i]
		#attente
		waitSteps[i]=float(waitSteps[i])
		if waitSteps[i]>MaxWGAll:
			MaxWGAll=waitSteps[i]
		if waitSteps[i]<MinWGAll:
			MinWGAll=waitSteps[i]
		TotalwaitStepsGreen=TotalwaitStepsGreen+waitSteps[i]
		TotalwaitSteps=TotalwaitSteps+waitSteps[i]
		#conso
		fuel[i]=float(fuel[i])
		if fuel[i]>MaxFGAll:
			MaxFGAll=fuel[i]
		if fuel[i]<MinFGAll:
			MinFGAll=fuel[i]
		TotalfuelGreen=TotalfuelGreen+fuel[i]
		Totalfuel=Totalfuel+fuel[i]
	
	#Quick
	if veh[i] in ListQuick:
		#temps
		duration[i]=float(duration[i])
		if duration[i]>MaxTQAll:
			MaxTQAll=duration[i]
		if duration[i]<MinTQAll:
			MinTQAll=duration[i]
		TotalDurationQuick=TotalDurationQuick+duration[i]
		TotalDuration=TotalDuration+duration[i]
		#attente
		waitSteps[i]=float(waitSteps[i])
		if waitSteps[i]>MaxWQAll:
			MaxWQAll=waitSteps[i]
		if waitSteps[i]<MinWQAll:
			MinWQAll=waitSteps[i]
		TotalwaitStepsQuick=TotalwaitStepsQuick+waitSteps[i]
		TotalwaitSteps=TotalwaitSteps+waitSteps[i]
		#conso
		fuel[i]=float(fuel[i])
		if fuel[i]>MaxFQAll:
			MaxFQAll=fuel[i]
		if fuel[i]<MinFQAll:
			MinFQAll=fuel[i]
		TotalfuelQuick=TotalfuelQuick+fuel[i]
		Totalfuel=Totalfuel+fuel[i]

	#Smooth
	if veh[i] in ListSmooth:
		#temps
		duration[i]=float(duration[i])
		if duration[i]>MaxTSAll:
			MaxTSAll=duration[i]
		if duration[i]<MinTSAll:
			MinTSAll=duration[i]
		TotalDurationSmooth=TotalDurationSmooth+duration[i]
		TotalDuration=TotalDuration+duration[i]
		#attente
		waitSteps[i]=float(waitSteps[i])
		if waitSteps[i]>MaxWSAll:
			MaxWSAll=waitSteps[i]
		if waitSteps[i]<MinWSAll:
			MinWSAll=waitSteps[i]
		TotalwaitStepsSmooth=TotalwaitStepsSmooth+waitSteps[i]
		TotalwaitSteps=TotalwaitSteps+waitSteps[i]
		#conso
		fuel[i]=float(fuel[i])
		if fuel[i]>MaxFSAll:
			MaxFSAll=fuel[i]
		if fuel[i]<MinFSAll:
			MinFSAll=fuel[i]
		TotalfuelSmooth=TotalfuelSmooth+fuel[i]
		Totalfuel=Totalfuel+fuel[i]
	i=i+1

####################################################################

#moyenne arithmetique Green
if len(ListGreen)>0:
	MeanDurationGreenAll=(TotalDurationGreen/len(ListGreen))/60
	MeanwaitStepsGreenAll=TotalwaitStepsGreen/len(ListGreen)
	MeanFuelConsoGreenAll=TotalfuelGreen/len(ListGreen)
else:
	MeanDurationGreenAll=MeanwaitStepsGreenAll=MeanFuelConsoGreenAll=0

####################################################################

#moyenne arithmetique Quick
if len(ListQuick)>0:
	MeanDurationQuickAll=(TotalDurationQuick/len(ListQuick))/60
	MeanwaitStepsQuickAll=TotalwaitStepsQuick/len(ListQuick)
	MeanFuelConsoQuickAll=TotalfuelQuick/len(ListQuick)
else:
	MeanDurationQuickAll=MeanwaitStepsQuickAll=MeanFuelConsoQuickAll=0

####################################################################

#moyenne arithmetique Smooth
if len(ListSmooth)>0:
	MeanDurationSmoothAll=(TotalDurationSmooth/len(ListSmooth))/60
	MeanwaitStepsSmoothAll=TotalwaitStepsSmooth/len(ListSmooth)
	MeanFuelConsoSmoothAll=TotalfuelSmooth/len(ListSmooth)
else:
	MeanDurationSmoothAll=MeanwaitStepsSmoothAll=MeanFuelConsoSmoothAll=0

####################################################################

#moyenne arithmetique tot
MeanDurationAll=(TotalDuration/len(duration))/60
MeanwaitStepsAll=TotalwaitSteps/len(duration)
MeanFuelConsoAll=Totalfuel/len(duration)

####################################################################

#maximum et minimum
MaxTAll=float(max(duration))
MaxWAll=float(max(waitSteps))
MaxFAll=float(max(fuel))
MinTAll=float(min(duration))
MinWAll=float(min(waitSteps))
MinFAll=float(min(fuel))






