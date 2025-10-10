from flask import Blueprint, request, jsonify
from app.models import db, Professor

professor_bp = Blueprint('professores', __name__)


@professor_bp.route('', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([{
        "id": p.id, 
        "nome": p.nome, 
        "idade": p.idade, 
        "materia": p.materia
    } for p in professores])


@professor_bp.route('', methods=['POST'])
def add_professor():
    data = request.get_json()
    try:
        professor = Professor(
            nome=data["nome"],
            idade=data.get("idade"),
            materia=data.get("materia"),
            observacoes=data.get("observacoes")
        )
        db.session.add(professor)
        db.session.commit()
        return jsonify({"msg": "Professor criado", "id": professor.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400


@professor_bp.route('/<int:id>', methods=['GET'])
def get_professor(id):
    prof = Professor.query.get_or_404(id)
    return jsonify({
        "id": prof.id, 
        "nome": prof.nome, 
        "idade": prof.idade, 
        "materia": prof.materia,
        "observacoes": prof.observacoes
    })


@professor_bp.route('/<int:id>', methods=['PUT'])
def update_professor(id):
    prof = Professor.query.get_or_404(id)
    data = request.get_json()
    try:
        if "nome" in data: prof.nome = data["nome"]
        if "idade" in data: prof.idade = data["idade"]
        if "materia" in data: prof.materia = data["materia"]
        if "observacoes" in data: prof.observacoes = data["observacoes"]
        db.session.commit()
        return jsonify({"msg": "Professor atualizado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400


@professor_bp.route('/<int:id>', methods=['DELETE'])
def delete_professor(id):
    prof = Professor.query.get_or_404(id)
    db.session.delete(prof)
    db.session.commit()
    return jsonify({"msg": "Professor deletado"})
