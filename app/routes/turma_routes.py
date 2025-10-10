from flask import Blueprint, request, jsonify
from app import db
from app.models import Turma, Professor

turma_bp = Blueprint("turma", __name__)


@turma_bp.route("/", methods=["POST"])
def criar_turma():
    data = request.get_json()
    try:
        nova_turma = Turma(
            descricao=data.get("descricao"),
            ativo=data.get("ativo", True),
            professor_id=data.get("professor_id")
        )
        db.session.add(nova_turma)
        db.session.commit()
        return jsonify({"mensagem": "Turma criada com sucesso!", "turma": {
            "id": nova_turma.id,
            "descricao": nova_turma.descricao,
            "ativo": nova_turma.ativo,
            "professor_id": nova_turma.professor_id
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400


@turma_bp.route("", methods=["POST"])
def criar_turma_sem_barra():
    return criar_turma()


@turma_bp.route("/", methods=["GET"])
def listar_turmas():
    turmas = Turma.query.all()
    resultado = []
    for t in turmas:
        resultado.append({
            "id": t.id,
            "descricao": t.descricao,
            "ativo": t.ativo,
            "professor_id": t.professor_id
        })
    return jsonify(resultado), 200


@turma_bp.route("", methods=["GET"])
def listar_turmas_sem_barra():
    return listar_turmas()


@turma_bp.route("/<int:id>", methods=["GET"])
def buscar_turma(id):
    turma = Turma.query.get_or_404(id)
    return jsonify({
        "id": turma.id,
        "descricao": turma.descricao,
        "ativo": turma.ativo,
        "professor_id": turma.professor_id
    }), 200


@turma_bp.route("/<int:id>", methods=["PUT"])
def atualizar_turma(id):
    turma = Turma.query.get_or_404(id)
    data = request.get_json()
    try:
        turma.descricao = data.get("descricao", turma.descricao)
        turma.ativo = data.get("ativo", turma.ativo)
        turma.professor_id = data.get("professor_id", turma.professor_id)
        db.session.commit()
        return jsonify({"mensagem": "Turma atualizada!", "turma": {
            "id": turma.id,
            "descricao": turma.descricao,
            "ativo": turma.ativo,
            "professor_id": turma.professor_id
        }}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400


@turma_bp.route("/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({"mensagem": "Turma deletada!"}), 200
