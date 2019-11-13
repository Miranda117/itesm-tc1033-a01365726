def diccionaryStructure():
    dic_data={}
    dic_dates={}
    data= open('datos_vuelos.csv','r')
    datalines=data.readlines()
    #datalines=datalines.replace(","," ")
    #pos=datalines.find("\n")
    #datalinesN=datalines[pos:]
    #datalinesR=datalinesN.readlines()
    #datalinesF=datalinesN.split(",")

    for x in datalines:
        data=x.split(",")
        #p=0+(x*4)
        iD=data[0]
        date=data[1]
        if iD not in dic_data.keys():
            dic_data[iD]={}
            
            if date not in dic_data[iD].keys():
                dic_dates[date]={}
                if date not in dic_data[date].keys():
                    dic_data[iD][date]=1
            else:
                dic_data[iD][date]+=1
   # x=9
    #p=0+(x*4)-x
    #data.close()
    print(dic_data)
    return dic_data
    
    



diccionaryStructure()