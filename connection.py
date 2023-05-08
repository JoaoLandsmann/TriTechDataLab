from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='')

# configuração do mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_site'

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

    consulta2 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '3'")
    consulta2 = cur.fetchall()

    consulta3 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '4'")
    consulta3 = cur.fetchall()

    cur.close()

    # retorna os resultados da pesquisa
    return render_template('index.html', consulta1=consulta1, consulta2=consulta2, consulta3=consulta3)

@app.route('/about.html')
def about():
    return render_template('about.html')

# rota para lidar com a barra de pesquisa
@app.route('/biblioteca.html')
def biblioteca():
    # recupera o termo de pesquisa do formulário
    query = request.args.get('query')

    # cria o cursor para executar a consulta
    cur = mysql.connection.cursor()
   
    apresentacoes = []
    apresenta1 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '1'")
    apresenta1 = cur.fetchall()
    apresentacoes.append(apresenta1)

    apresenta2 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '2'")
    apresenta2 = cur.fetchall()

    apresenta3 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '3'")
    apresenta3 = cur.fetchall()
    
    apresenta4 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '4'")
    apresenta4 = cur.fetchall()

    apresenta5 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '5'")
    apresenta5 = cur.fetchall()

    apresenta6 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '6'")
    apresenta6 = cur.fetchall()
    
    apresenta7 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '7'")
    apresenta7 = cur.fetchall()

    apresenta8 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '8'")
    apresenta8 = cur.fetchall()

    apresenta9 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '9'")
    apresenta9 = cur.fetchall()
    
    apresenta10 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '10'")
    apresenta10 = cur.fetchall()

    apresenta11 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '11'")
    apresenta11 = cur.fetchall()

    apresenta12 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '12'")
    apresenta12 = cur.fetchall()
    
    apresenta13 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '13'")
    apresenta13 = cur.fetchall()

    apresenta14 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '14'")
    apresenta14 = cur.fetchall()

    apresenta15 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '15'")
    apresenta15 = cur.fetchall()
    
    apresenta16 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '16'")
    apresenta16 = cur.fetchall()

    apresenta17 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '17'")
    apresenta17 = cur.fetchall()

    apresenta18 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '18'")
    apresenta18 = cur.fetchall()
    
    apresenta19 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '19'")
    apresenta19 = cur.fetchall()

    apresenta20 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '20'")
    apresenta20 = cur.fetchall()

    apresenta21 = cur.execute("SELECT * FROM bibliotecas WHERE id LIKE '21'")
    apresenta21 = cur.fetchall()
    
    cur.close()

    # retorna os resultados da pesquisa
    return render_template('biblioteca.html', 
                           query=query, 
                           apresenta1=apresenta1,
                           apresenta2=apresenta2,
                           apresenta3=apresenta3,
                           apresenta4=apresenta4,
                           apresenta5=apresenta5,
                           apresenta6=apresenta6,
                           apresenta7=apresenta7,
                           apresenta8=apresenta8,
                           apresenta9=apresenta9,
                           apresenta10=apresenta10,
                           apresenta11=apresenta11,
                           apresenta12=apresenta12,
                           apresenta13=apresenta13,
                           apresenta14=apresenta14,
                           apresenta15=apresenta15,
                           apresenta16=apresenta16,
                           apresenta17=apresenta17,
                           apresenta18=apresenta18,
                           apresenta19=apresenta19,
                           apresenta20=apresenta20,
                           apresenta21=apresenta21
                            )


if __name__ == '__main__':
    app.run(debug=True)