from flask import render_template, request, session, url_for, redirect, flash, send_from_directory
from models import Musica, Usuario
from app import app, db
from definicoes import recupera_imagem, deleta_imagem, FormularioMusica
import time


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
    form = FormularioMusica()
    return render_template('cadastro.html', nome_pagina='Cadastro', form=form)

#login
@app.route('/login')
def login():
    return render_template('login.html', nome_pagina='Login')

#editar musica
@app.route('/editar/<int:id>')
def editar(id):
    if session.get('usuario_in') is None or 'usuario_in' not in session:
        flash(f'Faça login para continuar ou <a href="{url_for("novo")}">cadastre-se</a>', 'html')
        return redirect(url_for('login'))
    
    musica=Musica.query.filter_by(tb_id=id).first()

    form = FormularioMusica()
    form.titulo.data = musica.tb_titulo
    form.artista.data = musica.tb_artista
    form.genero.data = musica.tb_genero

    album = recupera_imagem(id)

    return render_template('editar.html',
                           nome_pagina='Editar Música',
                           musica=form,
                           imagem_musica=album, id=id)

#excluir musica
@app.route('/excluir/<int:id_excluir>')
def excluir(id_excluir):
    Musica.query.filter_by(tb_id=id_excluir).delete()
    deleta_imagem(id_excluir)
    db.session.commit()
    flash('Música excluída.')
    return redirect(url_for('inicio'))


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
    formulario = FormularioMusica(request.form)
    # para validar o formulario:
    if not formulario.validate_on_submit():
        return redirect(url_for('cadastro'))
    
    titulo = formulario.titulo.data
    artista = formulario.artista.data
    genero = formulario.genero.data
    arquivo = request.files['arquivo']

    musica = Musica.query.filter_by(tb_titulo=titulo).first()
    cantor = Musica.query.filter_by(tb_artista=artista).first()
    pasta = app.config['UPLOAD']
    #no curso, ele limita apenas pela musica, mas isso é uma tolice porque pode haver músicas com o mesmo nome
    #de artistas diferentes, então eu fiz a validação também pelo artista.
    if musica and cantor:
        flash('Essa música já está cadastrada!')
        return redirect(url_for('inicio'))
    
    nova_musica = Musica(tb_titulo=titulo, tb_artista=artista, tb_genero=genero)
    #a linha abaixo esta salvando a imagem na pasta, com o nome de 'album_' e o id da música, ex. album_1.jpg
    db.session.add(nova_musica)
    db.session.commit()

    nome_arquivo = arquivo.filename.split('.') #pega o nome do arquivo, ex. album.jpg e separa no ponto('.'), ficando ['album', 'jpg']
    extensao = nome_arquivo[len(nome_arquivo)-1]#pega o último elemento da lista(o -1 ), ou seja a extensao ex. 'jpg'
    momento = time.time() #para resolver o problema de cash ao salvar a imagem. Para a imagem salva nao precisar de f5 para aparecer
    nome_completo = f'album_{nova_musica.tb_id}_{momento}.{extensao}'
    arquivo.save(f'{pasta}/{nome_completo}')# salva o arquivo na pasta uploads com o nome completo, ex. album_1.jpg

    musicas = Musica.query.order_by(Musica.tb_id).all()

    return render_template('home.html', lista_musicas=musicas)

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
#Passar os dados da rota editar para atualizar a música
@app.route('/atualizar', methods=['POST'])
def atualizar(): 
    #tratativa de informações do formulario
    form = FormularioMusica(request.form) 
    if form.validate_on_submit:
        musica = Musica.query.filter_by(tb_id=request.form['id_form_atualizar']).first()
        musica.tb_titulo = form.titulo.data
        musica.tb_artista = form.artista.data
        musica.tb_genero = form.genero.data
        db.session.add(musica)
        db.session.commit()
        #tratativa da imagem
        if arquivo:
            arquivo = request.files['arquivo_form_atualizar']
            pasta = app.config['UPLOAD']
            nome_arquivo = arquivo.filename.split('.')
            extensao = nome_arquivo[len(nome_arquivo)-1]
            momento = time.time()
            nome_completo = f'album_{musica.tb_id}_{momento}.{extensao}'
            deleta_imagem(musica.tb_id)
            arquivo.save(f'{pasta}/{nome_completo}')

        flash('Música atualizada com sucesso!')
        return redirect(url_for('inicio'))
#log out de usuario
@app.route('/sair')
def sair():
    session['usuario_in'] = None

    return redirect(url_for('login'))

@app.route('/uploads/<nome_imagem>')
def imagem(nome_imagem):
    return send_from_directory('uploads', nome_imagem)