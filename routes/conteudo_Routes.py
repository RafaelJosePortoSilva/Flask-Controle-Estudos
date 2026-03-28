from flask import Blueprint, request, redirect, url_for
from services.conteudo_Service import Conteudo_Service

conteudo_bp = Blueprint('conteudo', __name__)

@conteudo_bp.route('/conteudo/novo/<int:materia_id>', methods=['POST'])
def novo(materia_id):
    titulo = request.form.get('titulo')
    Conteudo_Service.criar_conteudo(titulo) 
    return redirect(url_for('materia.ver_materia', id=materia_id))

@conteudo_bp.route('/conteudo/remover/<int:id>/<int:materia_id>', methods=['POST'])
def remover(id, materia_id):
    Conteudo_Service.remover_conteudo(id)
    return redirect(url_for('materia.ver_materia', id=materia_id))