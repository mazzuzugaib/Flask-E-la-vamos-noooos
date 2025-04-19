#imports
from flask import Flask, render_template, request, session, url_for, redirect, flash
#instanciando o Flask
app = Flask(__name__)

app.secret_key = 'satorarepotenetoperarotas'

class lista:
    def __init__(self, titulo, artista, genero):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

m1 = lista('Knight of Cydonia', 'Muse', 'Rock')
m2 = lista('Bohemian Rhapsody', 'Queen', 'Rock')
m3 = lista('Stairway to Heaven', 'Led Zeppelin', 'Rock')
lista_musicas = [m1, m2, m3]

class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

u1 = Usuario('Lorem Ipsum', 'lorem', 'ipsum')



#VIEWS---------------------------------------------------------------------------

#pagina inicial
@app.route('/')
def inicio():
    if session.get('usuario_in') is None:
        flash('Faça login para continuar:')
        return redirect(url_for('login'))
    return render_template('home.html', lista_musicas = lista_musicas, nome_página='Home')

#pagina de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', nome_pagina='Cadastro')

#login
@app.route('/login')
def login():
    return render_template('login.html', nome_pagina='Login')


#ROTAS----------------------------------------------------------------------------------------------

#pega dados do form em cadastro.html.
@app.route('/cadastrar', methods=['POST'])
def cadastro_musica():
    
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']

    nova_musica = lista(titulo, artista, genero)

    lista_musicas.append(nova_musica)

    return render_template('home.html', lista_musicas = lista_musicas)

#validação de usuário (abrir sessão)
@app.route('/validar', methods=['POST'])
def valide():
    if request.form['user'] == u1.login and request.form['senha'] == u1.senha:
        session['usuario_in'] = u1.nome

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