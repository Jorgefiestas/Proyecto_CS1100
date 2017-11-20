#Algunas librerias que se necesitaran:

import IPython.display
import matplotlib
matplotlib.use('TkAgg')

import numpy as np

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

#Se importa la libreria de analisis de audio 'Librosa':

import librosa
import librosa.display

def arraysMSE(arr1, arr2):
	mse = 0

	#funcion que calcula el "Mean Squared Error", para ver que tan similares son los audios.

	for i in range(arr1.__len__()):
		mse = mse + ((arr1[i]-arr2[i])**2)/arr1.__len__()
		if mse>0.005:
			return mse
	return mse

#Se utiliza Tkinter para seleccionar un archivo.

gemi2 = False

Tk().withdraw()
filename = askopenfilename()
filename =  str(os.path.abspath(filename))

#Se genera el espectograma de Mel para este archivo.

y, sr = librosa.core.load(filename, sr=1000)

#Se abre el audio que se tratara de identificar.

g, sr = librosa.core.load("Gemi22.mp3", sr=1000)

for x in range(y.__len__()-g.__len__(),0, -1):
	mse = arraysMSE(g, [y[i] for i in range(x, x + g.__len__())])
	if mse <= 0.005:
		gemi2 = True
		break
	
if gemi2:
	print("No lo abras son gemidos")

else:
	print("No son gemidos")






