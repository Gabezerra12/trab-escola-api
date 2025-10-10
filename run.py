from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from app.models import db, Professor, Turma, Aluno
from app.routes.professor_routes import professor_bp
from app.routes.turma_routes import turma_bp
from app.routes.aluno_routes import aluno_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    print("✅ TABELAS CRIADAS COM SUCESSO!")

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Escola"}
)

app.register_blueprint(professor_bp, url_prefix='/api/professores')
app.register_blueprint(turma_bp, url_prefix='/api/turmas')
app.register_blueprint(aluno_bp, url_prefix='/api/alunos')
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:filename>')
def serve_static(filename):
    if filename == "swagger.json":
        return send_from_directory('static', filename, mimetype='application/json')
    return send_from_directory('static', filename)

@app.route("/")
def home():
    return jsonify({"msg": "API funcionando"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    
app.url_map.strict_slashes = False