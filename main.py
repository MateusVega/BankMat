import sqlite3
import uuid
from datetime import datetime
import os
from time import sleep

conexão_contas = sqlite3.connect('contas.db')
cursor_contas = conexão_contas.cursor()
cursor_contas.execute('''create table contas(nome text, senha text, account text, saldo real)''')
cursor_contas.execute('''create table transacao(valor real, tipo text, dia text)''')

def pergunta_reg_ou_log():
    header()
    try:
        rl = int(input("Você deseja registrar[1], logar[2] ou sair[3]? "))
        if rl == 1:
            registrar()
        elif rl == 2:
            logar()
        elif rl == 3:
            header()
            print("Adeus, volte sempre!")
            print("--" * 20)
        else:
            print("\nNúmeros invalidos, escolhe entre 1 e 3!")
            pergunta_reg_ou_log()
    except ValueError as VE:
        print("\nEscreva apenas números")
        pergunta_reg_ou_log()
def header():
    os.system('cls')
    print("="* 52)
    print("                    MATEUS BANK")
    print("="* 52)
    print("\n")
def registrar():
    header()
    nome = input("Digite seu novo nome aqui: ")
    senha = input("Digite sua nova senha aqui: ")
    account = str(uuid.uuid4())
    saldo = 0.00
    cursor_contas.execute('''insert into contas(nome, senha, account, saldo) values(?, ?, ?, ?)''', (nome, senha, account, saldo))
    conexão_contas.commit()
    cursor_contas.execute('''select * from contas''')
    result = cursor_contas.fetchall()
    print("Registro bem sucedido!")
    pergunta_reg_ou_log()
def logar():
    header()
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    cursor_contas.execute('''select * from contas where nome = ? and senha = ?''', (nome,senha))
    result = cursor_contas.fetchone()
    if result:
        print(f"O nome '{nome}' e a senha '{senha}' estão presentes no nosso banco de dados.")
        bank(nome,senha)

    else:
        print(f"O nome '{nome}' e/ou a senha '{senha}' não estão presentes no nosso banco de dados.")
        sleep(3)
        pergunta_reg_ou_log()
def bank(name,senha):
    sleep(2)
    header()
    opt = int(input(f"Olá {name}, o que você deseja fazer? \n\t[1]OLHAR SALDO\n\t[2]DEPOSITAR SALDO\n\t[3]RETIRAR SALDO\n\t[4]OLHAR ESTRATO\n\t[5]SAIR\n"))
    if opt == 1:
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo = cursor_contas.fetchone()[0]
        print(f"Olá {name}, o seu saldo atual é {saldo}")
        bank(name,senha)
    elif opt ==2:
        tipo = "Depositou"
        data_hora = datetime.now().strftime('%Y-%m-%d')
        val_to_dep = float(input("Quanto você deseja depositar? "))
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo_atual = cursor_contas.fetchone()[0]
        novo_saldo = saldo_atual + val_to_dep
        cursor_contas.execute('''UPDATE contas SET saldo = ? WHERE nome = ? AND senha = ?''', (novo_saldo, name, senha))
        cursor_contas.execute('''insert into transacao(valor, tipo, dia) values(?, ?, ?)''', (val_to_dep, tipo, data_hora))
        conexão_contas.commit()
        print("Depósito realizado com sucesso.")
        bank(name,senha)
    elif opt ==3:
        tipo = "Retirou"
        data_hora = datetime.now().strftime('%Y-%m-%d')
        val_to_ret = float(input("Quanto você deseja retirar? "))
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo_atual = cursor_contas.fetchone()[0]
        novo_saldo = saldo_atual - val_to_ret
        cursor_contas.execute('''UPDATE contas SET saldo = ? WHERE nome = ? AND senha = ?''', (novo_saldo, name, senha))
        cursor_contas.execute('''insert into transacao(valor, tipo, dia) values(?, ?, ?)''', (val_to_ret, tipo, data_hora))
        conexão_contas.commit()
        print("Transação realizada com sucesso.")
        bank(name,senha)
    elif opt ==4:
        cursor_contas.execute('''SELECT * FROM transacao ''')
        transacoes = cursor_contas.fetchall()
        for i in transacoes:
            print(f"No dia {i[2]}, você {i[1]} {i[0]} Reais")
        while True:
            gout = int(input("SE DESEJAR SAIR PRESSIONE 1: "))
            if gout == 1:
                break
            else:
                pass
        bank(name,senha)
    elif opt ==5:
        header()
        print("Adeus, volte sempre!")
        print("--" * 20)
    else:
        print("\nNúmeros invalidos, escolhe entre 1 e 5!")
        bank(name)

pergunta_reg_ou_log()