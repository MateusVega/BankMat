import sqlite3
import uuid
from datetime import datetime
import os
from time import sleep

conexão_contas = sqlite3.connect('contas.db')
cursor_contas = conexão_contas.cursor()
#cursor_contas.execute('''create table contas(nome text, senha text, account text, saldo real)''')
#cursor_contas.execute('''create table transacao(nome, senha, valor real, tipo text, dia text)''')
def pergunta_reg_ou_log():
    header()
    try:
        rl = int(input("Do you want to register[1], log in[2], or exit[3]? "))
        if rl == 1:
            registrar()
        elif rl == 2:
            logar()
        elif rl == 3:
            header()
            print("Goodbye, come back soon!")
            print("--" * 20)
        else:
            print("\nInvalid numbers, choose between 1 and 3!")
            pergunta_reg_ou_log()
    except ValueError as VE:
        print("\nWrite only numbers")
        pergunta_reg_ou_log()
def header():
    os.system('cls')
    print("="* 52)
    print("                    MATEUS BANK")
    print("="* 52)
    print("\n")
def registrar():
    header()
    nome = input("Enter your new name here: ")
    senha = input("Enter your new password here: ")
    account = str(uuid.uuid4())
    saldo = 0.00
    cursor_contas.execute('''SELECT nome FROM contas''')
    nom = cursor_contas.fetchone()
    if nom != None:
        if nome != str(nom).strip("(),'"):
            cursor_contas.execute('''insert into contas(nome, senha, account, saldo) values(?, ?, ?, ?)''', (nome, senha, account, saldo))
            conexão_contas.commit()
            cursor_contas.execute('''select * from contas''')
            result = cursor_contas.fetchall()
            print("Registration successful!")
            sleep(3)
            pergunta_reg_ou_log()
        else:
            print("Name already in use!")
            sleep(3)
            pergunta_reg_ou_log()
    else:
        cursor_contas.execute('''insert into contas(nome, senha, account, saldo) values(?, ?, ?, ?)''', (nome, senha, account, saldo))
        conexão_contas.commit()
        cursor_contas.execute('''select * from contas''')
        result = cursor_contas.fetchall()
        print("Registration successful!")
        sleep(3)
        pergunta_reg_ou_log()
def logar():
    header()
    nome = input("Enter your name: ")
    senha = input("Enter your password: ")
    cursor_contas.execute('''SELECT * FROM contas WHERE nome = ? AND senha = ?''', (nome,senha))
    result = cursor_contas.fetchone()
    if result:
        print(f"The name '{nome}' and the password '{senha}' are in our database.")
        sleep(3)
        bank(nome,senha)

    else:
        print(f"The name '{nome}' and/or the password '{senha}' are not in our database.")
        sleep(3)
        pergunta_reg_ou_log()
def bank(name,senha):
    sleep(2)
    header()
    opt = int(input(f"Hello {name}, what would you like to do? \n\t[1]CHECK BALANCE\n\t[2]DEPOSIT BALANCE\n\t[3]WITHDRAW BALANCE\n\t[4]CHECK STATEMENT\n\t[5]EXIT\n"))
    if opt == 1:
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo = cursor_contas.fetchone()[0]
        print(f"Hello {name}, your current balance is {saldo}")
        bank(name,senha)
    elif opt ==2:
        tipo = "Deposited"
        data_hora = datetime.now().strftime('%Y-%m-%d')
        val_to_dep = float(input("How much would you like to deposit? "))
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo_atual = cursor_contas.fetchone()[0]
        novo_saldo = saldo_atual + val_to_dep
        cursor_contas.execute('''UPDATE contas SET saldo = ? WHERE nome = ? AND senha = ?''', (novo_saldo, name, senha))
        cursor_contas.execute('''INSERT INTO transacao(nome, senha, valor, tipo, dia) VALUES(?, ?, ?, ?, ?)''', (name, senha, val_to_dep, tipo, data_hora))
        conexão_contas.commit()
        print("Deposit successful.")
        bank(name,senha)
    elif opt ==3:
        tipo = "Withdrew"
        data_hora = datetime.now().strftime('%Y-%m-%d')
        val_to_ret = float(input("How much would you like to withdraw? "))
        cursor_contas.execute('''SELECT saldo FROM contas WHERE nome = ? AND senha = ?''', (name, senha))
        saldo_atual = cursor_contas.fetchone()[0]
        novo_saldo = saldo_atual - val_to_ret
        cursor_contas.execute('''UPDATE contas SET saldo = ? WHERE nome = ? AND senha = ?''', (novo_saldo, name, senha))
        cursor_contas.execute('''INSERT INTO transacao(nome, senha, valor, tipo, dia) VALUES(?, ?, ?, ?, ?)''', (name, senha, val_to_ret, tipo, data_hora))
        conexão_contas.commit()
        print("Transaction successful.")
        bank(name,senha)
    elif opt ==4:
        cursor_contas.execute('''SELECT * FROM transacao WHERE nome = ? AND senha = ?''', (name, senha))
        transacoes = cursor_contas.fetchall()
        for i in transacoes:
            print(f"On {i[4]}, you {i[3]} {i[2]} Dollars")
        while True:
            gout = int(input("PRESS 1 TO QUIT: "))
            if gout == 1:
                break
            else:
                pass
        bank(name,senha)
    elif opt ==5:
        header()
        print("Goodbye, come back soon!")
        print("--" * 20)
    else:
        print("\nInvalid numbers, choose between 1 and 5!")
        bank(name)

pergunta_reg_ou_log()