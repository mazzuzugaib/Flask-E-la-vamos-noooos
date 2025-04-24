from app import db

#criando a tabela de músicas
class Musica(db.Model):
    tb_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tb_titulo = db.Column(db.String(30), nullable=False)
    tb_artista = db.Column(db.String(30), nullable=False)
    tb_genero = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Name> %r' % self.name

#criando a tabela de usuários
class Usuario(db.Model):
    id_us = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_us = db.Column(db.String(50), nullable=False)
    login_us = db.Column(db.String(10), nullable=False)
    senha_us = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Name> %r' % self.name