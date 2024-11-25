def sao_anagramas(palavra1, palavra2):
    palavra1 = ''.join(sorted(palavra1.replace(" ", "").lower()))
    palavra2 = ''.join(sorted(palavra2.replace(" ", "").lower()))
    return palavra1 == palavra2


palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")


if sao_anagramas(palavra1, palavra2):
    print(f"'{palavra1}' e '{palavra2}' são anagramas!")
else:
    print(f"'{palavra1}' e '{palavra2}' não são anagramas.")