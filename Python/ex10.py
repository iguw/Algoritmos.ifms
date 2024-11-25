def area_retangulo(base, altura):
    return base * altura


base = float(input("digite a base do retângulo: "))
altura = float(input("digite a altura do retangulo: "))
area = area_retangulo(base, altura)

print(f"a area do retangulo é: {area}")