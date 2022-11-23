from cProfile import label
import tkinter as tk
from tkinter import Toplevel, font
from setuptools import Command
import subprocess as sb
from tkinter.constants import *
from PIL import Image, ImageSequence, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import Counting
import Radix
import time

#archivo para que funcione la evaluacion de gramaticas segun la TAS
cmd='python index.py'
def evaluate():
    p=sb.call(cmd,shell=True)

#Crea la ventana principal
mainWindow=tk.Tk()
mainWindow.iconbitmap('icon.ico')
mainFrame=tk.Frame(mainWindow,bg="lightsteelblue2")
frameTitle=tk.Frame(mainWindow, bg="lightsteelblue3")

window_height = 800 
window_width = 900

screen_width = mainWindow.winfo_screenwidth() 
screen_height = mainWindow.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2)) 
y_cordinate = int((screen_height/2) - (window_height/2))

mainWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

imagen = tk.PhotoImage(file="hola.png")

#Crea la ventana Generalidades
def ventanaGen():
    ventanaGene = Toplevel()
    ventanaGene.iconbitmap('icon.ico')
    ventanaGene.title("Generalidades")
    ventanaGene.resizable(False,False)
    ventanaGene.config(bg="lightsteelblue2")

    window_height = 800 
    window_width = 900

    screen_width = ventanaGene.winfo_screenwidth() 
    screen_height = ventanaGene.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2))

    ventanaGene.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    ventanaGene.geometry("800x750")

    frameTitle=tk.Frame(ventanaGene, bg="lightsteelblue3")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Generalidades", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    text=tk.Label(ventanaGene, text="El Counting Sort es un algoritmo de ordenación que ordena los \nelementos de una matriz contando el número de ocurrencias\n de cada elemento único en la matriz. El conteo se almacena\n en una matriz auxiliar y la clasificación se realiza\n mapeando el conteo como un índice de la matriz auxiliar.", bg="lightsteelblue3", fg="white", font=('Consolas',16))
    text.place(x=20,y=100)

    text=tk.Label(ventanaGene, text="Caracteristicas", bg="lightsteelblue3", fg="white", font=('Consolas',20))
    text.place(x=20,y=250)

    text=tk.Label(ventanaGene, text="Se trata de un algoritmo estable cuya complejidad computacional\n es O(n+k), siendo n el número de elementos a ordenar y k el\n tamaño del vector auxiliar (máximo - mínimo).\nLa eficiencia del algoritmo es independiente de lo casi ordenado\n que estuviera anteriormente.\n Es decir no existe un mejor y peor caso, todos los casos se\n tratan iguales.\nEl algoritmo counting, no se ordena in situ, sino que requiere\n de una memoria adicional.", bg="lightsteelblue3", fg="white", font=('Consolas',16))
    text.place(x=20,y=300)

    btn4=tk.Button(ventanaGene, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=ventanaGene.destroy)
    btn4.place(x=695,y=8)

    lbImagen = tk.Label(ventanaGene, image=imagen)
    lbImagen.place(x=250, y=550)

