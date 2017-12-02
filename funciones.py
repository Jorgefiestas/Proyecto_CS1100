#Este es el archivo que contiene las funciones que se usaran durante la ejecución del programa.

#Librerías que se necesitaran
import multiprocessing
from multiprocessing import Pool
import time

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import tkinter.messagebox


import IPython.display
import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import os

#Se importa la libreria de analisis de audio 'Librosa':
import librosa
import librosa.display

#Variables globales:
g = []
y = []

import time

#Función que calcula el "Mean Squared Error", para ver que tan similares son los archivos:

def arraysMSE(arr1, arr2):
	mse = 0
	for i in range(arr1.__len__()):
		mse = mse + ((arr1[i]-arr2[i])**2)/arr1.__len__()
		if mse>0.005:
			return mse
	return mse

#Función que analiza el audio en paralelo.

def analizar(x):
	global g
	global y

	mse = arraysMSE(g, [y[i] for i in range(x, x + g.__len__())])
	if mse <= 0.005:
		gemi2 = True
		return gemi2
	else: return False


def analizarGmi2(k):
	global y
	global g

	Tk().withdraw()
	filename = askopenfilename()
	nombreArchivo = os.path.abspath(filename)

	#Se genera el espectograma de este archivo.

	y, sr = librosa.core.load(nombreArchivo, sr=(1000//k))

	#Se genera el espectograma que se trata de identificar.

	g, sr = librosa.core.load("Gemi22.mp3", sr=(1000//k))

	gemi2 = False #Variable que evalua si hay gemidos.

	start = time.time() #Esto es util para calcular el tiempo de proceso y el costo computacional.

	p = Pool() 

	h = p.map(analizar,range(y.__len__()-g.__len__(),0, -1)) #Se distribuye el trabajo en los diferentes cores.

	p.close()
	p.join() #Se espera a que todas los procesos concluyan

	for x in h:
		if x:
			gemi2 = True
			break

	print(time.time()-start)
		
	if gemi2:
		tkinter.messagebox.showinfo("Resultado de Análisis","¡No lo abras, son gemidos!")
	else:
		tkinter.messagebox.showinfo("Resultado de Análisis","No se han detectado gemidos.")
	return 