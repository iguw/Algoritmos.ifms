def contador(frase):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    frase = frase.lower()
    num_vogais = 0
    num_consoantes = 0
    for char in frase:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes += 1
    return num_vogais, num_consoantes


frase = input("digite uma frase: ")

vogais, consoantes = contador(frase)


print(f"Numero de vogais: {vogais}")
print(f"Numero de consoantes: {consoantes}")