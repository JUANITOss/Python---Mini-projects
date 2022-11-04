# Este corto programa crea un diccionario de la tabla de multiplicar de un número del 1 al 12, y lo imprime de forma linda

def multiplica_nro(n):
    
    return {f"{n} por {x}": n * x for x in range(1,13)}

nro = int(input("Ingrese un número entero: "))

print(multiplica_nro(nro))
