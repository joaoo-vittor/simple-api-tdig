from flask import Blueprint, request, jsonify
from src.infra.config import DBConnectionHandler
from src.infra.entities import Endereco


app_bp_endereco = Blueprint("app_bp_endereco", __name__)


@app_bp_endereco.route("/read", methods=["GET"])
def get_enderecos():

    message = []

    with DBConnectionHandler() as connection:
        try:
            engine = connection.get_engine()
            data = engine.execute("SELECT * FROM endereco;")

            for el in data:
                message.append(
                    {
                        "id": el[0],
                        "rua": el[1],
                        "numero": el[2],
                        "cep": el[3],
                        "cidade": el[4],
                        "estado": el[5],
                        "pais": el[6],
                    }
                )

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify(message), 200


@app_bp_endereco.route("/read_one/<id>", methods=["GET"])
def get_endereco(id):
    id = int(id)
    with DBConnectionHandler() as connection:
        try:
            engine = connection.get_engine()
            data = engine.execute(f"SELECT * FROM endereco WHERE endereco.id = {id}")
            for el in data:
                message = {
                    "id": el[0],
                    "rua": el[1],
                    "numero": el[2],
                    "cep": el[3],
                    "cidade": el[4],
                    "estado": el[5],
                    "pais": el[6],
                }

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify(message), 200


@app_bp_endereco.route("/create", methods=["POST"])
def post_endereco():
    data = request.get_json(force=True)

    if (
        "rua" in data.keys()
        and "numero" in data.keys()
        and "cep" in data.keys()
        and "cidade" in data.keys()
        and "estado" in data.keys()
        and "pais" in data.keys()
    ):
        with DBConnectionHandler() as connection:
            try:
                new_endereco = Endereco(
                    rua=data["rua"],
                    numero=data["numero"],
                    cep=data["cep"],
                    cidade=data["cidade"],
                    estado=data["estado"],
                    pais=data["pais"],
                )

                connection.session.add(new_endereco)
                connection.session.commit()

                new_data = {
                    "id": new_endereco.id,
                    "rua": new_endereco.rua,
                    "numero": new_endereco.numero,
                    "cep": new_endereco.cep,
                    "cidade": new_endereco.cidade,
                    "estado": new_endereco.estado,
                    "pais": new_endereco.pais,
                }

            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

        return jsonify(new_data), 200

    return {"msg": "invalid params."}, 400


@app_bp_endereco.route("/update/<id>", methods=["PUT"])
def put_endereco(id):
    id = int(id)

    data = request.get_json(force=True)

    if (
        "rua" in data.keys()
        or "numero" in data.keys()
        or "cep" in data.keys()
        or "cidade" in data.keys()
        or "estado" in data.keys()
        or "pais" in data.keys()
    ):
        with DBConnectionHandler() as connection:
            try:

                if "id" in data.keys():
                    data.pop("id")

                connection.session.query(Endereco).filter_by(id=id).update(
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


@app_bp_endereco.route("/delete/<id>", methods=["DELETE"])
def delete_endereco(id):
    id = int(id)

    with DBConnectionHandler() as connection:
        try:

            connection.session.query(Endereco).filter_by(id=id).delete()
            connection.session.commit()

        except:
            connection.session.rollback()
            raise
        finally:
            connection.session.close()

    return jsonify({"msg": "deleted with success."}), 200
