from flask import Blueprint, render_template, request, redirect, url_for
from services.materia_Service import Materia_Service

materia_bp = Blueprint('materia', __name__)

@materia_bp.route('/')
def index():
    materias = Materia_Service.listar_tudo()
    return render_template('index.html', materias=materias)

@materia_bp.route('/materia/<int:id>')
def ver_materia(id):
    materia = Materia_Service.buscar_por_id(id)
    return render_template('materia.html', materia=materia)

@materia_bp.route('/materia/nova', methods=['POST'])
def nova():
    nome = request.form.get('nome')
    cor = request.form.get('cor', 'primary')
    Materia_Service.criar_materia(nome, cor)
    return redirect(url_for('materia.index'))

@materia_bp.route('/materia/editar/<int:id>', methods=['POST'])
def editar(id):
    nome = request.form.get('nome')
    Materia_Service.atualizar_materia(id, novo_nome=nome)
    return redirect(url_for('materia.index'))

@materia_bp.route('/materia/remover/<int:id>', methods=['POST'])
def remover(id):
    Materia_Service.remover_materia(id)
    return redirect(url_for('materia.index'))