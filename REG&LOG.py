import sqlite3
conexão_contas = sqlite3.connect('contas.db')
cursor_contas = conexão_contas.cursor()
cursor_contas.execute('''create table contas(nome text, senha text)''')


def pergunta_reg_ou_log():
    try:
        print("--" * 20)
        rl = int(input("Você deseja registrar[1], logar[2] ou sair[3]? "))
        if rl == 1:
            registrar()
        elif rl == 2:
            logar()
        elif rl == 3:
            print("Adeus, volte sempre!")
        else:
            print("\nNúmeros invalidos, escolhe entre 1 e 2!")
            pergunta_reg_ou_log()
    except ValueError as VE:
        print("\nEscreva apenas números")
        pergunta_reg_ou_log()
    print("--" * 20)

def registrar():
    nome = input("Digite seu novo nome aqui: ")
    senha = input("Digite sua nova senha aqui: ")
    cursor_contas.execute('''insert into contas(nome, senha) values(?, ?)''', (nome, senha))
    conexão_contas.commit()
    cursor_contas.execute('''select * from contas''')
    result = cursor_contas.fetchall()
    print("Registro bem sucedido!")
    pergunta_reg_ou_log()

def logar():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    cursor_contas.execute('''select * from contas where nome = ? and senha = ?''', (nome,senha))
    result = cursor_contas.fetchone()
    if result:
        print(f"O nome '{nome}' e a senha '{senha}' estão presentes na tabela.")
    else:
        print(f"O nome '{nome}' e/ou a senha '{senha}' não estão presentes na tabela.")
pergunta_reg_ou_log()