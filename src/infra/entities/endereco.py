from sqlalchemy import Column, String, Integer
from src.infra.config import Base

class Endereco(Base):
    """endereco Entity"""

    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True)
    rua = Column(String(255), nullable=True)
    numero = Column(String(8), nullable=True)
    cep = Column(String(14), nullable=True)
    cidade = Column(String(50), nullable=True)
    estado = Column(String(50), nullable=True)
    pais = Column(String(50), nullable=True)
