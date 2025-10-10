from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint  
from app.models import db
from flask_migrate import Migrate
from app.routes.professor_routes import professor_bp
from app.routes.turma_routes import turma_bp
from app.routes.aluno_routes import aluno_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)  

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "API Gerenciamento Escolar"}
    )
    app.register_blueprint(professor_bp, url_prefix='/api/professores')
    app.register_blueprint(turma_bp, url_prefix='/api/turmas')
    app.register_blueprint(aluno_bp, url_prefix='/api/alunos')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app