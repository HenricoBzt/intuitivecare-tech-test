from sqlalchemy import Column, Integer, String, Date
from app.backend.database import Base

class OperadorasModel(Base):  
    __tablename__ = 'operadoras'

    id = Column(Integer, primary_key=True, index=True)
    registro_ans = Column(String(20), unique=True, index=True, nullable=False)
    cnpj = Column(String(20), index=True, nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(50))
    complemento = Column(String(255), nullable=True)
    bairro = Column(String(100))
    cidade = Column(String(100), index=True, nullable=False)
    uf = Column(String(2), nullable=False)
    cep = Column(String(20), nullable=False)
    ddd = Column(String(5))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255), nullable=True)
    representante = Column(String(255), nullable=True)
    cargo_representante = Column(String(255), nullable=True)
    regiao_de_comercializacao = Column(String(100))
    data_registro_ans = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Operadora(id={self.id}, registro_ans={self.registro_ans}, cnpj={self.cnpj}, cidade={self.cidade}, uf={self.uf})>"
