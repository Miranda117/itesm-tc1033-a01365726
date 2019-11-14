#Angel Nolasco Serrano
#A01365726
def diccionaryConverter(lists):
    return{i:lists.count(i) for i in lists}

def diccionaryStructure():
    iD=[]
    dates=[]
    data= open('datos_vuelos.csv','r')
    datalines=data.read()
    pos=datalines.find("\n")
    datalinesN=datalines[pos+1:]
    datalinesF=datalinesN.split(",")

    for x in range (len(datalinesF)):
        p=0+(x*4)-x
        if (len(datalinesF))>=p:
            iD.append(datalinesF[p])
        elif (len(datalinesF))<p:
            pass
    
    for x in range (len(datalinesF)):
        pd=1+(x*4)-x
        if (len(datalinesF))-3>=pd:
            dates.append(datalinesF[pd])
        elif (len(datalinesF))<pd:
            pass
    
    datesChain=",".join(dates)
    datesChain=datesChain.replace(" ","")
    datesChain=datesChain.replace("_",",")
    datestmp_list=datesChain.split(",")
   
    iDchain="\n".join(iD)
    iDchain=iDchain.replace("\n",",")
    iDchain=iDchain.replace(" ","")
    iDtmp_list=iDchain.split(",")

    pos=0
    while pos<=(len(iDtmp_list))/2+14:
        posD=pos+1
        del(iDtmp_list[posD])
        pos=pos+1
    del(iDtmp_list[31])
    for x in range(len(iDtmp_list)):
            iDtmp_list[x]=iDtmp_list[x][0:2]
    
    pos=0
    while pos<=(len(datestmp_list))-1:
        if datestmp_list[pos]=="GST":
            del(datestmp_list[pos])
        elif datestmp_list[pos]=="ICT":
            del(datestmp_list[pos])
        elif datestmp_list[pos]=="CEST":
            del(datestmp_list[pos])
        pos=pos+1
    
    pos=0
    while pos<=(len(datestmp_list))-1:
        posD=pos+1
        del(datestmp_list[posD])
        pos=pos+1

    for x in range(len(datestmp_list)):
            datestmp_list[x]=datestmp_list[x][2:4]

    iDnames=",".join(iDtmp_list)
    iDnames= iDnames.replace("A6","Emiratos Arabes")
    iDnames= iDnames.replace("HS","Tailandia")
    iDnames= iDnames.replace("D9","Alemania")
    iDnames= iDnames.replace("PP","Brasil")
    iDnames= iDnames.replace("CF","Canada")
    iDnames= iDnames.replace("EN","Estados Unidos")
    iDnames= iDnames.replace("PK","Indonesia")
    iDnames= iDnames.replace("JA","Japon")
    iDnames= iDnames.replace("XA","Mexico")
    iDnames= iDnames.replace("9V","Singapur")
    iDnames= iDnames.replace("A1","Catar")
    iDtmp_list=iDnames.split(",")
    
    months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    for month in range(len(datestmp_list)):
        intMonth=int(datestmp_list[month])
        datestmp_list[month]=months[intMonth-1]

    datesTravel=diccionaryConverter(datestmp_list)
    iDtravel=diccionaryConverter(iDtmp_list)
    data.close()

    monthsS=list(datesTravel.keys())
    timesS=list(datesTravel.values())
    timesI=list(datesTravel.values())
    for x in range(len(timesS)):
        timesS[x]=str(timesS[x])
    
    placesS=list(iDtravel.keys())
    zonesS=list(iDtravel.values())
    zonesI=list(iDtravel.values())
    for x in range(len(zonesS)):
        zonesS[x]=str(zonesS[x])

    solutions=open('resultados.csv','w+')
    solutions.write("Meses,numero de vuelos totales mensuales,porcentaje de vuelos a nivel mundial,\n")
    solutions.close()

    tot=0
    for i in range(len(timesI)):
        tot=tot+timesI[i]
    solutions=open('resultados.csv','a+')
    for x in range(len(timesS)):
        temp=monthsS[x]+","+timesS[x]+","+"%"+str(round((timesI[x]*100)/tot,4))+",\n"
        solutions.write(temp)
    solutions.close()

    tot=0
    for i in range(len(zonesI)):
        tot=tot+zonesI[i]
    solutions=open('resultados.csv','a+')
    solutions.write("\n")
    solutions.write("\nPaises,viajes totales por pais,porcentaje de viajes a nivel mundial,\n")
    for x in range(len(zonesS)):
        temp=placesS[x]+","+zonesS[x]+","+"%"+str(round((zonesI[x]*100)/tot,4))+",\n"
        solutions.write(temp)
    solutions.write("")
    solutions.close()
  
diccionaryStructure()