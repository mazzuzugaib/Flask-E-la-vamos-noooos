from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return('<h1>ola mundo é o caralho</h1>')

app.run()