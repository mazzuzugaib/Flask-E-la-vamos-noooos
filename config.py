import os

SECRET_KEY = 'satorarepotenetoperarotas'

#configurando o banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
      SGBD = 'mysql+mysqlconnector',
      usuario = 'root',
      senha = 'tenet',
      servidor = 'localhost',
      database = 'playmusica'
    )

#constante ULPOAD pega o diretorio onde as imagens serão salvas. os.path.abspath(__file__)) indica que
# o arquivo está no mesmo diretório do arquivo config.py, ou seja, na pasta app, + a pasta uploads
UPLOAD = os.path.dirname(os.path.abspath(__file__)) + '/uploads'