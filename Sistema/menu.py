from alunos import (cadastrar_aluno)
from disciplinas import (cadastrar_disciplina)
from professores import (cadastrar_professor)
from turmas import (cadastrar_turma)

#menu
def menu():
    while True:
        print("---Sistema Escolar---")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Disciplina")
        print("4. Cadastrar Turma")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            cadastrar_disciplina()
        elif escolha == "3":
            cadastrar_professor()
        elif escolha == "4":
            cadastrar_turma()
        elif escolha == "5":
            print("Sair")
            break
        else:
            print("Opção invalida, tente novamente")
menu()