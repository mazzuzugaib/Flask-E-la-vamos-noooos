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
