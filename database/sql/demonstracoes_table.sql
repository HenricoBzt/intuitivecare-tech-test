CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR(20),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial DECIMAL(15, 2),
    vl_saldo_final DECIMAL(15, 2)
);


CREATE INDEX idx_demonstracoes_data ON demonstracoes_contabeis(data);
CREATE INDEX idx_demonstracoes_reg_ans ON demonstracoes_contabeis(reg_ans);
CREATE INDEX idx_demonstracoes_descricao ON demonstracoes_contabeis(descricao varchar_pattern_ops);