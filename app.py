#imports
from flask import Flask, render_template, request, session
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



#VIEWS---------------------------------------------------------------------------

#pagina inicial
@app.route('/')
def inicio():

    return render_template('home.html', lista_musicas = lista_musicas)

#pagina de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#login
@app.route('/login')
def login():
    return render_template('login.html')


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

#validação de usuário
@app.route('/validar', methods=['POST'])
def valide():
    if request.form['user'] == 'lorem' and request.form['senha'] == 'ipsum':
        session['usuario_in'] = request.form['user']
        return render_template('home.html', lista_musicas = lista_musicas)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)