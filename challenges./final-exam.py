def dataValidator (data, condSup, condInf):
    
    if data <= condSup or data >= condInf:
        return True
    
    return False

def lenValidator (data, condLen):

    if len(data) != condLen:
        return False
    
    return True

def bubblesort(base, comp):

    for i in range(len(base)-1):
        for j in range(i+1, len(base)):

            if base[i] < base[j]:

                aux = base[i]
                base[i] = base[j]
                base[j] = aux

                aux = comp[i]
                comp[i] = comp[j]
                comp[j] = aux
                
# Main

dictProducts = dict()
totalOfYear = 0
products = []
stock = []

try:

    archBS = open("final-exam.txt")

    line = archBS.readline()

    # Block of code for data extraction, validation and processing

    while line != "":

        date = line[:10]

        dd, mm, aa = date.split(" ")

        if not dataValidator(int(dd), 31, 1) or not dataValidator(int(mm), 12, 1) or not lenValidator(aa, 4):
            
            print("Incorrect date")
            line = archBS.readline()

            continue

        price = line[36:]

        digs, decs = price.split(".")

        decs = decs.strip()
        
        if not dataValidator(int(digs), 999, 0) or not dataValidator(int(decs), 99, 0) or not lenValidator(digs, 3) or not lenValidator(decs, 2):
            
            print("Incorrect pricing")
            line = archBS.readline()
            
            continue            

        if line[11:14].isdigit():

            units = line[11:14]
            product = line[14:35].strip(" ")

            dictProducts[product] = dictProducts.get(product, 0) - int(units)

            if aa == "2009":
                totalOfYear -= int(units) * float(price)

        else:

            units = line[32:35]
            product = line[11:32].strip(" ")

            dictProducts[product] = dictProducts.get(product, 0) + int(units)

            if aa == "2009":
                totalOfYear += int(units) * float(price)

        if not dataValidator(int(units), 999, 1):
            
            print("Incorrect amount of units")
            line = archBS.readline()
            
            continue
        
        line = archBS.readline()

    # for items in dictProducts:

    #     products.append(items)
    #     stock.append(dictProducts[items])

    # bubblesort(stock, products)

    # for i in range(len(products)):

    #     print(f"-> {stock[i]} unidades de {products[i]}\n")

    print("\nLISTADO DE STOCK DE PRODUCTOS\n")

    # Orders the dict of products by the index = 1 (value) pf the dictProducts.items() tuple list

    for k,v in sorted(dictProducts.items(), key=lambda tupl: tupl[1]):
        print(f"-> {k}, con un stock de {v} productos")


    print(f"\nEl total recaudado en el año 2009 es de ${totalOfYear:.2f}")

except FileNotFoundError as msg:
    print(f"El archivo no se ha encontrado. {msg}")

finally:

    try:
        archBS.close()
    
    except NameError:

        pass