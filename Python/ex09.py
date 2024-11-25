def verificar_idade(idade):
    if idade >= 18:
        return "voce é maior de idade"
    else:
        return "voce é menor de idade"
    
idade = int(input("digite sua idade: "))
resultado = verificar_idade(idade)
print({resultado})