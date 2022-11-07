# Este programa utiliza a los sets para asegurarse de que una palabra no se repita en una frase.

def limpiapalabras(palabra):
    
    i = 0
    
    j = len(palabra)-1
    
    while i<len(palabra) and not palabra[i].isalpha():
        i += 1
    
    while j>i and not palabra[j].isalpha():
        j -= 1
    
    return palabra[i:j+1]

def norep_frase(frase):
    
    norep = set()
    fraseclean = list()
    
    for palabra in frase:
        
        norep.add(palabra)
    
    for palabra in norep:
        
        fraseclean.append(palabra)
    
    return fraseclean.sort(key=len)

phrs = input("Ingrese una frase a continuación: ")    

phrs = phrs.split()

for i,word in enumerate(phrs):
    
    phrs[i] = limpiapalabras(word)

print(norep_frase(phrs))
