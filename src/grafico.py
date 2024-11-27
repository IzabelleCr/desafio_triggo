import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


db_url = 'mysql+pymysql://Triggo:1234@localhost/projetotriggoai'
engine = create_engine(db_url)


sql_query = """
SELECT 
    YEAR(Vendas.Data_da_Venda) AS Ano,
    QUARTER(Vendas.Data_da_Venda) AS Trimestre,
    SUM(Vendas.Valor) AS Total_Vendas
FROM 
    Vendas
GROUP BY 
    Ano, Trimestre
ORDER BY 
    Ano, Trimestre;
"""


df = pd.read_sql(sql_query, engine)


print(df.head())


plt.figure(figsize=(10, 6))


df['Ano_Trimestre'] = df['Ano'].astype(str) + " - T" + df['Trimestre'].astype(str)


plt.plot(df['Ano_Trimestre'], df['Total_Vendas'], marker='o', linestyle='-', color='b')


plt.title('Vendas Trimestrais', fontsize=16)
plt.xlabel('Ano - Trimestre', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)


plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R$ {x:,.2f}'))


plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
