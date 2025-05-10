#import flask
from flask import Flask
#para criar o banco de dados
from flask_sqlalchemy import SQLAlchemy

#instanciando o Flask
app = Flask(__name__)

#chamando o arquivo de configuração config.py
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)