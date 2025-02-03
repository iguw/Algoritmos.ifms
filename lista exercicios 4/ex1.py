# Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma string s e devolve a string invertida. Não use laços (for ou while).
string = 'Exemplo'

reverter = lambda x : x if len(x) <= 1 else x[-1] + reverter(x[:-1])

reverter_caractere = reverter(string)

print(reverter_caractere)