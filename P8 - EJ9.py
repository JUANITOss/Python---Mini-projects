def multiplica_nro(n):
    
    return {f"{n} por {x}": n * x for x in range(1,13)}

nro = int(input("Ingrese un número entero: "))

print(multiplica_nro(nro))

# while True:
    
#     try:
        
#         nro = int(input("Ingrese un número entero: "))
        
#         tabla = multiplica_nro(nro)
        
#         print(tabla)
        
#         break
        
#     except ValueError as msg:
        
#         print("INGRESO INVÁLIDO --",msg)
#         continue