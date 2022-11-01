def romantoint(roman):
    
    rnums = {"M" : 1000,
        "CM" : 900,
        "D" : 500,
        "CD" : 400,
        "C" : 100,
        "XC" : 90,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1
    }

    rint = 0
    counter = 0

    while counter < len(roman):
        
        if counter+1 < len(roman) and roman[counter:counter+2] in rnums:
            rint += rnums[roman[counter:counter+2]]
            counter += 2
        
        elif roman[counter] in rnums:
            rint += rnums[roman[counter]]
            counter += 1
        
        else:
            print("\nThe roman number you entered is invalid. Please try again.")
            counter = 0
            break

    if counter == 0:
        return False
    
    if rint<=0 or rint>=3999 or len(roman) > 15:
        return False
    
    return rint

nro = input("Ingrese su numero romano: ")

nro = romantoint(nro.upper())


while not nro:

    nro = input("\nIngrese su numero romano: ")

    nro = romantoint(nro.upper())

print(f"\nThe number you entered equals to {nro} when converted to integer.")