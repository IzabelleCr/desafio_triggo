import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime

csv_path = r'C:/Users/Izzie/Documents/Pessoal/Teste TriggoAi/Project_Triggo_Ai/data/DB_Teste_modificado.csv'

db_url = 'mysql+pymysql://Triggo:1234@localhost/projetotriggoai'

engine = create_engine(db_url)

df = pd.read_csv(csv_path, sep=';')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.rename(columns={'data_da_venda': 'data'}, inplace=True)

print("Colunas após renomeação:", df.columns)

print(df.head())

if 'data' not in df.columns:
    print("Erro: A coluna 'data' não foi encontrada. As colunas disponíveis são:")
    print(df.columns)
    exit()

Session = sessionmaker(bind=engine)
session = Session()

clientes = df[['cliente', 'regional']].drop_duplicates()
for _, row in clientes.iterrows():
    session.execute(
        text("""
        INSERT IGNORE INTO Clientes (Cliente, Regional)
        VALUES (:cliente, :regional)
        """), {'cliente': row['cliente'], 'regional': row['regional']}
    )

vendedores = df[['vendedor', 'equipe']].drop_duplicates()
for _, row in vendedores.iterrows():
    session.execute(
        text("""
        INSERT IGNORE INTO Vendedores (Vendedor, Equipe)
        VALUES (:vendedor, :equipe)
        """), {'vendedor': row['vendedor'], 'equipe': row['equipe']}
    )


session.commit()


for _, row in df.iterrows():

    valor = str(row['valor']).replace(',', '.')

   
    try:
        valor = float(valor)
    except ValueError:
        print(f"Erro ao converter o valor: {row['valor']}")
        continue 

    
    cliente_id = session.execute(
        text("SELECT Cliente FROM Clientes WHERE Cliente = :cliente AND Regional = :regional"),
        {'cliente': row['cliente'], 'regional': row['regional']}
    ).fetchone()[0]

    vendedor_id = session.execute(
        text("SELECT Vendedor FROM Vendedores WHERE Vendedor = :vendedor AND Equipe = :equipe"),
        {'vendedor': row['vendedor'], 'equipe': row['equipe']}
    ).fetchone()[0]

   
    try:
        data = datetime.strptime(row['data'], '%d/%m/%Y')
    except ValueError:
        print(f"Erro ao converter a data: {row['data']}")
        continue  

    
    session.execute(
        text("""
        INSERT INTO Vendas (ID, Data_da_Venda, Tipo, Categoria, Cliente, Regional, Vendedor, Equipe, Duracao_do_Contrato, Valor)
        VALUES (:id, :data, :tipo, :categoria, :cliente, :regional, :vendedor, :equipe, :duracao_do_contrato, :valor)
        """), {
            'id': row['id'],  
            'data': data,
            'tipo': row['tipo'],
            'categoria': row['categoria'],
            'cliente': row['cliente'],
            'regional': row['regional'],
            'vendedor': row['vendedor'],
            'equipe': row['equipe'],
            'duracao_do_contrato': row['duracao_do_contrato_meses'],
            'valor': valor  
        })


session.commit()


session.close()

print("Dados inseridos com sucesso no banco de dados!")
