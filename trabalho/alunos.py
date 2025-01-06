import random
import string
from solicitar import obter_entrada

alunos = []

def gerar_matricula():
    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase)
    matricula = f"{numero:05}{letra}"
    return matricula

def cadastrar_alunos():
    id_aluno = gerar_matricula()

    nome = obter_entrada("Digite o nome do aluno: ")
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

    cursos = obter_entrada(
        "Digite os cursos que o aluno está matriculado (separados por vírgulas): "
    ).split(",")

    aluno = {
        "nome": nome,
        "id_aluno": id_aluno,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "cursos": [curso.strip() for curso in cursos],
    }

    alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucesso!\n")

def listagem_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
    else:
        print("\n=== Lista de Alunos ===")
        for aluno in alunos:
            print(
                f"ID: {aluno['id_aluno']}, Nome: {aluno['nome']}, Cursos: {', '.join(aluno['cursos'])}"
            )
    print("\n")

def excluir_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado para exclusão.\n")
        return

    print("\n=== Lista de Alunos Cadastrados ===")
    for aluno in alunos:
        print(f"ID: {aluno['id_aluno']}, Nome: {aluno['nome']}")
    print()

    id_aluno = obter_entrada(
        "Digite o ID do aluno para excluir: ",
        validacao=lambda x: any(a["id_aluno"] == x for a in alunos),
        erro="Aluno não encontrado.",
    )

    aluno = next(a for a in alunos if a["id_aluno"] == id_aluno)
    alunos.remove(aluno)
    print(f"Aluno com ID {id_aluno} excluído com sucesso!\n")

def filtrar_alunos_por_curso():
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    cursos_cadastrados = set(
        curso
        for aluno in alunos
        for curso in aluno.get("cursos", [])
    )

    if not cursos_cadastrados:
        print("Nenhum curso encontrado nos alunos cadastrados.")
        return

    print("\n=== Cursos Disponíveis ===")
    for curso in sorted(cursos_cadastrados):
        print(f"- {curso}")

    curso_escolhido = obter_entrada(
        "\nDigite o nome do curso para filtrar: ",
        validacao=lambda x: x in cursos_cadastrados,
        erro="Curso não encontrado.",
    )

    alunos_filtrados = [
        aluno
        for aluno in alunos
        if curso_escolhido in aluno.get("cursos", [])
    ]

    if not alunos_filtrados:
        print(
            f"Nenhum aluno encontrado para o curso '{curso_escolhido}'."
        )
    else:
        print(f"\n=== Alunos matriculados no curso '{curso_escolhido}' ===")
        for aluno in alunos_filtrados:
            print(f"ID: {aluno['id_aluno']}, Nome: {aluno['nome']}")