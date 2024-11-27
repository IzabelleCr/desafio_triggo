def calcular_maiores_e_menores_vendas(df):
    """Calcula as maiores e menores vendas"""
    maior_venda = df['valor'].max()
    menor_venda = df['valor'].min()
    cliente_com_maior_venda = df[df['valor'] == maior_venda]['cliente'].values[0]
    cliente_com_menor_venda = df[df['valor'] == menor_venda]['cliente'].values[0]
    vendedor_com_maior_venda = df[df['valor'] == maior_venda]['vendedor'].values[0]
    vendedor_com_menor_venda = df[df['valor'] == menor_venda]['vendedor'].values[0]
    return maior_venda, menor_venda, cliente_com_maior_venda, cliente_com_menor_venda, vendedor_com_maior_venda, vendedor_com_menor_venda
