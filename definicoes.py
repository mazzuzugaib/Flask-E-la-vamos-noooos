#para interagir com o sistema operacional e pegar as imagens:
import os
#arquivo app que é ondeo Flask é instanciado:
from app import app
#para validação de usuario:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField

#classe para validar formulario
class FormularioMusica(FlaskForm):
    titulo = StringField('Título da Música', [validators.DataRequired(), validators.length(min=2, max=30)])
    artista = StringField('Artista', [validators.DataRequired(), validators.length(min=2, max=30)])
    genero = StringField('Gênero', [validators.DataRequired(), validators.length(min=2, max=30)])
    cadastrar = SubmitField('Cadastrar')

class FormularioUser(FlaskForm):
    login_wtf = StringField('Login', [validators.DataRequired(), validators.length(min=2, max=10)])
    senha_wtf = PasswordField('Senha', [validators.DataRequired(), validators.length(min=2, max=10)])
    entrar_wtf = SubmitField('Entrar')


def recupera_imagem(id):
    for imagem in os.listdir(app.config['UPLOAD']):
        nome=str(imagem).split('.')
        if f'album_{id}_' in nome[0]:
            return imagem
    return 'default.png'

def deleta_imagem(id):
   imagem = recupera_imagem(id)
   if imagem != 'default.png':
      os.remove(os.path.join(app.config['UPLOAD'], recupera_imagem(id)))