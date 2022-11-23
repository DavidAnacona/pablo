import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from random import randint
import matplotlib
matplotlib.use("TkAgg")
import table


# va = int(input("\nIngrese la cantidad de números aleatorios para la primera iteración: "))
# inn = int(input("\nIngrese la cantidad de números aleatorios en la que se incrementa entre iteraciones: "))
# it = int(input("\nIngrese el numero de iteraciones: "))


def countingSortForRadix(inputArray, placeValue):
    
    countArray = [0] * 10
    inputSize = len(inputArray)

  
    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixSort(inputArray):
    
    maxEl = max(inputArray)

    
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1
    
    
    placeVal = 1

   
    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1

    return outputArray

def grafica(ejex,ejey):
    plt.figure(figsize=(8,8))
    plt.plot(ejex,ejey,label='Grafica')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Elementos Ordenados')
    plt.title('T VS E')
    plt.legend()
    plt.grid()
    plt.show()

def valoresiteraciones(inicial,iteraciones,incremento):
    iteraciones1=[]
    valor = inicial
    for i in range(iteraciones):
        iteraciones1.append(valor)
        valor = valor + incremento    
    return iteraciones1

def NumerosAleatorios(valores):
    arreglo = []
    valor_final = valores + 1000
    for i in range (1000,valor_final):
        numero = randint(1000,valor_final)
        arreglo.append(numero)
    return arreglo

def arreglosunsorted(Inicial,iteraciones,incremento):
    valores_iteraciones = valoresiteraciones(Inicial,iteraciones,incremento)
    unsorted1 = []
    for i in valores_iteraciones:
        unsorted = NumerosAleatorios(i)
        unsorted1.append(unsorted)
    return unsorted1

def tabladedatos(contador,longitud, tiempo):
    table.tableShow(contador,longitud, tiempo)
    ejecucion = pd.DataFrame({'Numero': contador,
              'Cantidad de elementos':longitud,
              'Tiempo de ejecucion':tiempo})
    print(ejecucion)
    return ejecucion

def ordenararreglos(arreglo_de_arreglos):
    arreglo_contador = []
    arreglo_longitud = []
    arreglo_tiempos =[]
    arreglos_sorted = []
    contador = 1
    for i in arreglo_de_arreglos:
        
        inicio = time.time()
        sorted = radixSort(i)
        fin = time.time()
        
        tiempo = fin - inicio
        longitud = len(sorted)
        
        
        
        arreglo_contador.append(contador)
        arreglo_longitud.append(longitud)
        arreglo_tiempos.append(tiempo)
        arreglos_sorted.append(sorted)
        contador = contador + 1
    grafica(arreglo_longitud,arreglo_tiempos)
    tabladatos = tabladedatos(arreglo_contador,arreglo_longitud,arreglo_tiempos)
    
    contador = contador + 1
    
    return arreglos_sorted    

# arreglos_unsorted= arreglosunsorted(va,it,inn)
# arreglos_sorted = ordenararreglos(arreglos_unsorted)

