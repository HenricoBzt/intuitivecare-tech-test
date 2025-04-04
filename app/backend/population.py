import csv
from app.backend.database import async_session
from app.backend.models import OperadorasModel
from datetime import date
from sqlalchemy import text

async def population_operadoras(csv_path: str):
    async with async_session() as session:
        result = await session.execute(text("SELECT * FROM operadoras"))
        count = result.scalar()

        if count > 0:
            print("Tabela já populada")
            return
        
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            operadoras = []


            for row in reader:
                operadora = OperadorasModel(
                    registro_ans=row['Registro_ANS'],
                    cnpj=row['CNPJ'],
                    razao_social=row['Razao_Social'],
                    nome_fantasia=row.get['Nome_Fantasia', ''],
                    modalidade=row['Modalidade'],
                    logradouro=row['Logradouro'],
                    numero=row['Numero'],
                    complemento=row.get['Complemento', ''],
                    bairro=row['Bairro'],
                    cidade=row['Cidade'],
                    uf=row['UF'],
                    cep=row['CEP'],
                    ddd=row.get['DDD', ''],
                    telefone=row.get['Telefone', ''],
                    fax=row['Fax', ''],
                    endereco_eletronico=row.get['Endereco_eletronico', ''],
                    representante=row['Representante'],
                    cargo_representante=row['Cargo_Representante'],
                    regiao_de_comercializacao=row.get['Regiao_de_Comercializacao', ''],
                    data_registro_ans=date.fromisoformat(row['Data_Registro_ANS'])
                )
                operadoras.append(operadora)

            session.add_all(operadoras)
            await session.commit()
            print("Tabela populada com sucesso!")