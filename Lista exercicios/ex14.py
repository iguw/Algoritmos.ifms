def palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]


palavra = input("digite uma palavra: ")


if palindromo(palavra):
    print(f"a palavra '{palavra}' é um palíndromo")
else:
    print(f"a palavra '{palavra}' não é um palíndromo")