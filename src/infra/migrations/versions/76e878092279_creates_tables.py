"""creates tables

Revision ID: 76e878092279
Revises: 
Create Date: 2021-09-30 19:06:42.390184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, Text


# revision identifiers, used by Alembic.
revision = "76e878092279"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "endereco",
        Column("id", Integer, primary_key=True),
        Column("rua", String(255), nullable=False),
        Column("numero", String(8), nullable=False),
        Column("cep", String(14), nullable=False),
        Column("cidade", String(50), nullable=False),
        Column("estado", String(50), nullable=False),
        Column("pais", String(50), nullable=False),
    )

    op.create_table(
        "aluno",
        Column("id", Integer, primary_key=True),
        Column("matricula", Integer, nullable=False),
        Column("nome", String(100), nullable=False),
        Column("cpf", String(100), nullable=False),
        Column("curso", String(200), nullable=False),
        Column("endereco_id", Integer, nullable=True),
        sa.ForeignKeyConstraint(["endereco_id"], ["endereco.id"]),
    )

    op.create_table(
        "professor",
        Column("id", Integer, primary_key=True),
        Column("matricula", Integer, nullable=False),
        Column("nome", String(100), nullable=False),
        Column("curso", String(200), nullable=False),
        Column("endereco_id", Integer, nullable=True),
        sa.ForeignKeyConstraint(["endereco_id"], ["endereco.id"]),
    )

    op.create_table(
        "projeto",
        Column("id", Integer, primary_key=True),
        Column("titulo", String(100), nullable=False),
        Column("area", String(200), nullable=False),
        Column("resumo", Text(200), nullable=False),
        Column("palavra_chave_1", String(200), nullable=False),
        Column("palavra_chave_2", String(200), nullable=False),
        Column("palavra_chave_3", String(200), nullable=False),
        Column("url_documento", String(200), nullable=False),
        Column("professor_id", Integer, nullable=True),
        Column("aluno_id", Integer, nullable=True),
        sa.ForeignKeyConstraint(["professor_id"], ["professor.id"]),
        sa.ForeignKeyConstraint(["aluno_id"], ["aluno.id"]),
    )


def downgrade():
    op.drop_table("endereco")
    op.drop_table("aluno")
    op.drop_table("professor")
    op.drop_table("projeto")
