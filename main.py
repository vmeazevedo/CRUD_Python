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
