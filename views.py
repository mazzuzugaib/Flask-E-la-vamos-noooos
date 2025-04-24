from flask import render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from models import Musica, Usuario
from app import app, db

#pagina inicial
@app.route('/')
def inicio():
    if session.get('usuario_in') is None or 'usuario_in' not in session:
        flash(f'Faça login para continuar ou <a href="{url_for("novo")}">cadastre-se</a>', 'html')

        return redirect(url_for('login'))
    
    lista = Musica.query.order_by(Musica.tb_id)

    return render_template('home.html', lista_musicas = lista, nome_pagina='Home')

#pagina de cadastro de usuario
@app.route('/novo')
def novo():
    return render_template('novo.html', nome_pagina='Novo Usuário')

#pagina de cadastro de musica
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', nome_pagina='Cadastro')

#login
@app.route('/login')
def login():
    return render_template('login.html', nome_pagina='Login')

# RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS ------ RETORNOS
#pega dados do form em cadastro.html.
@app.route('/criar_usuario', methods=['POST'])
def criar_usuario():
    nome = request.form['nome']
    login = request.form['login']
    senha = request.form['senha']

    usuario = Usuario.query.filter_by(login_us=login).first()
    if usuario:
        flash('Esse usuário já existe!')
        return redirect(url_for('novo'))

    novo_usuario = Usuario(nome_us=nome, login_us=login, senha_us=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Usuário cadastrado com sucesso!')
    
    return redirect(url_for('login'))

@app.route('/cadastrar', methods=['POST'])
def cadastro_musica():
    
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']

    musica = Musica.query.filter_by(tb_titulo=titulo).first()
    cantor = Musica.query.filter_by(tb_artista=artista).first()
    #no curso, ele limita apenas pela musica, mas isso é uma tolice porque pode haver músicas com o mesmo nome
    #de artistas diferentes, então eu fiz a validação também pelo artista.
    if musica and cantor:
        flash('Essa música já está cadastrada!')
        return redirect(url_for('inicio'))

    nova_musica = Musica(tb_titulo=titulo, tb_artista=artista, tb_genero=genero)
    db.session.add(nova_musica)
    db.session.commit()

    musicas = Musica.query.order_by(Musica.tb_id)

    return render_template('home.html', lista_musicas = musicas)

#validação de usuário (abrir sessão)
@app.route('/validar', methods=['POST'])
def valide():
    user = Usuario.query.filter_by(login_us=request.form['user']).first()
    senha = Usuario.query.filter_by(senha_us=request.form['senha']).first()
    if user and senha:
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