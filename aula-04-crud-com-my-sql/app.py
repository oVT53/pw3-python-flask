# Importando o Flask
from flask import Flask, render_template
import pymysql.cursors
# Importando as rotas que estão nos controllers
from controllers import routes

# Importando o PyMySQL
import pymysql

# Importando o Model
from models.database import db

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Define o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
# Chamando as rotas
routes.init_app(app)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    # Conectando ao MySQL e criando o banco de dados com suas tabelas
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.
                                 cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Executando a Query para criar o banco
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados está criado!")
    except Exception as error:
        print(f"Erro ao criar o banco: {error}")
    finally:
        connection.close()
    
    # Criando as tabelas:
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()

    # Rodando o projeto:
    app.run(host='localhost', port=5000, debug=True)
