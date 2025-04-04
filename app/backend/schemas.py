from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class MyBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class OperadoraBase(MyBaseModel):
    id: int
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = "" 
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str] = ""     
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: Optional[str] = ""            
    telefone: Optional[str] = ""      
    fax: Optional[str] = ""              
    endereco_eletronico: Optional[str] = "" 
    representante: str
    cargo_representante: str
    regiao_de_comercializacao: Optional[str] = "" 
    data_registro_ans: date

class OperadoraList(MyBaseModel):
    operadoras: list[OperadoraBase]
