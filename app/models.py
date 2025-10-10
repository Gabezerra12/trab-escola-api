
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)  
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))  
    observacoes = db.Column(db.Text)
      
    turmas = db.relationship('Turma', backref='professor', lazy=True)
    
    def __repr__(self):
        return f'<Professor {self.nome}>'

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)  
    ativo = db.Column(db.Boolean, default=True)
    
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __repr__(self):
        return f'<Turma {self.descricao}>'

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)  
    idade = db.Column(db.Integer)
    
    
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    
    data_nascimento = db.Column(db.Date)  
    nota_primeiro_semestre = db.Column(db.Float) 
    nota_segundo_semestre = db.Column(db.Float)  
    media_final = db.Column(db.Float)  
    
    def __repr__(self):
        return f'<Aluno {self.nome}>'

