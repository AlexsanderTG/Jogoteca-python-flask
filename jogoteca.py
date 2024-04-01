from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Configuração do aplicativo Flask
app = Flask(__name__)
# Configuração da chave secreta para sessões
app.config['SECRET_KEY'] = 'Zhiend'
# Configuração do banco de dados SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/jogoteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py', "rb")

db = SQLAlchemy(app)
from views import *

# Executando o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
