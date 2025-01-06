import random
import string
from solicitar import obter_entrada

professores = []

def gerar_matricula():

    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase)
    matricula = f"{numero:05}{letra}"
    return matricula

def cadastrar_professores():
    id_professor = gerar_matricula()

    nome = obter_entrada("Digite o nome do professor: ")
    data_nascimento = obter_entrada(
        "Digite a data de nascimento (DD/MM/AAAA): ",
        validacao=lambda x: len(x) == 10 and x[2] == "/" and x[5] == "/",
    )
    sexo = obter_entrada(
        "Digite o sexo (M/F): ",
        validacao=lambda x: x in ["M", "F"],
        erro="Sexo deve ser 'M' ou 'F'. Tente novamente.",
    )
    endereco = obter_entrada("Digite o endereço: ")
    telefone = obter_entrada(
        "Digite o telefone (apenas números): ",
        validacao=lambda x: x.isdigit(),
        erro="Telefone deve conter apenas números. Tente novamente.",
    )
    email = obter_entrada("Digite o email: ")

    disciplinas = obter_entrada(
        "Digite as disciplinas lecionadas (separadas por vírgulas): "
    ).split(",")

    professor = {
        "nome": nome,
        "id_professor": id_professor,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplinas": [
            disciplina.strip() for disciplina in disciplinas
        ],
    }

    professores.append(professor)
    print(f"Professor {professor['nome']} cadastrado com sucesso!\n")

def listagem_professor():
    if not professores:
        print("Nenhum professor cadastrado ainda.")
    else:
        print("\n=== Lista de Professores ===")
        for professor in professores:
            print(
                f"ID: {professor['id_professor']}, Nome: {professor['nome']}, Disciplinas: {', '.join(professor['disciplinas'])}"
            )
    print("\n")

def excluir_professor():
    if not professores:
        print("Nenhum professor cadastrado para exclusão.\n")
        return

    print("\n=== Lista de Professores Cadastrados ===")
    for professor in professores:
        print(f"ID: {professor['id_professor']}, Nome: {professor['nome']}")
    print()

    id_professor = obter_entrada(
        "Digite o ID do professor para excluir: ",
        validacao=lambda x: any(p["id_professor"] == x for p in professores),
        erro="Professor não encontrado.",
    )

    professor = next(p for p in professores if p["id_professor"] == id_professor)
    professores.remove(professor)
    print(f"Professor com ID {id_professor} excluído com sucesso!\n")

def filtrar_professores_por_disciplina():
    if not professores:
        print("Nenhum professor cadastrado no sistema.")
        return

    disciplinas_cadastradas = set(
        disciplina
        for professor in professores
        for disciplina in professor.get("disciplinas", [])
    )

    if not disciplinas_cadastradas:
        print("Nenhuma disciplina encontrada nos professores cadastrados.")
        return

    print("\n=== Disciplinas Disponíveis ===")
    for disciplina in sorted(disciplinas_cadastradas):
        print(f"- {disciplina}")

    disciplina_escolhida = obter_entrada(
        "\nDigite o nome da disciplina para filtrar: ",
        validacao=lambda x: x in disciplinas_cadastradas,
        erro="Disciplina não encontrada.",
    )

    professores_filtrados = [
        professor
        for professor in professores
        if disciplina_escolhida in professor.get("disciplinas", [])
    ]

    if not professores_filtrados:
        print(
            f"Nenhum professor encontrado para a disciplina '{disciplina_escolhida}'."
        )
    else:
        print(f"\n=== Professores que ministram '{disciplina_escolhida}' ===")
        for professor in professores_filtrados:
            print(f"ID: {professor['id_professor']}, Nome: {professor['nome']}")