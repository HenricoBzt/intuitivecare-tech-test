
-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT reg_ans,
       SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis
WHERE data BETWEEN '2023-11-10' AND '2024-01-10'
  AND (
       descricao ILIKE '%SINISTROS CONHECIDOS%' 
       OR descricao ILIKE '%SINISTROS AVISADOS%' 
       OR descricao ILIKE '%EVENTOS%'
  )
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;

SELECT opera.nome_fantasia,
       demonstra.reg_ans,
       SUM(demonstra.vl_saldo_final - demonstra.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis demonstra
JOIN operadoras opera ON demonstra.reg_ans = opera.registro_ans
WHERE demonstra.data BETWEEN '2023-11-10' AND '2024-01-10'
  AND (
       demonstra.descricao ILIKE '%SINISTROS CONHECIDOS%'
       OR demonstra.descricao ILIKE '%SINISTROS AVISADOS%'
       OR demonstra.descricao ILIKE '%EVENTOS%'
  )
GROUP BY opera.nome_fantasia, demonstra.reg_ans
ORDER BY total_despesas DESC
LIMIT 10;