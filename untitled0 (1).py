# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sYMFM5FdxjGCh6ZarcbPEgb956F6emcY
"""

# @autor: Diana





fila = 8 #Se inicializa la variable
columna = 8 #Se inicializa la variable

arfil1 = [2,2] #Localización en el array del arfil 1
arfil2 = [5,7] #Localización en el array del arfil 2

fila_arfil1, columna_arfil1 = arfil1 #Se le accina el valor de la fila y la columna del arfil1
fila_arfil2, columna_arfil2 = arfil2 #Se le accina el valor de la fila y la columna del arfil2

if abs(fila_arfil1 - fila_arfil2) == abs(columna_arfil1 - columna_arfil2): #El abs es el que saca el valor absoluto verificando la diagonal

  print("Los alfiles están amenazados") #Imprime un mensaje informativo

else :
  print("Los alfiles no están amenazados") #Imprime un mensaje informativo