#Crea la ventana Funcionamiento
def ventanaFun():
    ventanaFunci = Toplevel()
    ventanaFunci.iconbitmap('icon.ico')
    ventanaFunci.title("Funcionamiento")
    ventanaFunci.geometry("800x750")
    ventanaFunci.resizable(False,False)
    ventanaFunci.config(bg="lightsteelblue2")

    window_height = 800 
    window_width = 900

    screen_width = ventanaFunci.winfo_screenwidth() 
    screen_height = ventanaFunci.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2))

    ventanaFunci.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def play_gif():
        global img
        img= Image.open('imagen.gif')

        lblimg=tk.Label(ventanaFunci)
        lblimg.place(x=150,y=200)

        for img in ImageSequence.Iterator(img):
            img=ImageTk.PhotoImage(img)
            lblimg.config(image=img)

            ventanaFunci.update()
            time.sleep(0.01)
        ventanaFunci.after(0,play_gif)

    frameTitle=tk.Frame(ventanaFunci, bg="lightsteelblue3")
    frameTitle.place(relheight=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Funcionamiento", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    btn4=tk.Button(ventanaFunci, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=ventanaFunci.destroy)
    btn4.place(x=790,y=8)

    btn4=tk.Button(ventanaFunci, text="Play", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=play_gif)
    btn4.place(x=700,y=600)

#Crea la ventana demostracion
def ventanaDem():
    ventanaDemo = Toplevel()
    ventanaDemo.iconbitmap('icon.ico')
    ventanaDemo.title("Generalidades")
    ventanaDemo.geometry("800x750")
    ventanaDemo.resizable(False,False)
    ventanaDemo.config(bg="lightsteelblue2")

    window_height = 800 
    window_width = 900

    screen_width = ventanaDemo.winfo_screenwidth() 
    screen_height = ventanaDemo.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2))

    ventanaDemo.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    frameTitle=tk.Frame(ventanaDemo, bg="lightsteelblue3")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Demostracion", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    btn4=tk.Button(ventanaDemo, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=ventanaDemo.destroy)
    btn4.place(x=790,y=8)
    
    btn5=tk.Button(ventanaDemo, text="RADIX SORT", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=ventana4)
    btn5.place(x=630,y=8)

    initial_label = tk.Label(ventanaDemo,text="Introduzca el número de números aleatorios para la primera iteración:", fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    initial_label.place(x=20,y=100)

    initial = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    initial.place(x=20,y=150)

    increase_label = tk.Label(ventanaDemo, text="Ingrese el número de números aleatorios que se incrementa entre iteraciones:", fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    increase_label.place(x=20,y=250)

    increase = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    increase.place(x=20,y=300)

    iterations_label = tk.Label(ventanaDemo,text="Introduzca el número de iteraciones a realizar:",fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    iterations_label.place(x=20,y=400)

    iterations = tk.Entry(ventanaDemo, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    iterations.place(x=20,y=450)

    def ejecutar(initial,iterations,increase):
        # print('hola')
        arrays_unsorted= Counting.random_Array(initial,iterations,increase)
        Counting.sort_arrays_unsorted_show_table(arrays_unsorted)

    def ejecutar2(initial,iterations,increase):
        # print('hola')
        arrays_unsorted= Counting.random_Array(initial,iterations,increase)
        Counting.sort_arrays_unsorted_show_graphic(arrays_unsorted)

    ejecutar_btn = tk.Button(ventanaDemo, text='Mostrar tabla', padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=lambda: ejecutar(int(initial.get()),int(iterations.get()),int(increase.get())))
    ejecutar_btn.place(x=15,y=550)

    ejecutar_btn = tk.Button(ventanaDemo, text='Mostrar graficos',padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=lambda: ejecutar2(int(initial.get()),int(iterations.get()),int(increase.get())))
    ejecutar_btn.place(x=15,y=630)
    
def ventana4():
    ventana4 = Toplevel()
    ventana4.title("Demostracion Radix Sort")
    ventana4.geometry("800x750")
    ventana4.resizable(False,False)
    ventana4.config(bg="lightsteelblue2")

    window_height = 800 
    window_width = 900

    screen_width = ventana4.winfo_screenwidth() 
    screen_height = ventana4.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2))

    ventana4.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    mainFrame=tk.Frame(ventana4,bg="lightsteelblue2")
    mainFrame.place(relheight=1, relwidth=1)

    frameTitle=tk.Frame(ventana4, bg="lightsteelblue3")
    frameTitle.place(x=0.1,relwidth=1)

    title=tk.Label(frameTitle, text="Demostracion Radix Sort", bg="lightsteelblue3", fg="white", font=('Consolas',35))
    title.pack(side=LEFT)

    btn4=tk.Button(ventana4, text="Volver", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=ventana4.destroy)
    btn4.place(x=790,y=8)

    def ejecutar(initial,iterations,increase):
        arreglos_unsorted= Radix.arreglosunsorted(initial,iterations,increase)
        arreglos_sorted = Radix.ordenararreglos(arreglos_unsorted)

    btn5=tk.Button(ventana4, text="Ordenar", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 15), command=lambda: ejecutar(int(grammarEntry.get()),int(grammarEntry1.get()),int(grammarEntry2.get())))
    btn5.place(x=10,y=480)

    global grammarLblR
    global grammarEntry

    grammarLbl=tk.Label(ventana4,text="Introduzca el número de números aleatorios para la primera iteración:", fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    grammarLbl.place(x=10,y=70)

    grammarEntry=tk.Entry(ventana4, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    grammarEntry.place(x=10,y=150)

    grammarLbl1=tk.Label(ventana4, text="Ingrese el número de números aleatorios que se incrementa entre iteraciones:", fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    grammarLbl1.place(x=10,y=195)

    grammarEntry1=tk.Entry(ventana4, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    grammarEntry1.place(x=10,y=270)

    grammarLbl2=tk.Label(ventana4,text="Introduzca el número de iteraciones a realizar:",fg="white", bg="lightsteelblue3", font=('Consolas', 15))
    grammarLbl2.place(x=10,y=330)

    grammarEntry2=tk.Entry(ventana4, fg="black", bg="lightsteelblue3", font=('Consolas', 15))
    grammarEntry2.place(x=10,y=410)    


#Funcion para la configuracion de la ventana Principal
def mainWindowConfig():
    mainWindow.title("CountingSort")
    mainWindow.geometry("800x750")
    mainWindow.resizable(False,False)

#Funcion donde se configura y se ubican los contenedores de los labels y botones
def loadFrames():
    mainFrame.place(relheight=1, relwidth=1)
    frameTitle.place(relheight=0.1,relwidth=1)

#Funcion para configurar los labels
def loadLbl():
    title=tk.Label(frameTitle, text="CountingSort", bg="lightsteelblue3", fg="white", font=('Consolas',40))
    title.pack(side=TOP)

    #Variables globales con el fin de acceder a ellas más abajo
    global grammarLblR
    global grammarEntry

#Funcion para crear y configurar los botones de la venta principal
def loadBtn():
    btn1=tk.Button(mainWindow, text="Generalidades", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 26), command=ventanaGen)
    btn1.place(x=250,y=150)
    
def loadBtn1():
    btn2=tk.Button(mainWindow, text="Funcionamiento", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 26), command= ventanaFun)
    btn2.place(x=235,y=340)

def loadBtn2():
    btn3=tk.Button(mainWindow, text="Demostracion", padx=10, pady=5, fg="black", bg="lightsteelblue3", font=('Consolas', 26), command= ventanaDem)
    btn3.place(x=250,y=525)

mainWindowConfig()
loadFrames()
loadLbl()
loadBtn1()
loadBtn2()
loadBtn()

mainWindow.mainloop()