def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


numero = int(input("digite um número para calcular o fatorial: "))

if numero < 0:
    print("o fatorial não é definido para números negativos.")
else:
    fatorial = fatorial(numero)
    print(f"O fatorial de {numero} é: {fatorial}")