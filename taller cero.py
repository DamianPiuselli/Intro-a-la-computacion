# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:22:27 2018

Introduccion a la computacion
Taller Flash No 0

@author: Damian Piuselli
"""

import random

def generarMazo():
    Mazo = [1,2,3,4,5,6,7,8,9,10,11,12,   # creo una lista con el mazo ordenado 
            1,2,3,4,5,6,7,8,9,10,11,12,
            1,2,3,4,5,6,7,8,9,10,11,12,
            1,2,3,4,5,6,7,8,9,10,11,12]  
    
    random.shuffle(Mazo)  #Mezcla el mazo ordenado al azar
    return Mazo           #La funcion regresa la lista desordenada

def jugar(a):  # a: es una lista que representa un mazo
    total=0     # inicializo la suma del jugador
    while total < 21:  # loop que se para cuando el total es >= a 21
        total += a.pop()  #elimina el primer item del mazo y lo suma al total
    return total   #la funcion regresa la suma del jugador.

def jugarVarios(a,n): # a: es una lista que representa un mazo  n: numero de jugadores
    lista_total=[0]*n    #inicializo una lista para el total de c/u de los n jugadores
    for i in range(n):  # loopeo segun el numero de jugadores
        lista_total[i] = jugar(a)  # cada jugador "juega" y se guarda su total en la posicion i-esima
    return lista_total             # la funcion regresa una lista con el total de cada jugador.

test = [32,32,32]

def verQuienGano(res):  #res = lista de los resultados. Se considera el ganador al primer jugador (en orden) en estar mas cerca de 21.
     QuienGano = False      #posicion del personaje que gano. None si no gano nadie.
     puntaje_minimo = 21   # Busco un jugador con este puntaje, si no hay nadie lo incremento en 1.
     puntaje_maximo = 32   # el maximo puntaje posible es 20+12. Nadie gana si todos llegaron a 32.
     
     while QuienGano == False:   # el loop continua hasta que alguien gana o se determina que nadie gana (int o None).
         if puntaje_minimo != puntaje_maximo:  # para que se corte cuando min = max
             for jugador in range(len(res)):   # Busca sobre los resultados si algun jugador tiene el puntaje minimo
                 if res[jugador] == puntaje_minimo and QuienGano == False: # esta condicion esta para que gane el primer jugador en llegar al minimo (el de menor i)
                     QuienGano = jugador
             puntaje_minimo += 1  # si nadie tiene 21, se aumenta la cuenta en 1 y se repite hasta que puntaje_min = puntaje_max
         else: QuienGano = None  # si puntaje_min = puntaje_max, entonces nadie gano (todos en 32)
     return QuienGano
            

                 
         
             
         
         
    