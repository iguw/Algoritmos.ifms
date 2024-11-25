def calcular_notas(lista_notas):
    if not lista_notas:
        return 0, []
    media = sum(lista_notas) / len(lista_notas)
    notas_acima_da_media = [nota for nota in lista_notas if nota > media]
    return media, notas_acima_da_media


notas = input("Digite as notas separadas por espaço: ").split()
notas = [float(nota) for nota in notas]

media, notas_acima = calcular_notas(notas)

print(f"A média das notas é: {media:.2f}")
print(f"As notas acima da média são: {notas_acima}")