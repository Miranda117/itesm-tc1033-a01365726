#Angel Nolasco Serrano
#A01365726

def diccionaryConverter(lists):
    return{i:lists.count(i) for i in lists}

def diccionaryStructure():
    iD=[]
    dates=[]
    #dic_data={}
    #dic_dates={}
    data= open('datos_vuelos.csv','r')
    datalines=data.read()
    #datalines=datalines.replace(","," ")
    pos=datalines.find("\n")
    datalinesN=datalines[pos+1:]
    #datalinesR=datalinesN.readlines()
    datalinesF=datalinesN.split(",")

    for x in range (len(datalinesF)):
        p=0+(x*4)-x
        #pd=1+(x*4)-x
        if (len(datalinesF))>=p:
            iD.append(datalinesF[p])
            #dates.append(datalinesF[pd])
        elif (len(datalinesF))<p:
            pass#print("-")
    
    for x in range (len(datalinesF)):
        #p=0+(x*4)-x
        pd=1+(x*4)-x
        if (len(datalinesF))-3>=pd:
            #iD.append(datalinesF[p])
            dates.append(datalinesF[pd])
        elif (len(datalinesF))<pd:
            pass#print("-")
    
    datesChain=",".join(dates)
    datesChain=datesChain.replace(" ","")
    datesChain=datesChain.replace("_",",")
    datestmp_list=datesChain.split(",")
    #print(datestmp_list)
    #print(datalinesF[1])    
    iDchain="\n".join(iD)
    iDchain=iDchain.replace("\n",",")
    iDchain=iDchain.replace(" ","")
    iDtmp_list=iDchain.split(",")
    #print(iDtmp_list)
    pos=0
    while pos<=(len(iDtmp_list))/2+14:
        posD=pos+1
        del(iDtmp_list[posD])
        pos=pos+1
    del(iDtmp_list[31])
    for x in range(len(iDtmp_list)):
            iDtmp_list[x]=iDtmp_list[x][0:2]
    pos=0
    #print(datestmp_list)
    #print(datestmp_list[3])
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
    

        #yearMonth=",".join(datestmp_list)
      #  yearMonth=yearMonth.replace("18","c")
       # yearMonth=yearMonth.replace(",","_")
        #yearMonth=yearMonth.replace("","-")
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
    
    
     #print(yearMonth)
    datesTravel=diccionaryConverter(datestmp_list)
    print(datesTravel)
    #print("=========================================")
    iDtravel=diccionaryConverter(iDtmp_list)
    print(iDtravel)

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
    #monthsS=(",").join(monthsS)
    #timesS=(",").join(timesS)
    #monthsS=monthsS.replace(",","\n")
    #timesS=timesS.replace(",","\n")
    #print(timesS)
    #timesS=timesS.replace(",",",,")
    #timesS=timesS.replace()
    print(timesI)
    solutions=open('resultados.csv','w+')
    solutions.write("Meses,numero de vuelos totales mensuales,porcentaje de vuelos a nivel mundial,\n")
    #solutions.write(monthsS)
    #solutions.write(timesS)
    solutions.close()
    tot=0
    for i in range(len(timesI)):
        tot=tot+timesI[i]
    print(tot)
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
    print(tot)
    for x in range(len(zonesS)):
        temp=placesS[x]+","+zonesS[x]+","+"%"+str(round((zonesI[x]*100)/tot,4))+",\n"
        solutions.write(temp)
    solutions.close()
        



    #print(datestmp_list)
    #print(dates)
        #print(datalinesF[p])
        #print(datalinesF[pd])
    
   #for x in datalines:
    #    data=x.split(",")
        #p=0+(x*4)
     #   iD=data[0]
      #  date=data[1]
       # if iD not in dic_data.keys():
        #    dic_data[iD]={}
            
         #   if date not in dic_data[iD].keys():
          #      dic_dates[date]={}
           #     if date not in dic_data[date].keys():
            #        dic_data[iD][date]=1
            #else:
             #   dic_data[iD][date]+=1
                
    
    #data.close()
    #print(dic_data)
    #return dic_data
    
    



diccionaryStructure()