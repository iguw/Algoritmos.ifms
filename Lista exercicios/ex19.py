def contar_caracteres(frase):
    dicionario = {}
    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1
    return dicionario

frase = input("digite uma frase: ")

resultado = contar_caracteres(frase)
print("contagem de caracteres:")
for caractere, quantidade in resultado.items():
    print(f"'{caractere}': {quantidade}")