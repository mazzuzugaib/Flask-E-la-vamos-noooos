#imports
from flask import Flask, render_template, request
#instanciando o Flask
app = Flask(__name__)

class lista:
    def __init__(self, titulo, artista, genero):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

m1 = lista('Knight of Cydonia', 'Muse', 'Rock')
m2 = lista('Bohemian Rhapsody', 'Queen', 'Rock')
m3 = lista('Stairway to Heaven', 'Led Zeppelin', 'Rock')
lista_musicas = [m1, m2, m3]

@app.route('/')
def inicio():

    return render_template('home.html', lista_musicas = lista_musicas)

#renderiza pagina de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#pega dados do form em cadastro.html.
@app.route('/cadastrar', methods=['POST'])
def cadastro_musica():
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']

    nova_musica = lista(titulo, artista, genero)

    lista_musicas.append(nova_musica)

    return render_template('home.html', lista_musicas = lista_musicas)



if __name__ == '__main__':
    app.run(debug=True)