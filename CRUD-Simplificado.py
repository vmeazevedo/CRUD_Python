import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor

###############################################################################################################
# Conexão com a base de dados
###############################################################################################################
# Preencher os campos de conexão abaixo
host = 'localhost'           
user = 'root'                
password = ''                

# Tentando se conectar a base de dados MySQL
try:
	db_connection = mysql.connector.connect(host = host, user = user, password = password)
	print("\nConexão com a base de dados realizada!\n")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("\nA base de dados não existe.")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("\nUsername ou o password está errado.")
	else:
		print(error)

cursor = db_connection.cursor()
# Criando a database e a tabela
# cursor.execute("DROP DATABASE Formulario")
cursor.execute("CREATE DATABASE IF NOT EXISTS Crud2")
cursor.execute("use Crud2")
cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")
###############################################################################################################

###############################################################################################################
# CREATE
###############################################################################################################
def create():
    cursor = db_connection.cursor()
    # Validando os dados de input do Nome
    Nome = input("Digite o seu nome: ").title()
    # Validando os dados de input do CPF
    cpf = input("Digite o seu CPF: ")
    #Realizando a inserção dos dados em nosso banco de dados
    sql = "INSERT INTO Pessoas (Nome, CPF) VALUES ('{}','{}')".format(Nome, cpf)
    cursor.execute(sql)
    db_connection.commit()
    print("\nDados inseridos com sucesso")
###############################################################################################################

###############################################################################################################
# READ
###############################################################################################################
def read():
    cursor = db_connection.cursor()
    # Apresentando um menu de seleção
    while True:
        print("\n")
        print("="*20)
        print("       MENU")
        print("="*20)
        print("Você deseja consultar: ")
        print("1 - Nome")
        print("2 - CPF")
        print("3 - A base toda")
        choose = input("\nDigite a opção desejada: ")
        # Validando os dados de input do Nome
        if choose == '1':
            Nome = input("\nDigite o nome a ser localizado: ").title()
            sql = "SELECT * FROM Pessoas WHERE Nome = '{}'".format(Nome)
            cursor.execute(sql)
            dados_lidos = cursor.fetchall()
            if dados_lidos == []:
                print("Erro: Não encontramos {} em nossa base.". format(Nome))
            else:
                print(dados_lidos)
                print("\nDados apresentados com sucesso.")
                break
        
        # Validando os dados de input do CPF
        elif choose == '2':
            cpf = input("\nDigite o CPF a ser localizado: ")
            sql = "SELECT * FROM Pessoas WHERE cpf = '{}'".format(cpf)
            cursor.execute(sql)
            dados_lidos = cursor.fetchall()
            if dados_lidos == []:
                print("Erro: Não encontramos {} em nossa base.". format(cpf))
            else:
                print(dados_lidos)
                print("\nDados apresentados com sucesso.")
                break

            # Apresentando os dados de toda a base
        elif choose == '3':
            sql = "SELECT * FROM Pessoas"
            cursor.execute(sql)
            dados_lidos = cursor.fetchall()
            for cadastro in (dados_lidos):
                print(cadastro)
            print("\nDados apresentados com sucesso.")    
                
        break

###############################################################################################################

###############################################################################################################
# Update
###############################################################################################################
def update():
    cursor = db_connection.cursor()
    


###############################################################################################################

###############################################################################################################
# Delete
###############################################################################################################
def delete():
    cursor = db_connection.cursor()
    while True:
        print("\n")
        print("="*20)
        print("       MENU")
        print("="*20)
        print("Você deseja deletar: ")
        print("1 - Nome")
        print("2 - CPF")
        print("3 - A base toda")
        choose = input("\nDigite a opção desejada: ")
        
        if choose == '1':
            Nome = input("Informe o nome: ").title()
            sql = "DELETE FROM Pessoas WHERE Nome = '{}'".format(str(Nome))
            cursor.execute(sql)
            db_connection.commit()
            print("\nDado excluído com sucesso! Apresentando a base de dados: ")
            sql2 = "SELECT * FROM Pessoas"
            cursor.execute(sql2)
            dados_lidos = cursor.fetchall()
            for cadastro in (dados_lidos):
                print(cadastro)
            print("\nDados apresentados com sucesso.")
            break
        
        elif choose == '2':
            cpf = input("Informe o cpf: ")
            sql = "DELETE FROM Pessoas WHERE cpf = '{}'".format(cpf)
            cursor.execute(sql)
            db_connection.commit()
            print("\nDado excluído com sucesso! Apresentando a base de dados: ")
            sql2 = "SELECT * FROM Pessoas"
            cursor.execute(sql2)
            dados_lidos = cursor.fetchall()
            for cadastro in (dados_lidos):
                print(cadastro)
            print("\nDados apresentados com sucesso.")
            break
        
        elif choose == '3':
            sql = "DELETE FROM Pessoas"
            cursor.execute(sql)
            db_connection.commit()
            print("\nA base foi excluída com sucesso!")
            break
        break
###############################################################################################################

print("\n")
print("="*20)
print("  MENU PRINCIPAL")
print("="*20)
print("1 - Create")
print("2 - Read")
print("3 - Update")
print("3 - Delete")
choose2 = input("\nSelecione uma das opções: ")
if choose2 == '1':
    create()
elif choose2 == '2':
    read()
elif choose2 == '3':
    update()
elif choose2 == '4':
    delete()
