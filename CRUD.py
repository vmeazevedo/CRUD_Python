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
cursor.execute("CREATE DATABASE IF NOT EXISTS Crud")
cursor.execute("use Crud")
cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")
###############################################################################################################

###############################################################################################################
# CREATE
###############################################################################################################
def create():
    cursor = db_connection.cursor()
    # Validando os dados de input do Nome
    while True:
        Nome = input("Digite o seu nome: ").title()
        try:
            Nome = str(Nome)
            if Nome.isdigit():
                print("Por favor insira um nome válido.")
            elif Nome.isspace():
                print("Por favor insira um nome válido.")
            else :
                break
        except:
            print("Por favor, utilize apenas letras.")
    # Validando os dados de input do CPF
    while True:
        cpf = input("Digite o seu CPF: ")
        try:
            cpf = int(cpf)
            if cpf < 0:
                print("O número não pode ser negativo")
            elif len(str(cpf)) < 11:
                print("Você digitou números a menos em seu CPF")
            else:
                break
        except:
            print("Por favor insira um CPF válido.")

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
        try:
            choose = int(choose)
            # Validando os dados de input do choose
            if choose < 0:
                print("Por favor digite uma opção válida!")
            elif choose > 3:
                print("Por favor digite uma opção válida!")
            elif choose == 0:
                print("Por favor digite uma opção válida!")
            # Validando os dados de input do Nome
            elif choose == 1:
                while True:
                    Nome = input("\nDigite o nome a ser localizado: ").title()
                    try:
                        Nome = str(Nome)
                        if Nome.isdigit():
                            print("Por favor insira um nome válido.")
                        elif Nome.isspace():
                            print("Por favor insira um nome válido.")
                        else :
                            break
                    except:
                        print("Por favor, utilize apenas letras.")
                        break
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
            elif choose == 2:
                while True:
                    cpf = input("\nDigite o CPF a ser localizado: ")
                    try:
                        cpf = int(cpf)
                        if cpf < 0:
                            print("O número não pode ser negativo")
                        elif len(str(cpf)) < 11:
                            print("Você digitou números a menos em seu CPF")
                        else :
                            break
                    except:
                        print("Por favor, utilize apenas números.")
                        
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
            elif choose == 3:
                sql = "SELECT * FROM Pessoas "
                cursor.execute(sql)
                dados_lidos = cursor.fetchall()
                for cadastro in (dados_lidos):
                    print(cadastro)
                print("\nDados apresentados com sucesso.")
                break

        except:
            print("Por favor utilize apenas números.")
            

###############################################################################################################


print("\n")
print("="*20)
print("  MENU PRINCIPAL")
print("="*20)
print("1 - Create")
print("2 - Read")
print("3 - Update")
print("3 - Delete")
choose2 = input("\nSelecione uma das opções:")
if choose2 == 1:
    create()
elif choose2 == 2:
    read()

