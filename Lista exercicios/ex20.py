def gerar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


n = int(input("digite a quantidade de números da sequência de Fibonacci: "))


sequencia = gerar_fibonacci(n)
print(f"os {n} primeiros números da sequência de Fibonacci são: {sequencia}")
