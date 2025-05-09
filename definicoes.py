import os
from app import app

def recupera_imagem(id):
    for imagem in os.listdir(app.config['UPLOAD']):
        nome=str(imagem).split('.')
        if f'album_{id}_' in nome[0]:
            return imagem
    return 'default.png'