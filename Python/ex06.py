def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
    
n1 = float(input("digite sua nota: "))
n2 = float(input("digite sua outra nota: "))
n3 = float(input("digite sua ultima nota: "))

media_notas = media(n1, n2, n3)
print(f"a sua média é: {media_notas}")