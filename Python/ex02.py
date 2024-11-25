def par_impar (numero):
    if numero % 2 ==0:
        return "é par"
    else:
        return "é impar"
    
numero = int(input("digite um numero: "))
resultado = par_impar(numero)
print(resultado)