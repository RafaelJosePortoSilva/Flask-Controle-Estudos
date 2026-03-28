from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cor = db.Column(db.String(20), default="primary")
    conteudos = db.relationship('Conteudo', backref='materia', cascade="all, delete-orphan")
    tarefas = db.relationship('Tarefa', backref='materia', cascade="all, delete-orphan")

class Conteudo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    tarefas = db.relationship('Tarefa', backref='conteudo')

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    conteudo_id = db.Column(db.Integer, db.ForeignKey('conteudo.id'), nullable=True)

