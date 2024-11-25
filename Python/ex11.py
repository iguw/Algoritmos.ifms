def contador_palavras(frase):
    palavras = frase.lower().split()
    palavras_unicas = set(palavras)
    return len(palavras_unicas)



frase = input("digite uma frase: ")
quantidade_unicas = contador_palavras(frase)

print(f"a frase possui {quantidade_unicas} palavras unicas.")