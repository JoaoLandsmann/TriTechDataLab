# importando módulo para conectar com a database
import mysql.connector
# importando uma função do módulo para caso dê erro na conexão
from mysql.connector import errorcode

# tentando a conexão
try:
	db_connection = mysql.connector.connect(
		host="localhost", 
	    user="root", 
	    password="", 
        database="db_site"
	)
	#mensagem de êxito
	print("Database connection made!")

# caso dê erro na conexão
except mysql.connector.Error as error:
	
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:  
	db_connection.close()