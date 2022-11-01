#PRACTICA DE PARCIAL 02#

import random

'''

#EVALUAR CUBO MAGICO

def evalua_magico(mt,n):
    
    magic = True
    
    # evaluamos filas
    sfilas = 0
    
    for i in range(n):
        if sum(mt[i]) == sum(mt[0]):
            magic = True
        else:
            magic = False
    
    # evaluamos columnas
    scolu = 0
    
    for i in range(n):
        scolu += sum(mt[:n][i])
        
    if scolu / n == sum(mt[:n][0]):
        magic = True
        
    else:
        magic = False
    # evaluamos diagonales
    dp = 0
    ds = 0
    
    for i in range(n):
        dp += mt[i][i]
        ds += mt[i][n-i-1]
    
    if ds == dp:
        magic = True
    else:
        magic = False
    
    print()
    if magic:
        print("ES RE MAGICOO")
    else:
        print("no es sorry")
        
num = int(input("Ingrese el rango de su lista: "))

# mtz = [[random.randint(0,9) for i in range(num)] for j in range(num)]

mtz = [[4,3,8],
       [9,5,1],
       [2,7,6]]

evalua_magico(mtz,num)

'''
'''

#CREA PATRON

def crea_patron(mt,n):
    
    for i in range(n):
        for j in range(n):
            
            if i < n/2 and j < n/2:
                mt[i][j] = 1
            elif i < n/2 and j >= n/2:
                mt[i][j] = 2
            elif i >= n/2 and j < n/2:
                mt[i][j] = 3
            elif i >= n/2 and j >= n/2:
                mt[i][j] = 4
                
    for i in range(n):
        
        mt[i][i] = 0
        mt[i][n-i-1] = 0

def print_mtz(mt,n):
    
    for i in range(n):
        for j in range(n):
            print("%3d" %mt[i][j], end = " ")
        print()
        
num = int(input("INGRESO DE RANGO DE LA MATRIZ (DEBE SER PAR) --> "))

while num % 2 != 0: 
    num = int(input("INGRESO DE RANGO DE LA MATRIZ (DEBE SER PAR) --> "))

mtz = [[0]*num for i in range(num)]

crea_patron(mtz,num)
print_mtz(mtz,num)

'''
'''

#VALOR MAS REPETIDO

def valor_masrep(mt,fi,co):
    
    vector = [0] * 10
    
    for j in range(fi):
        for i in range(10):
            vector[i] += mt[j].count(i)
        
    maxim = max(vector)
    
    print(f"\nLISTA DE NUMEROS QUE MAS SE REPITEN (con un total de {maxim} repeticiones):\n")
    
    for i in range(10):
        if vector[i] == maxim:
            print(f"El numero {i} es de los que mas se repiten.\n")
    
    
    
def print_mtz(mt,fi,co):
    
    for f in range(fi):
        for c in range(co):
            print("%3d" %mt[f][c], end = " ")
        print()
    
fila = int(input("INGRESE LA CANTIDAD DE FILAS: "))
colu = int(input("INGRESE LA CANTIDAD DE COLUMNAS: "))

mtz = [[random.randint(0,9) for c in range(colu)] for f in range(fila)]

print()

print_mtz(mtz,fila,colu)
valor_masrep(mtz,fila,colu)
'''
'''
# LISTA CONCATENADORA

def carga_lista(lis,n):
    
    for i in range(n):
        az = random.randint(100,999)
        while az in lis:
            az = random.randint(100,999)
            
        lis.append(az)
    
    print("\nLISTA ORIGINAL --",lis)

def concatenar(ls):
    
    nro = (ls[0] * 1000) + ls[len(ls)-1]
    
    print("\nNUMERO CONCATENADO --",nro)
    
    lista = [x for x in range(1,nro+1) if nro % x == 0 or x == 1 or x == nro]
    
    print("\nLISTA DE DIVISORES DEL NUM CONCATENADO --", lista)
    
num = int(input("INGRESE LA CANTIDAD DE ELEMENTOS DE LA LISTA: "))
lis = []

carga_lista(lis,num)

lis.sort(key = lambda x: x // 10 % 10)

print("\nLISTA ORDENADA --",lis)

concatenar(lis)

'''
'''

# SUMA BELOW DP

def print_mt(mt):
    
    for i in range(len(mt)):
        for j in range(len(mt)):
            print("%3d" % mt [i][j], end = " ")
        print()

def below_dp(mt,n):
    
    suma = 0
    
    for i in range(1,n):
        for j in range(i):
            suma += mt[i][j]
    
    print("El total es de:",suma)
    
def over_dp(mt,n):
    
    suma = 0
    
    for i in range(1,n):
        for j in range(i+1,n):
            suma += mt[i][j]
    print("El total es de:",suma)
        
num = int(input("INGRESO DE RANGO DE LA MATRIZ: "))

mtz = [[random.randint(0,1) for c in range(num)] for f in range(num)]
print()
print_mt(mtz)
print()
below_dp(mtz,num)

'''
'''

# LISTA MULTIPLO-TERMINA 7

def sumadig(x):
    
    suma = 0
    
    while x > 0:
        
        suma += x % 10
        x //= 10
    
    return suma

num = int(input("INGRESE EL RANGO DE LA LISTA: "))

lista = [x for x in range(num) if x % 7 == 0 or x % 10 == 7]

print("\nLISTA ORIGINAL --",lista)

lista.sort(key = sumadig)

print("\nLISTA ORDENADA --",lista)

'''
'''

# IMPRIMIR MATRICES DE OTRA FORMA

num = 5

mtz = [[random.randint(0,9) for i in range(num)] for j in range(num)]

ctd = 1
for f in mtz:
    print(f"fila {ctd} ->", end = " ")
    ctd += 1
    for c in f:
        print("%3d" %c, end = " ")
    print()

'''