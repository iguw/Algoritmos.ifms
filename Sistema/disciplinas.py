import random

disciplinas = []

def gerar_codigo_disciplina(): #gerador de codigos para disciplinas
    return f"A{random.randint(1000, 9999)}"

#cadastro de disciplina
def cadastrar_disciplina():
    codigo_disciplina = gerar_codigo_disciplina
    nome = input("Digite o nome da disciplina")
    carga_horaria = input("Digite a carga horaria da disciplina")
    professor_id = input("Digite o ID do professor")

    disciplina = {
        "codigo_disciplina": codigo_disciplina,
        "nome": nome,
        "carga_horaria": carga_horaria,
        "professor": professor_id,
    }
    disciplinas.append(disciplina)
    