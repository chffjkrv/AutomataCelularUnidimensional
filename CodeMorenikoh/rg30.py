import random
import numpy as np
import matplotlib.pyplot as plt


#Inicializamos a 0 el array que muestra el estado inicial de las celdas, y luego cambiamos el estado de una de las celulas de forma aleatoria.
Tamanio = 1721
rg= 112
arrNow = np.zeros(Tamanio, int)
arrNext = np.zeros(Tamanio, int)
arrNow[random.randint(0,len(arrNow)-1)] = 1
matrix = np.zeros((Tamanio,Tamanio), int)

#En esta funcion determinamos si la celula ha de morir o vivir pasandole el triplete correspondiente de a la celula.
def Caesar(trip, rg):  
    #Creamos un diccionario con las reglas
    rg30 = {'111' : 0 , '110' : 0, '101': 0, '100':1 , '011':1 , '010':1 , '001':1 , '000':0 }
    rg110 = {'111' : 0 , '110' : 1, '101': 1, '100':0 , '011':1 , '010':1 , '001':1 , '000':0 }
    rg22 = {'111' : 0 , '110' : 0, '101': 0, '100':1 , '011':0 , '010':1 , '001':1 , '000':0}
    rg33 = {'111' : 0 , '110' : 0, '101': 1, '100':0 , '011':0 , '010':0 , '001':0 , '000':1}
    rg17 = {'111' : 0 , '110' : 0, '101': 0, '100':1 , '011':0 , '010':0 , '001':0 , '000':1}
    rg21 = {'111' : 0 , '110' : 0, '101': 0, '100':1 , '011':0 , '010':1 , '001':0 , '000':1}
    rg13 = {'111' : 0 , '110' : 0, '101': 0, '100':0 , '011':1 , '010':1 , '001':0 , '000':1}
    rg11 = {'111' : 0 , '110' : 0, '101': 0, '100':0 , '011':1 , '010':0 , '001':1 , '000':1}
    rg23 = {'111' : 0 , '110' : 0, '101': 0, '100':1 , '011':0 , '010':1 , '001':1 , '000':1}
    rg222 = {'111' : 1 , '110' : 1, '101': 0, '100':1 , '011':1 , '010':1 , '001':1 , '000':0}
    rg2 = {'111' : 0 , '110' : 0, '101': 0, '100':0 , '011':0 , '010':0 , '001':1 , '000':0 }
    rg220 = {'111' : 1 , '110' : 1, '101': 0, '100':1 , '011':1 , '010':1 , '001':0 , '000':0}
    rg128 = {'111' : 1 , '110' : 0, '101': 0, '100':0 , '011':0 , '010':0 , '001':0 , '000':0}
    rg56 = {'111' : 0 , '110' : 0, '101': 1, '100':1 , '011':1 , '010':0 , '001':0 , '000':0}
    rg112 = {'111' : 0 , '110' : 1, '101': 1, '100':1 , '011':0 , '010':0 , '001':0 , '000':0}

    
    if rg == 30:
        for key in rg30:
            if trip == key:
                return rg30[key]
    elif rg == 112:
        for key in rg112:
            if trip == key:
                return rg112[key]
    elif rg == 2:
        for key in rg2:
            if trip == key:
                return rg2[key]
    elif rg == 220:
        for key in rg220:
            if trip == key:
                return rg220[key]
    elif rg == 56:
        for key in rg56:
            if trip == key:
                return rg56[key]
    elif rg == 23:
        for key in rg23:
            if trip == key:
                return rg23[key]
    elif rg == 11:
        for key in rg11:
            if trip == key:
                return rg11[key]
    elif rg == 13:
        for key in rg13:
            if trip == key:
                return rg13[key]
    elif rg == 17:
        for key in rg17:
            if trip == key:
                return rg17[key]
    elif rg == 21:
        for key in rg21:
            if trip == key:
                return rg21[key]
    elif rg == 22:
        for key in rg22:
            if trip == key:
                return rg22[key]
    elif rg == 33:
        for key in rg33:
            if trip == key:
                return rg33[key]
    elif rg == 110:
        for key in rg110:
            if trip == key:
                return rg110[key]
    elif rg == 222:
        for key in rg222:
            if trip == key:
                return rg222[key]


#Crear bucle for para revisar el estado actual de las células en el arrNow y crear un nuevo array con el 
#estado siguiente de las celulas.
def DameArrNext(arrNow):
    global arrNext
    global rg
    nax=0
    for cel in arrNow:    
        if nax == 0:
            trip = str(arrNow[len(arrNow)-1])+str(arrNow[nax])+str(arrNow[nax+1])
            arrNext[nax] = Caesar(trip, rg)
            nax+=1
        elif nax > 0 and nax < len(arrNow)-1:
            trip = str(arrNow[nax-1])+str(arrNow[nax])+str(arrNow[nax+1])
            arrNext[nax] = Caesar(trip, rg)
            nax+=1
        elif nax == len(arrNow)-1:
            trip = str(arrNow[nax-1])+str(arrNow[nax])+str(arrNow[0])
            arrNext[nax] = Caesar(trip, rg)   
    return arrNext

def CreaMatrix():
    global matrix
    global arrNow
    global arrNext
    matrix[0] = arrNow
    for arr in range(len(matrix)):
        if arr > 0:
            matrix[arr] = DameArrNext(arrNow)
            arrNow = matrix[arr]
    return matrix

def GuardaImagen(mtx):
    global Tamanio
    plt.style.use(['dark_background'])
    plt.rcParams['image.cmap'] = 'binary'
    fig, ax = plt.subplots(figsize=(256, 144))
    ax.imshow(mtx)
    ax.axis(False)
    plt.savefig("rg"+str(rg)+"_"+str(Tamanio)+"x"+str(Tamanio)+".png")


matrix = CreaMatrix()
GuardaImagen(matrix)



#PARA INICIALIZAR EL ARRAY CON 1721
#arrNow = np.zeros(Tamanio, int)
#arrNow[0]=1
#arrNow[1]=1
#arrNow[3]=1
#arrNow[5]=1
#arrNow[6]=1
#arrNow[7]=1
#arrNow[10]=1