from flask import Blueprint, request, jsonify
from src.infra.config import DBConnectionHandler
from src.infra.entities import Projeto


app_bp_projeto = Blueprint('app_bp_projeto', __name__)


@app_bp_projeto.route('/read', methods=['GET'])
def get_projetos():

    message = []

    with DBConnectionHandler() as connection:
        try:
            engine = connection.get_engine()
            data = engine.execute("SELECT * FROM projeto;")

            for el in data:
                message.append({
                    'id': el[0],
                    'titulo': el[1],
                    'area': el[2],
                    'resumo': el[3],
                    'palavra_chave_1': el[4],
                    'palavra_chave_2': el[5],
                    'palavra_chave_3': el[6],
                    'url_documento': el[7],
                    'professor_id': el[8],
                })
            
        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()
    
    return jsonify(message), 200


@app_bp_projeto.route('/create', methods=['POST'])
def post_projeto():
    data = request.get_json(force=True)

    list_params = ['titulo', 'area', 'resumo', 'palavra_chave_1', 
    'palavra_chave_2', 'palavra_chave_3', 'url_documento']

    if ('titulo' in data.keys()
        or 'area' in data.keys()
        or 'resumo' in data.keys()
        or 'palavra_chave_1' in data.keys()
        or 'palavra_chave_2' in data.keys()
        or 'palavra_chave_3' in data.keys()
        or 'url_documento' in data.keys()
    ):  
        for i in list_params:
            if i not in data.keys():
                data.update({i: ''})

        with DBConnectionHandler() as connection:
            try:
                if 'professor_id' in data.keys():
                    new_user = Projeto(
                        titulo=data['titulo'],
                        area=data['area'],
                        resumo=data['resumo'],
                        palavra_chave_1=data['palavra_chave_1'],
                        palavra_chave_2=data['palavra_chave_2'],
                        palavra_chave_3=data['palavra_chave_3'],
                        url_documento=data['url_documento'],
                        professor_id=data['professor_id']
                    )
                else:
                    new_user = Projeto(
                        titulo=data['titulo'],
                        area=data['area'],
                        resumo=data['resumo'],
                        palavra_chave_1=data['palavra_chave_1'],
                        palavra_chave_2=data['palavra_chave_2'],
                        palavra_chave_3=data['palavra_chave_3'],
                        url_documento=data['url_documento'],
                    )

                connection.session.add(new_user)
                connection.session.commit()

                new_data = {
                    'id': new_user.id,
                    'titulo': new_user.titulo,
                    'area': new_user.area,
                    'resumo': new_user.resumo,
                    'palavra_chave_1': new_user.palavra_chave_1,
                    'palavra_chave_2': new_user.palavra_chave_2,
                    'palavra_chave_3': new_user.palavra_chave_3,
                    'url_documento': new_user.url_documento,
                    'professor_id': new_user.professor_id,
                }

            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return new_data, 200
        
    return {'msg': 'invalid params.'}, 400


@app_bp_projeto.route('/update/<id>', methods=['PUT'])
def put_projeto(id):
    id = int(id)

    data = request.get_json(force=True)

    if ('titulo' in data.keys()
        or 'area' in data.keys()
        or 'resumo' in data.keys()
        or 'palavra_chave_1' in data.keys()
        or 'palavra_chave_2' in data.keys()
        or 'palavra_chave_3' in data.keys()
        or 'url_documento' in data.keys()
    ):
        with DBConnectionHandler() as connection:
            try:

                if "professor_id" in data.keys():
                    data.pop("professor_id")

                connection.session.query(Projeto).filter_by(
                    id=id
                ).update(data, synchronize_session=False)
                connection.session.commit()
                
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
        
        return jsonify({'msg': 'updated with success.'}), 200
    
    return jsonify({'msg': 'invalid params.'}), 400


@app_bp_projeto.route('/delete/<id>', methods=['DELETE'])
def delete_projeto(id):
    id = int(id)

    with DBConnectionHandler() as connection:
        try:
            
            connection.session.query(Projeto).filter_by(
                id=id
            ).delete()
            connection.session.commit()

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify({'msg': 'deleted with success.'}), 200
