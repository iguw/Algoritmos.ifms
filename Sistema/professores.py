import random
import string
professores = []

def gerar_codigo_professor(): #gerador de codigos para professores
    numero = random.randint(100000, 99999)
    letra = random.choice(string.ascii_uppercase)
    return f"{numero:05}{letra}"

#cadastro de professores
def cadastrar_professor():
    id_professor = gerar_codigo_professor
    nome = input("Digite o nome do aluno")
    data_nascimento = input("Digite a data de nascimento do aluno")
    sexo = input("Digite o sexo do aluno (M/F)")
    endereco = input("Digite o endereço")
    telefone = input("Digite o telefone")
    email = input("Digite o email do aluno")
    
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
    