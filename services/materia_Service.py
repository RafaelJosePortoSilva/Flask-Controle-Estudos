from models import db, Materia
from datetime import datetime

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

    @staticmethod
    def buscar_por_id(materia_id):
        return Materia.query.get(materia_id)
        
    
    @staticmethod
    def atualizar_materia(materia_id, novo_nome=None, nova_cor=None):
        materia = Materia.query.get(materia_id)
        if materia:
            if nome:
                materia.nome = novo_nome
            if cor:
                materia.cor = nova_cor
            db.session.commit()
        return None
    
    @staticmethod
    def remover_materia(materia_id):
        materia = Materia.query.get(materia_id)
        if materia:
            db.session.delete(materia)
            db.session.commit()
            return True

        return False