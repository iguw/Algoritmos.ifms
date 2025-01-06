import random
from disciplinas import listar_disciplinas, disciplinas
from professores import professores
from alunos import alunos

turmas = []

def gerar_codigo_turma():
    return f"T-{random.randint(1000, 9999)}"

def selecionar_opcao(lista, descricao):
    if not lista:
        print(f"Nenhum(a) {descricao} disponível. Operação cancelada.")
        return None

    print(f"\nEscolha um(a) {descricao}:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item['nome']}")

    escolha = input("Digite o número correspondente: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(lista):
        return lista[int(escolha) - 1]

    print("Opção inválida. Operação cancelada.")
    return None
