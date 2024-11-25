def quantidade_caracteres(palavra):
    return len(palavra)

palavra = input("digite uma palavra: ")
contador = quantidade_caracteres(palavra)
print(f"a quantidade de letras nessa palavra é: {contador}")