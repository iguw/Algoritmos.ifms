from collections import Counter
def palavras_mais_frequentes(texto):

    palavras = texto.lower().split()
    contador = Counter(palavras)
    mais_comuns = contador.most_common(5)
    return mais_comuns


texto = input("digite um texto longo: ")
resultado = palavras_mais_frequentes(texto)

print("as 5 palavras mais frequentes no texto são:")
for palavra, frequencia in resultado:
    print(f"'{palavra}': {frequencia} vez(es)")
