USE ProjetoTriggoAI;

SELECT 
    YEAR(Vendas.Data_da_Venda) AS Ano,
    QUARTER(Vendas.Data_da_Venda) AS Trimestre,
    FORMAT(SUM(Vendas.Valor), 2, 'de_DE') AS Total_Vendas_Formatado
FROM 
    Vendas
GROUP BY 
    Ano, Trimestre
ORDER BY 
    Ano, Trimestre;
