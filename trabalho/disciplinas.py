import random
from professores import (
    listagem_professores, professores
)
from solicitar import obter_entrada


disciplinas = []


def gerar_codigo():
    return f"D-{random.randint(1000, 9999)}"


def cadastrar_disciplina():
    codigo = gerar_codigo()
    print(f"Código da disciplina gerado: {codigo}")

    nome = input("Digite o nome da disciplina: ").strip()
    carga_horaria = input("Digite a carga horária (em horas): ").strip()

    listagem_professores()

    professor_escolhido = obter_entrada(
        "Escolha o ID do professor que irá ministrar a disciplina: ",
        lambda x: any(prof["id_professor"] == x for prof in professores),
        "Professor não encontrado.",
    )

    professor = next(
        (prof for prof in professores if prof["id_professor"] == professor_escolhido),
        None,
    )

    disciplina = {
        "codigo": codigo,
        "nome": nome,
        "carga_horaria": carga_horaria,
        "professor": {"id": professor["id_professor"], "nome": professor["nome"]},
    }

    disciplinas.append(disciplina)
    print(f"Disciplina '{nome}' cadastrada com sucesso!\n")


def listar_disciplinas():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada ainda.")
    else:
        print("\n=== Lista de Disciplinas ===")
        for disciplina in disciplinas:
            print(
                f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}, "
                f"Carga Horária: {disciplina['carga_horaria']}h, "
                f"Professor: {disciplina['professor']['nome']} (ID: {disciplina['professor']['id']})"
            )
    print("\n")


def excluir_disciplina():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada para exclusão.\n")
        return

    listar_disciplinas()
    codigo_disciplina = obter_entrada(
        "Digite o código da disciplina para excluir: ",
        lambda x: any(d["codigo"] == x for d in disciplinas),
        "Disciplina não encontrada.",
    )

    disciplina = next(
        (d for d in disciplinas if d["codigo"] == codigo_disciplina), None
    )

    disciplinas.remove(disciplina)
    print(f"Disciplina com código {codigo_disciplina} excluída com sucesso!\n")


def inserir_professor_em_disciplina():
    if not professores:
        print("Nenhum professor cadastrado. Operação cancelada.")
        return

    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Operação cancelada.")
        return

    listar_disciplinas()
    codigo_disciplina = obter_entrada(
        "Digite o código da disciplina para alocar o professor: ",
        lambda x: any(d["codigo"] == x for d in disciplinas),
        "Disciplina não encontrada.",
    )

    disciplina = next(d for d in disciplinas if d["codigo"] == codigo_disciplina)

    listagem_professores()
    professor_id = obter_entrada(
        "Digite o ID do professor para alocar: ",
        lambda x: any(p["id_professor"] == x for p in professores),
        "Professor não encontrado.",
    )

    professor = next(p for p in professores if p["id_professor"] == professor_id)

    if "professor" in disciplina and disciplina["professor"]:
        confirmacao = input(
            f"Esta disciplina já tem um professor alocado ({disciplina['professor']['nome']}). Deseja substituí-lo? (S/N): "
        ).strip().upper()
        if confirmacao != "S":
            print("Operação cancelada.")
            return

    disciplina["professor"] = {"id": professor["id_professor"], "nome": professor["nome"]}
    print(f"Professor {professor['nome']} alocado com sucesso à disciplina '{disciplina['nome']}'!\n")


def consultar_professor_por_disciplina():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada ainda.")
        return

    listar_disciplinas()
    codigo_disciplina = obter_entrada(
        "Digite o código da disciplina para consultar o professor: ",
        lambda x: any(d["codigo"] == x for d in disciplinas),
        "Disciplina não encontrada.",
    )

    disciplina = next(d for d in disciplinas if d["codigo"] == codigo_disciplina)
    professor = disciplina["professor"]

    print(f"\nProfessor alocado para a disciplina '{disciplina['nome']}':")
    print(f"Nome: {professor['nome']}, ID: {professor['id']}\n")