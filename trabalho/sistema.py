import random
import string

alunos = []
professores = []
disciplinas = []
turmas = []

def gerar_codigo_professor():
    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase)
    return f"{numero:05}{letra}"

def gerar_codigo_disciplina():
    return f"A{random.randint(1000, 9999)}"

def gerar_codigo_turma():
    return f"T-{random.randint(1000, 9999)}"

def cadastrar_aluno():
    matricula = input("Digite a matrícula do aluno (exemplo: 12837382-8): ")
    nome = input("Digite o nome do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
    sexo = input("Digite o sexo do aluno (M/F): ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno: ")

    aluno = {
        "matricula": matricula,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def cadastrar_professor():
    id_professor = gerar_codigo_professor()
    nome = input("Digite o nome do professor: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    sexo = input("Digite o sexo (M/F): ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    professor = {
        "id_professor": id_professor,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso!, ID do Professor: {id_professor}")


def cadastrar_disciplina():
    codigo = gerar_codigo_disciplina()
    nome = input("Digite o nome da disciplina: ")
    carga_horaria = input("Digite a carga horária (em horas): ")
    professor_id = input("Digite o ID do professor responsável pela disciplina: ")

    professor = next((p for p in professores if p["id_professor"] == professor_id), None)
    if not professor:
        print("Professor não encontrado.")
        return

    disciplina = {
        "codigo": codigo,
        "nome": nome,
        "carga_horaria": carga_horaria,
        "professor": professor_id
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!, Código da Disciplina: {codigo}")


def cadastrar_turma():
    nome_turma = input("Digite o nome da turma: ")
    codigo_turma = gerar_codigo_turma()
    disciplina_codigo = input("Digite o código da disciplina que será alocada à turma: ")

    disciplina = next((d for d in disciplinas if d["codigo"] == disciplina_codigo), None)
    if not disciplina:
        print("Disciplina não encontrada.")
        return

    professor_id = disciplina["professor"]
    professor = next((p for p in professores if p["id_professor"] == professor_id), None)

    turma = {
        "nome": nome_turma,
        "codigo": codigo_turma,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": []
    }
    turmas.append(turma)
    print(f"Turma {nome_turma} cadastrada com sucesso!, Código da Turma: {codigo_turma}")


def matricular_aluno_em_turma():
    if not alunos:
        print("Nenhum aluno cadastrado. Cadastre um aluno primeiro.")
        return
    
    print("\nAlunos disponíveis para matrícula:")
    for aluno in alunos:
        print(f"- Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")

    matricula = input("\nDigite a matrícula do aluno a ser matriculado: ").strip()
    aluno = next((a for a in alunos if a["matricula"] == matricula), None)
    if not aluno:
        print("Aluno não encontrado. Verifique a matrícula e tente novamente.")
        return
    print(f"Aluno encontrado: {aluno['nome']}")

    if not turmas:
        print("Nenhuma turma cadastrada. Cadastre uma turma primeiro.")
        return

    print("\nTurmas disponíveis:")
    for i, turma in enumerate(turmas, start=1):
        print(f"{i}. Nome: {turma['nome']}, Código: {turma['codigo']}")

    escolha = input("\nEscolha a turma pelo número correspondente: ").strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(turmas):
        print("Opção inválida. Tente novamente.")
        return

    turma_escolhida = turmas[int(escolha) - 1]
    print(f"Turma escolhida: {turma_escolhida['nome']}")

    turma_escolhida["alunos"].append(aluno)
    print(f"\nAluno {aluno['nome']} matriculado com sucesso na turma {turma_escolhida['nome']}.")

#Consultas
def consultar_alunos_na_turma():
    codigo_turma = input("Digite o código da turma para consultar os alunos: ")
    turma = next((t for t in turmas if t["codigo"] == codigo_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    print(f"\nAlunos matriculados na turma {turma['nome']}:")
    for aluno in turma["alunos"]:
        print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']})")

def consultar_professor_por_disciplina():
    codigo_disciplina = input("Digite o código da disciplina para consultar o professor: ")
    disciplina = next((d for d in disciplinas if d["codigo"] == codigo_disciplina), None)
    if not disciplina:
        print("Disciplina não encontrada.")
        return

    professor = next((p for p in professores if p["id_professor"] == disciplina["professor"]), None)
    print(f"Professor responsável pela disciplina {disciplina['nome']}: {professor['nome']}")

def consultar_disciplinas_em_turma():
    codigo_turma = input("Digite o código da turma para consultar as disciplinas: ")
    turma = next((t for t in turmas if t["codigo"] == codigo_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    print(f"\nDisciplina alocada na turma {turma['nome']}: {turma['disciplina']['nome']}")

#Menu
def menu():
    while True:
        print("\n--- Sistema Escolar ---")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Disciplina")
        print("4. Cadastrar Turma")
        print("5. Matricular Aluno em Turma")
        print("6. Consultar Alunos em uma Turma")
        print("7. Consultar Professor de uma Disciplina")
        print("8. Consultar Disciplinas de uma Turma")
        print("9. Sair")

        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            cadastrar_professor()
        elif escolha == "3":
            cadastrar_disciplina()
        elif escolha == "4":
            cadastrar_turma()
        elif escolha == "5":
            matricular_aluno_em_turma()
        elif escolha == "6":
            consultar_alunos_na_turma()
        elif escolha == "7":
            consultar_professor_por_disciplina()
        elif escolha == "8":
            consultar_disciplinas_em_turma()
        elif escolha == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
menu()