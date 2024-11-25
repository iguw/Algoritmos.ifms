def tabuada(numero):
    print(f"a tabuada de {numero} é: ")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("digite um numero: "))
tabuada(numero)