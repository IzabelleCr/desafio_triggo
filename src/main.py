from helpers import configure_locale, format_money, encontrar_arquivo
from processing import calcular_maiores_e_menores_vendas
from cleaner import DataCleaner
import pandas as pd
import os

def main():
    configure_locale()  

    
    nome_arquivo = 'DB_Teste_modificado.csv'
    
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorios_para_procurar = [
        os.path.join(diretorio_atual, '..', 'data'),
        diretorio_atual,
        os.path.join(diretorio_atual, '..'),
        os.path.join(diretorio_atual, 'subdiretorio1'),
        os.path.join(diretorio_atual, 'subdiretorio2')
    ]
    
    
    caminho_arquivo = encontrar_arquivo(nome_arquivo, diretorios_para_procurar)
    
    if not caminho_arquivo:
        print(f"O arquivo {nome_arquivo} não foi encontrado nos caminhos verificados.")
        return
    else:
        print(f"Carregando o arquivo a partir do caminho: {caminho_arquivo}")

    
    df = pd.read_csv(caminho_arquivo, sep=';')
    
    
    df.columns = DataCleaner.clean_column_names(df)
    
    
    df = DataCleaner.clean_value_column(df)
    
   
    maior_venda, menor_venda, cliente_com_maior_venda, cliente_com_menor_venda, vendedor_com_maior_venda, vendedor_com_menor_venda = calcular_maiores_e_menores_vendas(df)
    
    
    vendas_por_tipo = df.groupby('tipo')['valor'].mean()
    numero_de_vendas_por_cliente = df['cliente'].value_counts()
    
    
    tabela_auxiliar = df.groupby('vendedor')['valor'].sum().sort_values(ascending=False)
    
    
    soma_total_vendas = df['valor'].sum()

    
    quantidade_vendas_totais = len(df)
    
    
    csv_path = os.path.join(diretorio_atual, '..', 'resumo_vendas.csv')
    tabela_auxiliar.to_csv(csv_path, sep=';', index=True, float_format='%.2f')
    
    
    print("\n=== Total Vendido por Vendedor (Ordenado) ===\n")
    print(tabela_auxiliar.map(format_money))  
    
    print("\n=== Venda Mais Alta ===")
    print(f"Cliente: {cliente_com_maior_venda}, Vendedor: {vendedor_com_maior_venda}, Valor: {format_money(maior_venda)}")
    
    print("\n=== Venda Mais Baixa ===")
    print(f"Cliente: {cliente_com_menor_venda}, Vendedor: {vendedor_com_menor_venda}, Valor: {format_money(menor_venda)}")
    
    print("\n=== Valor Médio por Tipo de Venda ===")
    print(vendas_por_tipo.map(format_money)) 
    
    print("\n=== Número de Vendas por Cliente ===")
    for cliente, valor in numero_de_vendas_por_cliente.items():
        print(f"{cliente}: {valor}")
    
   
    print(f"\n=== A soma total das vendas é {format_money(soma_total_vendas)} ===")
    
    
    print(f"\n=== A quantidade total de vendas é {quantidade_vendas_totais} ===\n")

if __name__ == "__main__":
    main()
