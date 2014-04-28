import libxml2
from libxml2 import xmlAttr

#####################################################

#Simulation avec reroutage, recuperation :
#temps de parcours
#temps d'attente
#consommation
#identifiant 

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()
duration=map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
waitSteps=map(xmlAttr.getContent,ctxt.xpathEval("//@waitSteps"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs"))
veh=map(xmlAttr.getContent,ctxt.xpathEval("//@id"))

#####################################################

#Simulation sans reroutage, recuperation :
#temps de parcours
#temps d'attente
#consommation
#identifiant 

docW=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxtW=docW.xpathNewContext()
durationW=map(xmlAttr.getContent,ctxtW.xpathEval("//@duration"))
waitStepsW=map(xmlAttr.getContent,ctxtW.xpathEval("//@waitSteps"))
fuelW=map(xmlAttr.getContent,ctxtW.xpathEval("//@fuel_abs"))
vehW=map(xmlAttr.getContent,ctxtW.xpathEval("//@id"))

#####################################################

#Liste des indentifiants des vehicules dans chaque applications

ListGreen=sys.argv[1]
ListQuick=sys.argv[2]
ListSmooth=sys.argv[3]
List=ListGreen+ListQuick+ListSmooth





#####################################################

#initialisation des parametres
i=0

#Avec reroutage Local
#Temps total
TotalDurationGreen=TotalDuration=TotalDurationQuick=TotalDurationSmooth=0.0
#Temps d'attente
TotalwaitStepsGreen=TotalwaitStepsQuick=TotalwaitStepsSmooth=TotalwaitSteps=0.0
#Consommation
TotalfuelGreen=TotalfuelQuick=TotalfuelSmooth=Totalfuel=0.0
#Maximum et Minimum
MaxT=MaxTG=MaxTQ=MaxTS=0.0
MinT=MinTG=MinTQ=MinTS=100000000000.0
MaxW=MaxWG=MaxWQ=MaxWS=MaxF=MaxFG=MaxFQ=MaxFS=0.0
MinW=MinWG=MinWQ=MinWS=MinF=MinFG=MinFQ=MinFS=10000000.0


#Sans reroutage 'W'
#Temps total
TotalDurationGreenW=TotalDurationW=TotalDurationQuickW=TotalDurationSmoothW=0.0
#Temps d'attente
TotalwaitStepsGreenW=TotalwaitStepsQuickW=TotalwaitStepsSmoothW=TotalwaitStepsW=0.0
#Consommation
TotalfuelGreenW=TotalfuelQuickW=TotalfuelSmoothW=TotalfuelW=0.0
#Maximum et Minimum
WMaxT=WMaxTG=WMaxTQ=WMaxTS=0.0
WMaxW=WMaxWG=WMaxWQ=WMaxWS=WMaxF=WMaxFG=WMaxFQ=WMaxFS=0.0
WMinT=WMinTG=WMinTQ=WMinTS=WMinW=WMinWG=WMinWQ=WMinWS=WMinF=WMinFG=WMinFQ=WMinFS=10000000.0

#################################################################################

#Debut calcul
while i<len(duration):

#Total Avec reroutage

#################################################################################

	#Temps total Avec reroutage

	duration[i]=float(duration[i])
	if duration[i]>MaxT:
		MaxT=duration[i]
	if duration[i]<MinT:
		MinT=duration[i]
	TotalDuration=TotalDuration+duration[i]


	#Temps total d'attente Avec reroutage

	waitSteps[i]=float(waitSteps[i])
	if waitSteps[i]>MaxW:
		MaxW=waitSteps[i]
	if waitSteps[i]<MinW:
		MinW=waitSteps[i]
	TotalwaitSteps=TotalwaitSteps+waitSteps[i]

	#Consommation totale Avec reroutage

	fuel[i]=float(fuel[i])
	if fuel[i]>MaxF:
		MaxF=fuel[i]
	if fuel[i]<MinF:
		MinF=fuel[i]
	Totalfuel=Totalfuel+fuel[i]




#######################################################################

#Vehicules utilisant Green

#######################################################################

	if veh[i] in ListGreen:
		
		#Temps Avec reroutage Local
		j=vehW.index(veh[i])
		if duration[i]>MaxTG:
			MaxTG=duration[i]
		if duration[i]<MinTG:
			MinTG=duration[i]
		TotalDurationGreen=TotalDurationGreen+duration[i]
		
		#Temps d'attente Avec reroutage Local
		if waitSteps[i]>MaxWG:
			MaxWG=waitSteps[i]
		if waitSteps[i]<MinWG:
			MinWG=waitSteps[i]
		TotalwaitStepsGreen=TotalwaitStepsGreen+waitSteps[i]

		#Consommation Avec reroutage Local
		if fuel[i]>MaxFG:
			MaxFG=fuel[i]
		if fuel[i]<MinFG:
			MinFG=fuel[i]
		TotalfuelGreen=TotalfuelGreen+fuel[i]



		durationW[j]=float(durationW[j])
		waitStepsW[j]=float(waitStepsW[j])
		fuelW[j]=float(fuelW[j])

		#Temps Sans reroutage
		if durationW[j]>WMaxTG:
			WMaxTG=durationW[j]
		if durationW[j]<WMinTG:
			WMinTG=durationW[j]
		TotalDurationGreenW=TotalDurationGreenW+durationW[j]
		TotalDurationW=TotalDurationW+durationW[j]

		#Temps d'attente Sans reroutage 
		if waitStepsW[j]>WMaxWG:
			WMaxWG=waitStepsW[j]
		if waitStepsW[j]<WMinWG:
			WMinWG=waitStepsW[j]
		TotalwaitStepsGreenW=TotalwaitStepsGreen+waitStepsW[j]
		TotalwaitStepsW=TotalwaitStepsW+waitStepsW[j]

		#Consommation Sans reroutage
		if fuelW[j]>WMaxFG:
			WMaxFG=fuelW[j]
		if fuelW[j]<WMinFG:
			WMinFG=fuelW[j]
		TotalfuelGreenW=TotalfuelGreenW+fuelW[j]
		TotalfuelW=TotalfuelW+fuelW[j]

#######################################################################

#Vehicules utilisant Quick

#######################################################################


	if veh[i] in ListQuick:

		#Temps Avec reroutage Local
		j=vehW.index(veh[i])
		if duration[i]>MaxTQ:
			MaxTQ=duration[i]
		if duration[i]<MinTQ:
			MinTQ=duration[i]
		TotalDurationQuick=TotalDurationQuick+duration[i]
		
		#Temps d'attente Avec reroutage Local
		if waitSteps[i]>MaxWQ:
			MaxWQ=waitSteps[i]
		if waitSteps[i]<MinWQ:
			MinWQ=waitSteps[i]
		TotalwaitStepsQuick=TotalwaitStepsQuick+waitSteps[i]

		#Consommation Avec reroutage Local
		if fuel[i]>MaxFQ:
			MaxFQ=fuel[i]
		if fuel[i]<MinFQ:
			MinFQ=fuel[i]
		TotalfuelQuick=TotalfuelQuick+fuel[i]

		durationW[j]=float(durationW[j])
		waitStepsW[j]=float(waitStepsW[j])
		fuelW[j]=float(fuelW[j])


		#Temps Sans reroutage
		if durationW[j]>WMaxTQ:
			WMaxTQ=durationW[j]
		if durationW[j]<WMinTQ:
			WMinTQ=durationW[j]
		TotalDurationQuickW=TotalDurationQuickW+durationW[j]
		TotalDurationW=TotalDurationW+durationW[j]

		#Temps d'attente Sans reroutage 
		if waitStepsW[j]>WMaxWQ:
			WMaxWQ=waitStepsW[j]
		if waitStepsW[j]<WMinWQ:
			WMinWQ=waitStepsW[j]
			if WMinWQ==0:
				WMinWQ=1
		TotalwaitStepsQuickW=TotalwaitStepsQuickW+waitStepsW[j]
		TotalwaitStepsW=TotalwaitStepsW+waitStepsW[j]

		#Consommation Sans reroutage
		if fuelW[j]>WMaxFQ:
			WMaxFQ=fuelW[j]
		if fuelW[j]<WMinFQ:
			WMinFQ=fuelW[j]
		TotalfuelQuickW=TotalfuelQuickW+fuelW[j]
		TotalfuelW=TotalfuelW+fuelW[j]

#######################################################################

#Vehicules utilisant Smooth

#######################################################################


	if veh[i] in ListSmooth:
		j=vehW.index(veh[i])

		#Temps Avec reroutage Local
		if duration[i]>MaxTS:
			MaxTS=duration[i]
		if duration[i]<MinTS:
			MinTS=duration[i]
		TotalDurationSmooth=TotalDurationSmooth+duration[i]

		#Temps d'attente Avec reroutage Local
		if waitSteps[i]>MaxWS:
			MaxWS=waitSteps[i]
		if waitSteps[i]<MinWS:
			MinWS=waitSteps[i]
		TotalwaitStepsSmooth=TotalwaitStepsSmooth+waitSteps[i]

		#Consommation Avec reroutage Local
		if fuel[i]>MaxFS:
			MaxFS=fuel[i]
		if fuel[i]<MinFS:
			MinFS=fuel[i]
		TotalfuelSmooth=TotalfuelSmooth+fuel[i]

		durationW[j]=float(durationW[j])
		waitStepsW[j]=float(waitStepsW[j])
		fuelW[j]=float(fuelW[j])



		#Temps Sans reroutage
		if durationW[j]>WMaxTS:
			WMaxTS=durationW[j]
		if durationW[j]<WMinTS:
			WMinTS=durationW[j]
		TotalDurationSmoothW=TotalDurationSmoothW+durationW[j]
		TotalDurationW=TotalDurationW+durationW[j]

		#Temps d'attente Sans reroutage 
		if waitStepsW[j]>MaxWS:
			WMaxWS=waitStepsW[j]
		if waitStepsW[j]<MinWS:
			WMinWS=waitStepsW[j]
		TotalwaitStepsSmoothW=TotalwaitStepsSmoothW+waitStepsW[j]
		TotalwaitStepsW=TotalwaitStepsW+waitStepsW[j]

		#Consommation Sans reroutage
		if fuelW[j]>WMaxFS:
			WMaxFS=fuelW[j]
		if fuelW[j]<WMinFS:
			WMinFS=fuelW[j]
		TotalfuelSmoothW=TotalfuelSmoothW+fuelW[j]
		TotalfuelW=TotalfuelW+fuelW[j]			
	i=i+1

#################################################################################

#maximum et minimum

#################################################################################



WMaxT=max(WMaxTG,WMaxTQ,WMaxTS)
WMinT=min(WMinTG,WMinTQ,WMinTS)
WMaxW=max(WMaxWG,WMaxWQ,WMaxWS)
WMinW=min(WMinWG,WMinWQ,WMinWS)
WMaxF=max(WMaxFG,WMaxFQ,WMaxFS)
WMinF=min(WMinFG,WMinFQ,WMinFS)





#############################################################################################

#Moyenne Application Green
#Avec

if len(ListGreen)>0:
	MeanDurationGreen=(TotalDurationGreen/len(ListGreen))/60
	MeanwaitStepsGreen=TotalwaitStepsGreen/len(ListGreen)
	MeanFuelConsoGreen=TotalfuelGreen/len(ListGreen)
else:
	MeanDurationGreen=0
	MeanwaitStepsGreen=0
	MeanFuelConsoGreen=0
#Sans
if len(ListGreen)>0:
	MeanDurationGreenW=(TotalDurationGreenW/len(ListGreen))/60
	MeanwaitStepsGreenW=TotalwaitStepsGreenW/len(ListGreen)
	MeanFuelConsoGreenW=TotalfuelGreenW/len(ListGreen)
else:
	MeanDurationGreenW=0
	MeanwaitStepsGreenW=0
	MeanFuelConsoGreenW=0

#############################################################################################

#Moyenne Application Quick
#Avec
if len(ListQuick)>0:
	MeanDurationQuick=(TotalDurationQuick/len(ListQuick))/60
	MeanwaitStepsQuick=TotalwaitStepsQuick/len(ListQuick)
	MeanFuelConsoQuick=TotalfuelQuick/len(ListQuick)
else:
	MeanDurationQuick=0
	MeanwaitStepsQuick=0
	MeanFuelConsoQuick=0

#Sans
if len(ListQuick)>0:
	MeanDurationQuickW=(TotalDurationQuickW/len(ListQuick))/60
	MeanwaitStepsQuickW=TotalwaitStepsQuickW/len(ListQuick)
	MeanFuelConsoQuickW=TotalfuelQuickW/len(ListQuick)
else:
	MeanDurationQuickW=0
	MeanwaitStepsQuickW=0
	MeanFuelConsoQuickW=0

#############################################################################################

#Moyenne Application Smooth

#Avec
if len(ListSmooth)>0:
	MeanDurationSmooth=(TotalDurationSmooth/len(ListSmooth))/60
	MeanwaitStepsSmooth=TotalwaitStepsSmooth/len(ListSmooth)
	MeanFuelConsoSmooth=TotalfuelSmooth/len(ListSmooth)
else:
	MeanDurationSmooth=0
	MeanwaitStepsSmooth=0
	MeanFuelConsoSmooth=0

#Sans
if len(ListSmooth)>0:
	MeanDurationSmoothW=(TotalDurationSmoothW/len(ListSmooth))/60
	MeanwaitStepsSmoothW=TotalwaitStepsSmoothW/len(ListSmooth)
	MeanFuelConsoSmoothW=TotalfuelSmoothW/len(ListSmooth)
else:
	MeanDurationSmoothW=0
	MeanwaitStepsSmoothW=0
	MeanFuelConsoSmoothW=0

#############################################################################################

#Moyenne Total

#Avec
MeanDuration=(TotalDuration/len(List))/60
MeanwaitSteps=TotalwaitSteps/len(List)
MeanFuelConso=Totalfuel/len(List)

#Sans
MeanDurationW=(TotalDurationW/len(List))/60
MeanwaitStepsW=TotalwaitStepsW/len(List)
MeanFuelConsoW=TotalfuelW/len(List)











#print "la conso moyenne est de" + str(MeanFuelConso) + "ml"
#print "Le parcours moyen en temps est " + str(MeanDuration) +" min"
#print "Le temps moyen d'attente par vehicule est : " + str(MeanwaitSteps) +" s"
#print "Le nombre de vehicule est de : " + str(len(duration))
#print "maximum de temps d'attente :" + str(max(waitSteps)) + "s"
#print "maximum temps de parcours :" + str(max(duration)/60) + "min"





