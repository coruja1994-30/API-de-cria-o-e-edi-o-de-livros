from flask import Blueprint, jsonify, request
from app.models import Livro, db

routes = Blueprint('routes', __name__)

@routes.route('/livros', methods=['GET'])
def obter_livros():
    livros = Livro.query.all()
    return jsonify([livro.to_dict() for livro in livros])

@routes.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = Livro.query.get(id)
    if livro:
        return jsonify(livro.to_dict())
    return jsonify({'message': 'Livro não encontrado'}), 404

@routes.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livro = Livro(**novo_livro)
    db.session.add(livro)
    db.session.commit()
    return jsonify(livro.to_dict()), 201

@routes.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro = Livro.query.get(id)
    if livro:
        livro_alterado = request.get_json()
        for key, value in livro_alterado.items():
            setattr(livro, key, value)
        db.session.commit()
        return jsonify(livro.to_dict())
    return jsonify({'message': 'Livro não encontrado'}), 404

@routes.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    livro = Livro.query.get(id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
        return jsonify({'message': 'Livro excluído com sucesso'})
    return jsonify({'message': 'Livro não encontrado'}), 404