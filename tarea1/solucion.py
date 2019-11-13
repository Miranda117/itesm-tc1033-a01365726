def diccionaryConverter(iDtmp_list):
    return{i:iDtmp_list.count(i) for i in iDtmp_list}

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
            datestmp_list[x]=datestmp_list[x][0:4]

    #print(yearMonth)
    datesTravel=diccionaryConverter(datestmp_list)
    print(datesTravel)
    #print("=========================================")
    iDtravel=diccionaryConverter(iDtmp_list)
    print(iDtravel)
    

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