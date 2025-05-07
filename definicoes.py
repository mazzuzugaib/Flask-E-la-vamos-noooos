import os
from app import app

def recupera_imagem(id):
    for imagem in os.listdir(app.config['UPLOAD']):
        nome=str(imagem).split('.')
        if nome[0] == f'album_{id}':
            return imagem
    return 'default.png'