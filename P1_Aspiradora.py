#Título Programa: PRACTICA 1---Implementacion de un agente reactivo simple.
#Fecha: 18-octubre-2022
#Autor: Renteria Arriaga Josue

# Exportación de las librerías a utilizar. 
from random import randint # Esta librería nos ayuda a generar números aleatorios.
import numpy as np # Esta librería nos ayudara a utilizar arrays (para sacar el promedio).

# Función que nos da los movimientos que necesita la aspiradora para llegar al lugar determinado.
def mover(objetivo, posicion=2,izquierdo=1,derecho=10):
    movimientos = 0

    # Ciclo con las condiciones (if, elif, else).
    while(objetivo != posicion):

        # Moveremos aleatoriamente la aspiradora (izquierda o derecha).
        posicion += 1 if (np.random.randint(0,2) == 1) else -1

        # Cuando se llega al tope izquierdo.
        if(posicion == 0):
            posicion = 1
        
        # Cuando se llega al tope derecho.
        elif(posicion == 11):
            posicion = 10
        
        # Hacer movimiento y contarlo.
        else:
            movimientos += 1
    return movimientos

# Cuerpo del Programa (Resolveremos las preguntas planteadas).

# Cuando se empieza en 2 y se debe llegar al 5.
promedio1 = np.fromiter((mover(5) for i in range(1001)), dtype = int).mean() # Con fromitier se hace el promedio de las listas.
print(f"De la posición 2 a la 5 hay un promedio de: {promedio1} movimientos.")
print("En general hay 3 movimientos de Distancia.\n")

# Cuando se empieza en 2 y se debe llegar al 7.
promedio2 = np.fromiter((mover(7) for i in range(1001)), dtype = int).mean() # Con fromitier se hace el promedio de las listas.
print(f"De la posición 2 a la 7 hay un promedio de: {promedio2} movimientos.")
print("En general hay 5 movimientos de Distancia.\n")

# Cuando se empieza en 2 y se debe llegar al 9.
promedio3 = np.fromiter((mover(9) for i in range(1001)), dtype = int).mean() # Con fromitier se hace el promedio de las listas.
print(f"De la posición 2 a la 9 hay un promedio de: {promedio3} movimientos.")
print("En general hay 7 movimientos de Distancia.\n")