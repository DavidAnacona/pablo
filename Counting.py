from cProfile import label
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import table

def countingSort(collection):
    if collection == []:
        return []

    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    for number in collection:
        counting_arr[number - coll_min] += 1

    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    ordered = [0] * coll_len

    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered

def grafica(ejex,ejey):
    plt.figure(figsize=(8,8))
    plt.plot(ejex,ejey,label='Grafica \n O(n+k)')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Elementos Ordenados')
    plt.title('T VS E')
    plt.legend()
    plt.grid()
    plt.show()

def calculate_iterations(initial,iterations,increase):
    array_iterations=[]
    valor = initial
    for i in range(iterations):
        array_iterations.append(valor)
        valor = valor + increase    
    return array_iterations

def random_Numbers(num):
    array = []
    v_endal = num + 1000
    for i in range (1000,v_endal):
        numero = randint(1000,v_endal)
        array.append(numero)
    return array

def random_Array(initial,iterations,increase):
    v_iterations = calculate_iterations(initial,iterations,increase)
    arrays_unsorted = []
    for i in v_iterations:
        unsorted = random_Numbers(i)
        arrays_unsorted.append(unsorted)
    return arrays_unsorted

def generate_data_table(count,longitud, tiempo):
    table.tableShow(count,longitud, tiempo)

def sort_arrays_unsorted_show_table(array_de_arrays):
    array_count = []
    array_length = []
    array_time =[]
    arrays_sorted = []
    count = 1
    for i in array_de_arrays:
        
        start = time.time()
        sorted = countingSort(i)
        end = time.time()
        
        tiempo = end - start
        longitud = len(sorted)
        
        
        array_count.append(count)
        array_length.append(longitud)
        array_time.append(tiempo)
        arrays_sorted.append(sorted)
        count = count + 1
    generate_data_table(array_count,array_length,array_time)
    
    count = count + 1
    
    return arrays_sorted    

def sort_arrays_unsorted_show_graphic(array_de_arrays):
    array_count = []
    array_length = []
    array_time =[]
    arrays_sorted = []
    count = 1
    for i in array_de_arrays:
        
        start = time.time()
        sorted = countingSort(i)
        end = time.time()
        
        tiempo = end - start
        longitud = len(sorted)
        
        
        array_count.append(count)
        array_length.append(longitud)
        array_time.append(tiempo)
        arrays_sorted.append(sorted)
        count = count + 1
    grafica(array_length,array_time)
    
    count = count + 1
    
    return arrays_sorted  