import random
def jogo_adivinhar():
    numero_aleatorio = random.randint(0, 100)
    for n in range(numero_aleatorio):
        while n != numero_aleatorio:
            return 'numero errado'
        else:
            return 'voce acertou!'

n = int(input('digite um numero: '))

resultado = jogo_adivinhar()
print(f'{resultado}')