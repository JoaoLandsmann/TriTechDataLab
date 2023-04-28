from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from sqlalchemy import create_engine
import pandas as pd
import pymysql

app = Flask(__name__, static_folder='')

# inicialização do objeto MySQL
mysql = MySQL(app)

# definição da rota padrão
@app.route('/index.html')
def index():
    # cria o cursor para executar a consulta
    cur = mysql.connection.cursor()

    # executa a consulta para pesquisar por um termo em cada uma das tabelas
    consulta1 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '1'")
    consulta1 = cur.fetchall()

    consulta2 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '9'")
    consulta2 = cur.fetchall()

    consulta3 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '10'")
    consulta3 = cur.fetchall()

    cur.close()

    # retorna os resultados da pesquisa
    return render_template('index.html', consulta1=consulta1, consulta2=consulta2, consulta3=consulta3)

@app.route('/about.html')
def about():
    return render_template('about.html')

# rota para lidar com a barra de pesquisa
@app.route('/teste.html')
def teste():


    engine = create_engine('mysql+pymysql://root@localhost/db_site')
      
    query = f"SELECT * FROM bibliotecas WHERE  LIKE;"
 
    df2 = pd.read_sql(query, engine)
    df2 = pd.DataFrame(df2)
    df2 = df2.head()
    
    return render_template('teste.html', df2=df2, query=query)

if __name__ == '__main__':
    app.run(debug=True)