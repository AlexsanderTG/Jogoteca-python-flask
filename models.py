from jogoteca import db


# Definindo a classe Jogo
class Jogos(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<name %r>' % self.nome

# Definindo a classe Usuarios
class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    Senha = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<name %r>' % self.nome