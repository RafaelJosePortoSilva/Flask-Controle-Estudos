from models import db, Tarefa

class Tarefa_Service():
    @staticmethod
    def criar_tarefa(descricao, concluida=False):
        nova = Tarefa(descricao=descricao, concluida=concluida)
        db.session.add(nova)
        db.session.commit()
        return nova

    @staticmethod
    def listar_tudo():
        return Tarefa.query.all()

    @staticmethod
    def buscar_por_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)
        
    
    @staticmethod
    def atualizar_tarefa(tarefa_id, nova_descricao=None, novo_status=None):
        tarefa = Tarefa.query.get(tarefa_id)
        if tarefa:
            if nova_descricao:
                tarefa.descricao = nova_descricao
            if novo_status:
                tarefa.concluida = novo_status
            db.session.commit()
        return None
    
    @staticmethod
    def remover_tarefa(tarefa_id):
        tarefa = Tarefa.query.get(tarefa_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
            return True

        return False