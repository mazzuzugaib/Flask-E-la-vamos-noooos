#imports
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#instanciando o Flask
app = Flask(__name__)

app.secret_key = 'satorarepotenetoperarotas'

#configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
      SGBD = 'mysql+mysqlconnector',
      usuario = 'root',
      senha = 'tenet',
      servidor = 'localhost',
      database = 'playmusica'
    )

db = SQLAlchemy(app)

#criando a tabela de músicas
    class Musica(db.Model):
        tb_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        tb_titulo = db.Column(db.String(30), nullable=False)
        tb_artista = db.Column(db.String(30), nullable=False)
        tb_genero = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Name> %r' % self.name

#criando a tabela de usuários
class Usuario(db.Model):
    id_us = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_us = db.Column(db.String(50), nullable=False)
    login_us = db.Column(db.String(10), nullable=False)
    senha_us = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Name> %r' % self.name

#VIEWS---------------------------------------------------------------------------

#pagina inicial
@app.route('/')
def inicio():
    if session.get('usuario_in') is None:
        flash('Faça login para continuar:')
        return redirect(url_for('login'))
    
    lista = Musica.query.order_by(Musica.tb_id)

    return render_template('home.html', lista_musicas = lista, nome_pagina='Home')

#pagina de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', nome_pagina='Cadastro')

#login
@app.route('/login')
def login():
    return render_template('login.html', nome_pagina='Login')


#MODELS----------------------------------------------------------------------------------------------

#pega dados do form em cadastro.html.
@app.route('/cadastrar', methods=['POST'])
def cadastro_musica():
    
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']

    nova_musica = Musica(tb_titulo=titulo, tb_artista=artista, tb_genero=genero)
    db.session.add()
    db.session.commit()

    musicas = Musica.query.order_by(Musica.tb_id)

    return render_template('home.html', lista_musicas = musicas)

#validação de usuário (abrir sessão)
@app.route('/validar', methods=['POST'])
def valide():
    if request.form['user'] == 'lorem' and request.form['senha'] == 'ipsum':
        session['usuario_in'] = 'Lorem'

        flash('Login realizado com sucesso!')
        
        return redirect(url_for('inicio'))
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('login'))

#log out de usuario
@app.route('/sair')
def sair():
    session['usuario_in'] = None

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)