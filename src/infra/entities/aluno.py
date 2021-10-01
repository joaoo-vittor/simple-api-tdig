from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.infra.config import Base


class Aluno(Base):
    """aluno Entity"""

    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True)
    matricula = Column(Integer, nullable=True)
    nome = Column(String(100), nullable=True)
    cpf = Column(String(100), nullable=True)
    curso = Column(String(200), nullable=True)
    endereco_id = Column(Integer, ForeignKey('endereco.id'))

    endereco = relationship('Endereco')
