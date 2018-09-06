# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:41:29 2018
Problemas ICB, guia 2.
@author: Damian Piuselli
"""

        
##Ejercicio 1.

def doble(n):
    return 2*n

def signo(n):
    if n<0:
        return -1
    elif n>0:
        return 1
    else:
        return 0
    
def absoluto(n): #no puedo usar el nombre abs, xk ya existe en python la funcion.
    return signo(n)*n

def inversoMultiplicativo(n):
    if n != 0:  #confirmo que el input no es cero, ya que la funcion no esta definida en ese punto.
        return 1/n

def suma3(n1,n2,n3):
    return n1+n2+n3

def promedio(n1,n2,n3):
    return suma3(n1,n2,n3)/3

def maximo3(n1,n2,n3):  # cada if confirma si un elemento es el mayor.
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
    
def maximoAbsoluto(n1,n2,n3):
    n1,n2,n3 = n1*signo(n1),n2*signo(n2),n3*signo(n3) #convierto el input de la funcion a valor absoluto.
    return maximo3(n1,n2,n3)

##Ejercicio 2.
def noEsCero(n):
    if n != 0: return True
    else: return False

def iguales(n1,n2):
    if n1 == n2: return True
    else: return False
    
def menor(n1,n2):
    if n1 < n2: return True
    else: return False
    
def par(n):
    if n%2 == 0: return True
    else: return False
    
def divisible(n,d):
    if n%d == 0: return True
    else: return False
    
def imparDivisiblePorTresOCinco(n):
    if divisible(n,3) == True and divisible(n,5) == False:
        return True
    elif divisible(n,3) == False and divisible(n,5) == True:
        return True
    else: return False    

##Ejercicio 3.

def factorial(n):  #falla si el argumento es muy grande, normal?
    if n == 0: return 1
    elif n>0: return n*factorial(n-1) # lo defino recursivamente, cada loop me agrega un termino de la multiplicatoria
    

def sumaDivisores(n):
    i = 1  # pruebo todos los divisores de 1 a n
    suma_divisores = 0  
    while i <= abs(n):  #abs, asi el input puede ser negativo
        if divisible(n,i) == True:
            suma_divisores += i
        i +=1
    return suma_divisores
    
def primo(n): #si es primo sus divisores son 1 y si mismo, entonces sumaDivisores da n+1
    if sumaDivisores(n) == abs(n)+1: return True
    else: return False
    
def menorDivisiblePorTres(n):
    return n+3-n%3  #restando el resto de la division por 3 a n me queda el multiplo de 3 menor a n, sumando 3 me queda el mayor.

## me hago una funcion auxiliar, para hacer la funcion mayorPrimo.
def listarDivisores(n):  # listo divisores, de mayor a menor.
    i = abs(n)
    lista_divisores = []
    while i > 0:
        if divisible(n,i) == True:
            lista_divisores.append(i)
        i -= 1
    return lista_divisores

def mayorPrimo(n1, n2): #n1 es el candidato a mayor divisor primo, n2 el numero que se divide.
    lista_divisores = listarDivisores(n2)
    mayor_divisor_primo = False
    for divisor in lista_divisores:   #itero sobre la lista de divisores de n2 para encontrar el mayor div primo
        if primo(divisor) == True and mayor_divisor_primo == False:
            mayor_divisor_primo += divisor
    if mayor_divisor_primo == abs(n1): #si el mayor divisor primo es igual a n1, abs asi funciona con negativos
        return True
    else: 
        return False
            
def potencia(n1,n2): #True si n1 es potencia de n2. Es decir base^n1 = n2 con base un numero natural.
    base = 1
    es_potencia = False
    while base**n1 <= n2 and es_potencia == False:
        if base**n1 == n2:
            es_potencia = True
        else: base +=1
    return es_potencia        
    
def mcd(n1,n2):
    divisores_n1 = listarDivisores(n1)
    divisores_n2 = listarDivisores(n2)
    max_divisor = False
    
    for divisor_n1 in divisores_n1:
        for divisor_n2 in divisores_n2:
            if divisor_n1 == divisor_n2 and max_divisor == False:
                max_divisor = divisor_n1
    return max_divisor

##Ejercicio 4
## la variable 'a' son listas.
test = [1,2,5,3,5,3,-7,11,9,10]
test2 = [5,5,5,5,5,5,5,5,5,5]

def suma(a):
    total = 0
    for i in a: total +=i
    return total

def promedio(a):
    return suma(a)/len(a)

def maximo(a):
    current = a[0]  
    for i in a:
        if i>= current:
            current = i
    return current

def listaDeAbs(a):
    a_abs = []
    for i in a:
        a_abs.append(i*signo(i))
    return a_abs

def maximoAbsoluto(a):
    a = listaDeAbs(a)
    return maximo(a)

# divisores, ya la hice en el punto anterior. listardivisores(a)

def cantidadAparaciones(a,x):
    i = 0
    for element in a:
        if element == x: 
            i+=1
    return i

#funcion auxiliar para masRepetido.
def repeticionesEnLista(a):
    apariciones_por_elemento = []
    for x1 in a:
        i=0
        for x2 in a:
            if x1==x2:
                i+=1
        apariciones_por_elemento.append(i)
    return apariciones_por_elemento

def masRepetido(a):
    apariciones_por_elemento = repeticionesEnLista(a)
    i = 0  #maximo numero de repeticiones
    i_max = 0  #indice del elemento con mayor repeticiones
    
    for x1 in apariciones_por_elemento:
        if x1 >= i:
            i = x1
            i_max = apariciones_por_elemento.index(x1)
    return a[i_max]
        
def todosPares(a):
    pares = True
    for x in a:
        if par(x) != True:
            pares = False
    return pares

def ordenAscendente(a):
    ascendente = True
    for i in range(len(a)-1):
        if a[i+1]-a[i] < 0:
            ascendente = False
    return ascendente
            
def reverso(a):
    a_reverso = []
    for i in range(len(a)):
        a_reverso.append(a[-i-1])
    return a_reverso

# Ejercicio 5
    
def  ad
        
        
            
    
                
        
        
    

    