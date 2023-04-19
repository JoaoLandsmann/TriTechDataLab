import mysql.connector

# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_site"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Conectado ao servidor mySQL versão {db_info}")
    cursor = mydb.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print(f"Conectado ao bando de dados {linha}\n")

    query = "SELECT * FROM modulos"
    cursor.execute(query)
    rows = cursor.fetchall()

    print("Printando conteúdo da tabela modulos")
    print(f"{rows}\n")