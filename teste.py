from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# estabelece a conexão com o banco de dados
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
    
# cria um cursor para executar consultas SQL
mycursor = mydb.cursor()

# define uma rota para exibir os dados do banco de dados
@app.route('/')
def exibir_dados():
    # executa uma consulta SQL
    mycursor.execute("SELECT * FROM modulos")

    # pega o resultado da consulta
    resultado = mycursor.fetchall()

    # integra o resultado com o HTML usando um template
    return render_template('index.php', dados=resultado)

if __name__ == '__main__':
    app.run(debug=True)