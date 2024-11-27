USE ProjetoTriggoAI;

SELECT 
    Vendas.ID AS id_vendas, 
    Clientes.Cliente AS Nome_Cliente, 
    Vendas.Data_da_Venda
FROM 
    Vendas
JOIN 
    Clientes ON Vendas.Cliente = Clientes.Cliente AND Vendas.Regional = Clientes.Regional
WHERE 
    YEAR(Vendas.Data_da_Venda) = 2020;
