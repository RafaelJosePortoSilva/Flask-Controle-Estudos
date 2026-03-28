from models import db, Materia

class Materia_Service():
    @staticmethod
    def criar_materia(nome, cor="primary"):
        nova = Materia(nome=nome, cor=cor)
        db.session.add(nova)
        db.session.commit()
        return nova

    @staticmethod
    def listar_tudo():
        return Materia.query.all()