def encontrar_primos(inicio, fim):
    def numero_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    primos = [num for num in range(inicio, fim + 1) if numero_primo(num)]
    return primos

inicio = int(input("digite o início do intervalo: "))
fim = int(input("digite o fim do intervalo: "))

primos = encontrar_primos(inicio, fim)
print(f"numeros primos entre {inicio} e {fim}: {primos}")