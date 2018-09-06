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
    res=[0]*n    #inicializo una lista para el total de c/u de los n jugadores
    for i in range(n):  # loopeo segun el numero de jugadores
        res[i] = jugar(a)  # cada jugador "juega" y se guarda su total en la posicion i-esima
    return res            # la funcion regresa una lista con el total de cada jugador.

 
def verQuienGano(res):  #res = lista de los resultados. Se considera el ganador al primer jugador (en orden) en estar mas cerca de 21.
    QuienGano = None    #posicion del personaje que gano
    puntaje_minimo = 0   # Busco el primer jugador con este puntaje, si no hay nadie lo incremento en 1.
    res_dist = [abs(x - 21) for x in res]  # distancia al 21, para buscar ganadores mas facilmente.
    while QuienGano == None :    # el loop continua hasta que se encuentra un ganador, siempre hay uno, incluso en caso de empate ya que gana el primero.
        i=0
        for jugador in res_dist:
            if jugador == puntaje_minimo and QuienGano == None:
                QuienGano = i
            else:
                i+=1
        puntaje_minimo += 1
    return QuienGano

# Para jugar otro, considero que una mejor estrategia que robar hasta pasarse es para de robar a una cierta distancia de 21.
def jugarOtro(a, min_score=19):  # a: es una lista que representa un mazo, min_score: el score minimo para dejar de robar.
    total=0     # inicializo la suma del jugador
    while total < min_score:
        total += a.pop()  #elimina el primer item del mazo y lo suma al total
    return total   #la funcion regresa la suma del jugador.

test = [19,26,20,15,11]
             
         
         
    