from flask import Blueprint, request, jsonify
from app.models import db, Aluno
from datetime import datetime, date

aluno_bp = Blueprint("alunos", __name__)

@aluno_bp.route("/", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{
        "id": a.id, "nome": a.nome, "idade": a.idade, "turma_id": a.turma_id,
        "nota1": a.nota_primeiro_semestre, "nota2": a.nota_segundo_semestre, "media": a.media_final
    } for a in alunos])

@aluno_bp.route("", methods=["GET"])
def listar_alunos_sem_barra():
    return listar_alunos()

@aluno_bp.route("/", methods=["POST"])
def criar_aluno():
    data = request.get_json()
    try:
        data_nascimento = data.get("data_nascimento")
        idade = None
        if data_nascimento:
            data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            hoje = date.today()
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        nota1 = data.get("nota_primeiro_semestre")
        nota2 = data.get("nota_segundo_semestre")
        media_final = None
        if nota1 is not None and nota2 is not None:
            media_final = (float(nota1) + float(nota2)) / 2
        aluno = Aluno(
            nome=data["nome"],
            idade=idade,
            turma_id=data["turma_id"],
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=nota1,
            nota_segundo_semestre=nota2,
            media_final=media_final
        )
        db.session.add(aluno)
        db.session.commit()
        return jsonify({"msg": "Aluno criado", "id": aluno.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400

@aluno_bp.route("", methods=["POST"])
def criar_aluno_sem_barra():
    return criar_aluno()

@aluno_bp.route("/<int:id>", methods=["GET"])
def buscar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify({
        "id": aluno.id, "nome": aluno.nome, "idade": aluno.idade, "turma_id": aluno.turma_id,
        "nota1": aluno.nota_primeiro_semestre, "nota2": aluno.nota_segundo_semestre, "media": aluno.media_final
    })

@aluno_bp.route("/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()
    try:
        if "nome" in data: aluno.nome = data["nome"]
        if "turma_id" in data: aluno.turma_id = data["turma_id"]
        if "data_nascimento" in data:
            aluno.data_nascimento = datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date()
            hoje = date.today()
            aluno.idade = hoje.year - aluno.data_nascimento.year - ((hoje.month, hoje.day) < (aluno.data_nascimento.month, aluno.data_nascimento.day))
        if "nota_primeiro_semestre" in data: aluno.nota_primeiro_semestre = data["nota_primeiro_semestre"]
        if "nota_segundo_semestre" in data: aluno.nota_segundo_semestre = data["nota_segundo_semestre"]
        # Atualiza média se as notas existirem
        if aluno.nota_primeiro_semestre is not None and aluno.nota_segundo_semestre is not None:
            aluno.media_final = (float(aluno.nota_primeiro_semestre) + float(aluno.nota_segundo_semestre)) / 2
        db.session.commit()
        return jsonify({"msg": "Aluno atualizado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"msg": "Aluno deletado"})