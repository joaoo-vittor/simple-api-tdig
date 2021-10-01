from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Professor(Base):
    """professor Entity"""

    __tablename__ = "professor"

    id = Column(Integer, primary_key=True)
    matricula = Column(Integer, nullable=True)
    nome = Column(String(100), nullable=True)
    curso = Column(String(200), nullable=True)
    endereco_id = Column(Integer, ForeignKey('endereco.id'))

    endereco = relationship('Endereco')
