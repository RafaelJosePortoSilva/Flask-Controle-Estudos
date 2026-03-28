from flask import Flask
from models import db 
from routes.materia_Routes import materia_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudos.db'

db.init_app(app)

# Separação de rotas
app.register_blueprint(materia_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)