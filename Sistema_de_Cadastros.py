import mysql.connector
from pacotes import estilo
import os

from pacotes import estilo
try:
    db = mysql.connector.connect(
    host="127.0.0.1",
    user= "root",
    password ="",
    database = "cadastro_de_pessoas"
    )
    cursor = db.cursor()
    print("Conexão realiza com o banco de dados!!")
except:
    print("Conexão não realiza com o banco de dados!!")
    #return cursor , db
    
def inserir_dados(database,cursor,nome,telefone,idade): #Precisamos de um banco de dados e um cursor inicializado.
    cursor.execute(f"insert into pessoas(nome,idade,telefone)values ('{nome}',{idade},{telefone});")
    database.commit()

def visualizar_dados(cursor):
    print("\n")
    cursor.execute(f"select concat('Nome: ',nome, '.   Idade: ', idade) as descricao from pessoas;")
    resultado = cursor.fetchall()
    estilo.estilo()
    for x in resultado:
        print(x)
    estilo.estilo()

print("Bem vindo ao sistema!")
while True:
    os.system("cls")
    print("\nOpções: ")
    print("[1] - Cadastrar pessoas")
    print("[2] - Ver pessoas cadastradas")
    print("[3] - Sair do sistema")
    op = int(input("\nDigite sua opção: "))
    if op == 1:
        nome = str(input("\nDigite seu nome: "))
        telefone = int(input("Digite seu telefone: "))
        idade = int(input("Digite sua idade: "))
        inserir_dados(db,cursor,nome,telefone,idade)
    elif op == 2:
        visualizar_dados(cursor)
        input("Aperter enter para continuar.")
    elif op == 3:
        break
    else:
        print("Digite uma opção válida")    