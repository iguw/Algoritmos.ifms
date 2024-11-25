def calcular(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"


numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))
operacao = input("digite a operação (+, -, *, /): ")


resultado = calcular(numero1, numero2, operacao)
print(f"resultado: {resultado}")