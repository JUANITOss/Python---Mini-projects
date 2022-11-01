def contarvocales(word):
    return {x : word.count(x) for x in word if x in "aeiou"}

frase = input("Ingrese una frase: ")
frase = frase.split()

for palabra in frase:
    print(f"{palabra} -> {contarvocales(palabra)}")