from flask import Blueprint, request, redirect, url_for
from services.tarefa_Service import Tarefa_Service

tarefa_bp = Blueprint('tarefa', __name__)

@tarefa_bp.route('/tarefa/nova/<int:materia_id>', methods=['POST'])
def nova(materia_id):
    descricao = request.form.get('descricao')
    Tarefa_Service.criar_tarefa(descricao)
    return redirect(url_for('materia.ver_materia', id=materia_id))

@tarefa_bp.route('/tarefa/check/<int:id>/<int:materia_id>')
def check(id, materia_id):
    tarefa = Tarefa_Service.buscar_por_id(id)
    if tarefa:
        novo_status = not tarefa.concluida
        Tarefa_Service.atualizar_tarefa(id, novo_status=novo_status)
    return redirect(url_for('materia.ver_materia', id=materia_id))

@tarefa_bp.route('/tarefa/remover/<int:id>/<int:materia_id>', methods=['POST'])
def remover(id, materia_id):
    Tarefa_Service.remover_tarefa(id)
    return redirect(url_for('materia.ver_materia', id=materia_id))