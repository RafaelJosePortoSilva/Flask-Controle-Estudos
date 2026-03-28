from flask import Blueprint, render_template
from services.materia_Service import MateriaService

materia_bp = Blueprint('materia', __name__)

@materia_bp.route('/')
def index():
    materias = Materia_Service.listar_tudo()
    return render_template('index.html', materias=materias)

@materia_bp.route('/materia/nova', methods=['POST'])
def nova():
    nome = request.form.get('nome')
    Materia_Service.criar_materia(nome)
    return redirect(url_for('materia.index'))