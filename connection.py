from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='D:\Xampp\htdocs\Projeto-Dos-Guri')

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
    # fazendo uma consulta nos módulos
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM table_index")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/bibliotecas.html')
def bibliotecas():
    # fazendo uma consulta nas bibliotecas
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bibliotecas")
    data = cur.fetchall()
    cur.close()
    return render_template('bibliotecas.html', data=data)

@app.route('/about.html')
def about_us():
    # about the devs
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM about_us")
    data = cur.fetchall()
    cur.close()
    return render_template('about.html', data=data)

# rota para lidar com a pesquisa
@app.route('/pesquisa.html', methods=['get'])
def pesquisa():
    # recupera o termo de pesquisa do formulário
    query = request.args.get('query')

    # cria o cursor para executar a consulta
    cur = mysql.connection.cursor()

    # executa a consulta para pesquisar por um termo em cada uma das tabelas
    cur.execute("SELECT * FROM bibliotecas WHERE id LIKE %s OR nome LIKE %s OR descricao LIKE %s", (f'%{query}%', f'%{query}%', f'%{query}%'))
    bibliotecas_results = cur.fetchall()

    cur.close()

    # retorna os resultados da pesquisa
    return render_template('pesquisa.html', query=query, bibliotecas_results=bibliotecas_results)

if __name__ == '__main__':
    app.run(debug=True)