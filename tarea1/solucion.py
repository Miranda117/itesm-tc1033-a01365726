#Angel Nolasco Serrano
#A01365726
# -*- coding: utf-8 -*-
def diccionaryConverter(lists):
    return{i:lists.count(i) for i in lists}

def diccionaryStructure():
    iD=[]
    dates=[]
    data= open('datos_vuelos.csv','r')
    datalines=data.read()
    pos=datalines.find("\n")
    datalinesN=datalines[pos+1:] #Se inicia despues del \n de la linea principal para asi leer unicamente los datos del documento y organizarlo en lista
    datalinesF=datalinesN.split(",")
    #Para distinguir las matriculas del resto del documento se observa que las posiciones de estas es constantes, por lo que se plantéa una ecuación cuyo resultado es la posición de la matrícula, la cual es la única que se agrega de todo el segmento
    for x in range (len(datalinesF)):
        p=0+(x*4)-x
        if (len(datalinesF))>=p:
            iD.append(datalinesF[p])
        elif (len(datalinesF))<p:
            pass
    #Al igual que las matrículas, el cambio de posición es constante, por lo que se recorre un espacio a comparación de la ecuación original
    for x in range (len(datalinesF)):
        pd=1+(x*4)-x
        if (len(datalinesF))-3>=pd:#-3 permite omitir los 3 ecabezados que estaban al inicio del documento
            dates.append(datalinesF[pd])
        elif (len(datalinesF))<pd:
            pass
    #El segmento siguiente transforma las listas en cadenas de caracteres para filtrar los espacios inecesarios, así como los caracteres que impiden la filtración de resultados. Despues del proceso vuelve a convertirlos en listas
    datesChain=",".join(dates)
    datesChain=datesChain.replace(" ","")
    datesChain=datesChain.replace("_",",")
    datestmp_list=datesChain.split(",")
    iDchain="\n".join(iD)
    iDchain=iDchain.replace("\n",",")
    iDchain=iDchain.replace(" ","")
    iDtmp_list=iDchain.split(",")
    #filtrado de matriculas de aviones, el ciclo while elimina cualquier elemento dentro de la posición asignada en el ciclo mientras que el ciclo for acorta las matriculas para conservar únicamente los primeros 2 dígitos de identificación, en este punto ya únicamente hay matrículas en la lista.
    pos=0#la constante 2+14 se coloca para evitar una mala delimitación para el cíclo, expresarlo de esta manera evita que el programa falle
    while pos<=(len(iDtmp_list))/2+14:
        posD=pos+1
        del(iDtmp_list[posD])
        pos=pos+1
    del(iDtmp_list[31])
    for x in range(len(iDtmp_list)):
            iDtmp_list[x]=iDtmp_list[x][0:2]
    #Al igual que con las matrículas, los cíclos filtran el contenido de las listas para conservar datos útiles, en este caso, las fechas.
    pos=0# La diferencia fundamental es que en el caso de las fechas, se hace un subproceso de filtración, donde antes de eliminar el formato sobrante de fehca, se eliminan las zonas horarias
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
    #con este ciclo simplemente se reajusta el formato de la fecha
    for x in range(len(datestmp_list)):
            datestmp_list[x]=datestmp_list[x][2:4]
    #Aqui se cambian las claves de identificación por su respectivo nombre para mayor facilidad de lectura para el usuario
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
    #En este ciclo for se cambia el formato numérico del mes por su respectivo nombre, convirtiendo el string del formato original en un entero con el propósito de ser utilizado como posición el la lista months
    months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    for month in range(len(datestmp_list)):
        intMonth=int(datestmp_list[month])
        datestmp_list[month]=months[intMonth-1]
    #ambas variables reciben como parámetros los datos finales obtenidos en las listas para convertirse en diccionarios
    datesTravel=diccionaryConverter(datestmp_list)
    iDtravel=diccionaryConverter(iDtmp_list)
    data.close()
    #este segmento de codigo separa los componentes de los diccionarios previamente creados en [texto] y [valor numerico], obtiene una copia de los valores numéricos de los mismos y mantiene una copia en formato de texto
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
    solutions.write("\n")
    solutions.write("Diccionario de los meses/organizacion fechas: "+str(datesTravel))
    solutions.write("\nDiccionario de los registros de los vuelos/paises: "+str(iDtravel))
    solutions.close()
  
diccionaryStructure()