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

    result=diccionaryConverter(iDtmp_list)
    print(result)
    

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