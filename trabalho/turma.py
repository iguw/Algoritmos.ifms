turmas = []

def gerar_codigo_turma():
    return f"T-{random.randint(1000, 9999)}"

def cadastrar_turma():
    nome = input("Digite o nome da turma: ").strip()
    codigo = gerar_codigo_turma()

    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastro cancelado.")
        return
    print("Escolha uma disciplina para a turma:")
    for i, disciplina in enumerate(disciplinas, start=1):
        print(f"{i}. {disciplina['nome']} (Código: {disciplina['codigo']})")
    escolha_disciplina = int(input("Digite o número correspondente: ").strip())
    if escolha_disciplina < 1 or escolha_disciplina > len(disciplinas):
        print("Opção inválida. Cadastro cancelado.")
        return
    disciplina_selecionada = disciplinas[escolha_disciplina - 1]

    if not professores:
        print("Nenhum professor cadastrado. Cadastro cancelado.")
        return
    print("Escolha um professor para a turma:")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor['nome']} (ID: {professor['id_professor']})")
    escolha_professor = int(input("Digite o número correspondente: ").strip())
    if escolha_professor < 1 or escolha_professor > len(professores):
        print("Opção inválida. Cadastro cancelado.")
        return
    professor_selecionado = professores[escolha_professor - 1]
    