import tkinter
import tkinter.messagebox

#Algunas librerias que se necesitaran:


import tkinter
import tkinter.messagebox

import funciones #rchivo con nuestras funciones


main = tkinter.Tk()
main.resizable(width=False,height=False)
main.minsize(width=350,height=150)
main.maxsize(width=350,height=200)
main.title("Detector de gmi2")
main.config(bg="#ffffff")



texto = tkinter.Label(text="Presiona el boton para elegir el audio y analizarlo",bg="#ffffff",padx=10,pady=15,font=("Helvetica",12))
subir2 = tkinter.Button(main,text="Resolución Estándar",command=lambda: funciones.analizarGmi2(2),fg="#a1dbcd",bg="#383a39",activebackground="#2c5912",cursor="target",takefocus=True,font=("Helvetica",12))
subir3 = tkinter.Button(main,text="Alta Resolución",command=lambda: funciones.analizarGmi2(1),fg="#a1dbcd",bg="#383a39",activebackground="#2c5912",cursor="target",takefocus=True,font=("Helvetica",12))
frame = tkinter.Frame(height=15)

#packing
texto.pack()
subir2.pack()
frame.pack()
subir3.pack()


tkinter.mainloop()