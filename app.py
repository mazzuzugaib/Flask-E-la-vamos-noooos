#imports
from flask import Flask, render_template
#instanciando o Flask
app = Flask(__name__)

class lista:
    def __init__(self, titulo, artista, genero):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

@app.route('/')
def inicio():
    m1 = lista('Knight of Cydonia', 'Muse', 'Rock')
    m2 = lista('Bohemian Rhapsody', 'Queen', 'Rock')
    m3 = lista('Stairway to Heaven', 'Led Zeppelin', 'Rock')

    return render_template('home.html', lista_musicas = [m1, m2, m3])


if __name__ == '__main__':
    app.run(debug=True)