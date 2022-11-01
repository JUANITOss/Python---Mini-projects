


# PASCAL TRIANGLE #


pascal = []
rango = int(input("Enter the length of your pascal triangle (the amout of lines it will get): "))

for i in range(rango):
    pascal.append([])
    pascal[i].append(1) 
    for j in range(1,i):
        pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
    if rango != 0:
        pascal[i].append(1)  
for i in range(rango):
    print(" "* (rango-i), end = " ")
    for j in range(i+1):
        print("%2d" %pascal[i][j], end = " ")
    print()

num = int(input("Enter the number: "))  
pascal = [] #an empty list  
for i in range(num):  
    pascal.append([])  
    pascal[i].append(1)  
    for j in range(1, i):  
        pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])  
    if(num != 0):  
        pascal[i].append(1) 
         
for i in range(num):  
    print(" " * (num - i), end = " ", sep = " ")  
    for j in range(0, i + 1):  
        print('{0:6}'.format(pascal[i][j]), end = " ", sep = " ")  
    print()  

num = int(input("Ingrese el numero:"))
    
for i in range(num):
    
    nro = 11**i
    print(""*(num-i),end = " ")
    print("",nro)
    print()