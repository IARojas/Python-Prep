#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
x=5
if(x>0):
    print(x,"es mayor que cero")
else:
    print(x,"es menor que 0")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
x=5
y=6
if(type(x)==type(y)):
    print(x," y ",y," tienen el mismo tipo de dato")
else:
    print(x," y ",y," no tienen el mismo tipo de dato")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
x=1
while x<21:
    if(x%2==0):
        print(x,"es par")
        x=x+1
    else:
        print(x,"es impar")
        x=x+1






# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
numeros=[0,1,2,3,4,5]
for num in numeros:
    potencia=num**3
    print("El número",num,"elevado a la 3 es",potencia)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
x=4
for i in range(0,x):
    pass
print(i)

# No entiendo bien lo que solicita


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

x=0
if (x>-1):
    factorial=x
    while(factorial>2 and x>1):
        x=x-1
        factorial=factorial*x
    print("El factorial es",factorial)
else:
    print("La variable es menor que 0")






# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
x=5
while(x>0):
    for num in range(2,x):
        num=num-1
        print(num,"es mayor que 0")
    x=x-1






# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
x=5
for num in range(2,x):
    while (x<5):
        x-=1
    print(x,"es mayor que 2")






# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

numeros=range(0,30)
primos=[]
#Consideramos que el 2 es un número primo a perse.
for i in numeros:
    if(i<2):
        continue
    es_primo=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            es_primo=False
            break
    if es_primo:
        primos.append(i)
print("Números primos encontrados:",primos)






# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
numeros=range(0,30)
primos=[]
#Consideramos que el 2 es un número primo a perse.
for i in numeros:
    if(i<2):
        continue
    es_primo=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            es_primo=False
            break
    if es_primo:
        primos.append(i)
print("Números primos encontrados:",primos)





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

#Se uso el mimo codigo ya que se uso continue para pasar el 0 y el 1. y break para romper el segundo for, en caso de que 
# se encuentre que es divisible por algun numero del 2do rango

numeros=range(0,30)
ciclos_sin_break = 0
n = 0
primo = True
while (n < max(numeros)):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

# In[57]:
numeros=range(0,30)
ciclos_sin_break=0
primos=[]
#Consideramos que el 2 es un número primo a perse.
for i in numeros:
    if(i<2):
        ciclos_sin_break+=1
        continue
    es_primo=True
    for j in range(2,int(i**0.5)+1):
        ciclos_sin_break+=1
        if i%j==0:
            es_primo=False
            break
    if es_primo:
        primos.append(i)
print("Números primos encontrados:",primos)
print(ciclos_sin_break)



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

minimo=100
maximo=300
Divisible12=[]
i=100

while i<=maximo:
    if i%12==0:
        Divisible12.append(i)
    i+=1
print("Los números divisibles por 12 entre 100 y",maximo,"son",Divisible12)





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
numero=int(input())
print(numero,"finaliza exitosamente")
numeros=range(0,numero)
primos=[]
#Consideramos que el 2 es un número primo a perse.
for i in numeros:
    if(i<2):
        continue
    es_primo=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            es_primo=False
            break
    if es_primo:
        primos.append(i)
print("Números primos encontrados:",primos)


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
divisible9=[]
multiplo6=[]
maximo=1000
i=100
j=100
while i<=maximo:
    if i%9==0:
        divisible9.append(i)
    i+=1
print("Los numeros divisibles por 9 son",divisible9)

while j<=maximo:
    if j%6==0:
        multiplo6.append(j)
    j+=1
print("Los numeros multiplos de 6 son:",multiplo6)

set_divisible9 = set(divisible9)
set_multiplo6 = set(multiplo6)
elementos_comunes = set_divisible9 & set_multiplo6
print("Elementos en común entre divisibles por 9 y múltiplos de 6:", elementos_comunes)
minimo_comun = min(elementos_comunes)
print("El valor mínimo común entre divisibles por 9 y múltiplos de 6 es:", minimo_comun)

# %%
