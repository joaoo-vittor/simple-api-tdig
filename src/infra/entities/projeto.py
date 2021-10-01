from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Projeto(Base):
    """projeto Entity"""

    __tablename__ = "projeto"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=True)
    area = Column(String(200), nullable=True)
    resumo = Column(Text(200), nullable=True)
    palavra_chave_1 = Column(String(200), nullable=True)
    palavra_chave_2 = Column(String(200), nullable=True)
    palavra_chave_3 = Column(String(200), nullable=True)
    url_documento = Column(String(200), nullable=True)
    professor_id = Column(Integer, ForeignKey('professor.id'))

    professor = relationship('Professor')
