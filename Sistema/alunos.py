import random

alunos = []

#cadastro de alunos
def cadastrar_aluno():
    nome = input("Digite o nome do aluno")
    matricula = input("Digite o codigo da matricula")
    data_nascimento = input("Digite a data de nascimento do aluno")
    sexo = input("Digite o sexo do aluno (M/F)")
    endereco = input("Digite o endereço")
    telefone = input("Digite o telefone")
    email = input("Digite o email do aluno")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    alunos.append(aluno)
