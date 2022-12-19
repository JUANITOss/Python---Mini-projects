def rangeValidator(data, infLim, supLim):

    if infLim <= data and data <= supLim:
        return True
    
    return False

def lenValidator(data, desiredLen):

    if len(data) == desiredLen:
        return True
    
    return False

def sortByAmount(struct, minToMax = True):

    orderdedList = []

    for k,v in sorted(struct, key = lambda x: x[1], reverse=minToMax):

        orderdedList.append(f"-> {k} has '{v}' units available.")

    return orderdedList


# Main Program

totalMoney = 0
dictForProducts = dict()

try:

    archBuySell = open("final-exam.txt", "rt")

    line = archBuySell.readline()

    while line != "":

        # Extracting the date

        date = line[:10]

        dd, mm, aaaa = date.split(" ")

        assert rangeValidator(int(dd), 1, 31) and rangeValidator(int(mm), 1, 12), "date or the month, they are invalid numbers"
        assert lenValidator(dd, 2) and lenValidator(mm, 2) and lenValidator(aaaa, 4), "length of the values for the days, months or years"

        # Extracting Value of Units

        nnn = line[36:]

        dig, dec = nnn.strip().split(".")

        assert lenValidator(dig, 3) and lenValidator(dec, 2), "lengths of the values of units being sold/bought"
        
        # Extracting type of product and available amount for them

        if line[11:14].strip().isdigit():
            
            # FOR SELLING PRODUCTS (earning money and having less stock)
            
            stock = line[11:14].strip()
            prod = line[15:35]

            assert lenValidator(prod, 20) and lenValidator(stock, 3), "lengths of the stock or the name of the product"

            dictForProducts[prod] = dictForProducts.get(prod, 0) - int(stock)

            if aaaa == "2009":
                totalMoney += int(stock) * float(nnn)                

        else:
            
            # FOR BUYING (losing money and gaining stock)

            stock = line[32:35].strip()
            prod = line[11:31]
            
            assert lenValidator(prod, 20) and lenValidator(stock, 3), "lengths of the stock or the name of the product"

            dictForProducts[prod] = dictForProducts.get(prod, 0) + int(stock)

            if aaaa == "2009":
                totalMoney -= int(stock) * float(nnn)                

        line = archBuySell.readline()

    # SHOWING FINAL INFO

    print(f"The amount of money obtained in the year 2009 is of ${totalMoney:.2f}.\n")

    print(f"LIST OF ITEMS ORDERED BY STOCK (From lowest to highest amount):")

    printer = sortByAmount(dictForProducts.items())

    for elements in printer:

        print(elements, end ="\n")

except OSError as msg:
    print(f"The program failed. {msg}")

except AssertionError as msg:
    print(f"The file you tried to open had errors. Check the {msg}.")

finally:

    try:
        archBuySell.close()
    
    except:
        pass