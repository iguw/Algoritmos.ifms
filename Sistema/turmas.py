import random
turmas = []

def gerar_codigo_turma(): #gerador de codigos para turmas
    return f"T-{random.randit(1000, 9999)}"

#cadastro de turma
def cadastrar_turma():
    codigo_turma = gerar_codigo_turma
    nome_turma = input("Digite o nome da turma")
    disciplinas = input("Digite o codigo da disciplina")
    
    turma = {
        "codigo_turma": codigo_turma,
        "nome_turma": nome_turma,
        "disciplinas": disciplinas
    }
    turmas.append(turma)
    