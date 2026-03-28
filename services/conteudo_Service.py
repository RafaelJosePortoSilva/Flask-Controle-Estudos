from models import db, Conteudo

class Conteudo_Service():
    @staticmethod
    def criar_conteudo(titulo, descricao=None):
        nova = Conteudo(titulo=titulo, descricao=cor)
        db.session.add(nova)
        db.session.commit()
        return nova

    @staticmethod
    def listar_tudo():
        return Conteudo.query.all()

    @staticmethod
    def buscar_por_id(conteudo_id):
        return Conteudo.query.get(conteudo_id)
        
    
    @staticmethod
    def atualizar_conteudo(conteudo_id, novo_titulo=None, nova_descricao=None):
        conteudo = Conteudo.query.get(conteudo_id)
        if conteudo:
            if novo_titulo:
                conteudo.titulo = novo_titulo
            if nova_descricao:
                conteudo.descricao = nova_descricao
            db.session.commit()
        return None
    
    @staticmethod
    def remover_conteudo(conteudo_id):
        conteudo = Conteudo.query.get(conteudo_id)
        if conteudo:
            db.session.delete(conteudo)
            db.session.commit()
            return True

        return False