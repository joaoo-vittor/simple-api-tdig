from flask import Blueprint, request, jsonify
from src.infra.config import DBConnectionHandler
from src.infra.entities import Aluno


app_bp_alunos = Blueprint("app_bp_alunos", __name__)


@app_bp_alunos.route("/read", methods=["GET"])
def get_alunos():

    message = []

    with DBConnectionHandler() as connection:
        try:
            engine = connection.get_engine()
            data = engine.execute("SELECT * FROM aluno;")

            for el in data:
                message.append(
                    {
                        "id": el[0],
                        "matricula": el[1],
                        "nome": el[2],
                        "cpf": el[3],
                        "curso": el[4],
                        "endereco_id": el[5],
                    }
                )

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify(message), 200


@app_bp_alunos.route("/read_one/<id>", methods=["GET"])
def get_aluno(id):
    id = int(id)

    with DBConnectionHandler() as connection:
        try:
            engine = connection.get_engine()
            data = engine.execute(f"SELECT * FROM aluno WHERE aluno.id = {id};")

            for el in data:
                message = {
                    "id": el[0],
                    "matricula": el[1],
                    "nome": el[2],
                    "cpf": el[3],
                    "curso": el[4],
                    "endereco_id": el[5],
                }

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify(message), 200


@app_bp_alunos.route("/create", methods=["POST"])
def post_aluno():
    data = request.get_json(force=True)

    if (
        "matricula" in data.keys()
        and "nome" in data.keys()
        and "cpf" in data.keys()
        and "curso" in data.keys()
    ):
        with DBConnectionHandler() as connection:
            try:
                if "endereco_id" in data.keys():
                    new_user = Aluno(
                        matricula=data["matricula"],
                        nome=data["nome"],
                        cpf=data["cpf"],
                        curso=data["curso"],
                        endereco_id=data["endereco_id"],
                    )
                else:
                    new_user = Aluno(
                        matricula=data["matricula"],
                        nome=data["nome"],
                        cpf=data["cpf"],
                        curso=data["curso"],
                    )

                connection.session.add(new_user)
                connection.session.commit()

                new_data = {
                    "id": new_user.id,
                    "nome": new_user.nome,
                    "matricula": new_user.matricula,
                    "curso": new_user.curso,
                    "cpf": new_user.cpf,
                    "endereco_id": new_user.endereco_id,
                }

            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return new_data, 200

    return {"msg": "invalid params."}, 400


@app_bp_alunos.route("/update/<id>", methods=["PUT"])
def put_aluno(id):
    id = int(id)

    data = request.get_json(force=True)

    if (
        "matricula" in data.keys()
        or "nome" in data.keys()
        or "cpf" in data.keys()
        or "curso" in data.keys()
        or "endereco_id" in data.keys()
    ):
        with DBConnectionHandler() as connection:
            try:

                if "id" in data.keys():
                    data.pop("id")

                connection.session.query(Aluno).filter_by(id=id).update(
                    data, synchronize_session=False
                )
                connection.session.commit()

            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return jsonify({"msg": "updated with success."}), 200

    return jsonify({"msg": "invalid params."}), 400


@app_bp_alunos.route("/delete/<id>", methods=["DELETE"])
def delete_aluno(id):
    id = int(id)

    with DBConnectionHandler() as connection:
        try:

            connection.session.query(Aluno).filter_by(id=id).delete()
            connection.session.commit()

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify({"msg": "deleted with success."}), 200
