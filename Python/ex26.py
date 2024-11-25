def mesclar_dicionarios(dicionario1, dicionario2):
    dicionario_mesclado = dicionario1.copy()
    for chave, valor in dicionario2.items():
        if chave in dicionario_mesclado:
            dicionario_mesclado[chave] += valor
        else:
            dicionario_mesclado[chave] = valor
    return dicionario_mesclado


dicionario1 = {'a': 10, 'b': 5, 'c': 7}
dicionario2 = {'a': 3, 'b': 8, 'd': 4}


resultado = mesclar_dicionarios(dicionario1, dicionario2)


print(f"dicionário mesclado: {resultado}")