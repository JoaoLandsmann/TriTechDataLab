from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='D:\Xampp\htdocs\Projeto-Dos-Guri/templates')

# configuração do mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_site'

# inicialização do objeto MySQL
mysql = MySQL(app)

# definição da rota padrão
@app.route('/')
def index():
    # conexão com o banco de dados
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM modulos")
    data = cur.fetchall()
    cur.close()
    return render_template('index.php', data=data)

if __name__ == '__main__':
    app.run(debug=True)