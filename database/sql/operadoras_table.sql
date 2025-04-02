
CREATE TABLE operadoras (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(20),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(100),
    data_registro_ans DATE
);


CREATE UNIQUE INDEX idx_operadoras_registro_ans ON operadoras(registro_ans);
CREATE INDEX idx_operadoras_cnpj ON operadoras(cnpj);
CREATE INDEX idx_operadoras_cidade ON operadoras(cidade);
