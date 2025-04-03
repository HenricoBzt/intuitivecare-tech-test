-- Importação de CSV para a tabela demonstracoes_contabeis
-- Substitua 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/' pelo caminho correto do seu arquivo CSV

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/1T2023.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/2t2023.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/3T2023.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/4T2023.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/1T2024.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/2T2024.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/3T2024.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_etl/csv_processed/4T2024.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');

-- Importação do CSV de operadoras
\copy operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans) FROM 'C:/Users/henri/intuitivecare-tech-test/database/data_zips/operadoras/operadoras_ativas.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER, ENCODING 'UTF8');