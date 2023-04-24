from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='D:\Xampp\htdocs\Projeto-Dos-Guri\templates')

# configuração do mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_site'

# inicialização do objeto MySQL
mysql = MySQL(app)


# definição da rota padrão
@app.route('/index.php')
def index():
    # fazendo uma consulta nos módulos
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM table_index")
    data = cur.fetchall()
    cur.close()
    return render_template('index.php', data=data)

@app.route('/modulos.php')
def modulos():
    # fazendo uma consulta nos módulos
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM modulos")
    data = cur.fetchall()
    cur.close()
    return render_template('modulos.php', data=data)

@app.route('/bibliotecas.php')
def bibliotecas():
    # fazendo uma consulta nos módulos
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bibliotecas")
    data = cur.fetchall()
    cur.close()
    return render_template('bibliotecas.php', data=data)

@app.route('/about.php')
def about_us():
    # fazendo uma consulta nos módulos
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM about_us")
    data = cur.fetchall()
    cur.close()
    return render_template('about.php', data=data)

if __name__ == '__main__':
    app.run(debug=True)