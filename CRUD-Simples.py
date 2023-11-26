import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor

# Class connect
class Connect:
    def __init__(self,
    host='localhost',
    user='root',
    password='',
    database='crud2',
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        try:
            self.connect = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Succesful connection")
        except Exception as e:
            print(f"Error{e}")
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("BD doesnt exists")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("The username or password is not valid")
            else:
                print(e)

    def close_connection(self):
        if self.connect:
            self.connect.close()

###############################################################################################################
# Conexão com a base de dados
###############################################################################################################
# Preencher os campos de conexão abaixo
"""
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
"""
# Dropando a base de dados
# cursor.execute("DROP DATABASE Crud2")
# Criando uma base de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS Crud2")
# Selecionando a nossa base
cursor.execute("use Crud2")
# Criando nossa tabela com alguns parâmetros
cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")
###############################################################################################################

###############################################################################################################
# CREATE
###############################################################################################################
def create():
    cursor = db_connection.cursor()
    # Dados de input da variável nome
    Nome = input("Digite o seu nome: ").title()
    # Dados de input da variável cpf
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
        # Dados de input da variável nome
        if choose == '1':
            Nome = input("\nDigite o nome a ser localizado: ").title()
            sql = "SELECT * FROM Pessoas WHERE Nome = '{}'".format(Nome)
            cursor.execute(sql)
            dados_lidos = cursor.fetchall()
            # Validação se a variavel dados_lidos retornar em branco
            if dados_lidos == []:
                print("Erro: Não encontramos {} em nossa base.". format(Nome))
            else:
                print(dados_lidos)
                print("\nDados apresentados com sucesso.")
                break
        
        # Dados de input da variável cpf
        elif choose == '2':
            cpf = input("\nDigite o CPF a ser localizado: ")
            sql = "SELECT * FROM Pessoas WHERE cpf = '{}'".format(cpf)
            cursor.execute(sql)
            dados_lidos = cursor.fetchall()
            # Validação se a variavel dados_lidos retornar em branco
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
    # Apresentando um menu de seleção
    while True:
        print("\n")
        print("="*20)
        print("       MENU")
        print("="*20)
        print("Você deseja atualizar: ")
        print("1 - Nome")
        print("2 - CPF")
        choose = input("\nDigite a opção desejada: ")

        # Dados de input da variável nome
        if choose == '1':
            Nome = input("Digite o nome a ser atualizado: ").title()
            Nome2 = input("Informe o nome corrigido: ").title()
            sql = "UPDATE Pessoas SET Nome = '{}' WHERE Nome = '{}'".format(Nome2, Nome)
            cursor.execute(sql)
            db_connection.commit()
            print("\nDados atualizados com sucesso")
            # Realizando um print da variável para confirmar a atualização
            sql2 = "SELECT * FROM Pessoas WHERE Nome = '{}'".format(Nome2)
            cursor.execute(sql2)
            dados_lidos = cursor.fetchall()
            print(dados_lidos)
            print("\nDados apresentados com sucesso.")
            break
        
        # Dados de input da variável cpf
        elif choose == '2':
            cpf = input("Digite o nome a ser atualizado: ")
            cpf2 = input("Informe o nome corrigido: ")
            sql = "UPDATE Pessoas SET cpf = '{}' WHERE cpf = '{}'".format(cpf2, cpf)
            cursor.execute(sql)
            db_connection.commit()
            print("\nDados atualizados com sucesso")
            # Realizando um print da variável para confirmar a atualização
            sql2 = "SELECT * FROM Pessoas WHERE cpf = '{}'".format(cpf2)
            cursor.execute(sql2)
            dados_lidos = cursor.fetchall()
            print(dados_lidos)
            print("\nDados apresentados com sucesso.")
            break


###############################################################################################################

###############################################################################################################
# Delete
###############################################################################################################
def delete():
    cursor = db_connection.cursor()
    # Apresentando um menu de seleção
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

        # Dados de input da variável nome
        if choose == '1':
            Nome = input("Informe o nome: ").title()
            sql = "DELETE FROM Pessoas WHERE Nome = '{}'".format(str(Nome))
            cursor.execute(sql)
            db_connection.commit()
            print("\nDado excluído com sucesso! Apresentando a base de dados: ")
            # Realizando um print da variável para confirmar a deleção
            sql2 = "SELECT * FROM Pessoas"
            cursor.execute(sql2)
            dados_lidos = cursor.fetchall()
            for cadastro in (dados_lidos):
                print(cadastro)
            print("\nDados apresentados com sucesso.")
            break
        
        # Dados de input da variável cpf
        elif choose == '2':
            cpf = input("Informe o cpf: ")
            sql = "DELETE FROM Pessoas WHERE cpf = '{}'".format(cpf)
            cursor.execute(sql)
            db_connection.commit()
            print("\nDado excluído com sucesso! Apresentando a base de dados: ")
            # Realizando um print da variável para confirmar a deleção
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
print("="*25)
print("  CRUD - SIMPLIFICADO")
print("="*25)
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