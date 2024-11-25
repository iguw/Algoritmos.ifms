def invertendo_palavra(palavra):
    return palavra[::-1]

palavra = str(input("digite uma palavra: "))
resultado = invertendo_palavra(palavra)
print(resultado)