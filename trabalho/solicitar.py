def obter_entrada(mensagem, condicao=None, mensagem_erro=None):
    while True:
        entrada = input(mensagem).strip()
        if condicao is None or condicao(entrada):
            return entrada
        if mensagem_erro:
            print(mensagem_erro)
