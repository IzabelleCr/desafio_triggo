## Introdução ##

##### Este projeto foi desenvolvido para processar, organizar e analisar dados relacionados a vendas, utilizando ferramentas como Python e SQL. A proposta inclui a criação de um banco de dados relacional, a manipulação dos dados fornecidos em arquivos CSV e a geração de análises e gráficos baseados nesses dados.#####

## Estrutura do Projeto ##

-  O projeto foi modularizado para garantir organização e facilitar a manutenção. Ele é composto por diversos scripts Python e arquivos SQL, divididos conforme suas responsabilidades:

### Scripts Python ###

 **cleaner.py:** Realiza a limpeza e padronização de dados, incluindo o ajuste de nomes de colunas e conversão de valores financeiros.

 **helpers.py:** Contém funções auxiliares para formatação de valores e outras tarefas recorrentes.

 **integracao_banco.py:** Gerencia a integração entre os dados processados e o banco de dados MySQL. 

**processing.py:** Executa análises detalhadas, como identificação das maiores vendas, cálculo de médias e totais.

**grafico.py:** Gera gráficos para visualização de dados, como vendas trimestrais.

**main.py:** Arquivo principal que orquestra as funções de todos os outros módulos, controlando o fluxo completo do programa.

### Arquivo SQL ###

**create_database.sql:** Define a estrutura do banco de dados, incluindo tabelas, chaves primárias e estrangeiras para manter a integridade referencial.

### Documentação### 

Inclui um arquivo PDF com detalhes completos do projeto, suas etapas e decisões de implementação.

### Instruções de Execução ### 

**Pré-requisitos**

- Python 3.x instalado.

- MySQL instalado e configurado.

- Instale as bibliotecas necessárias utilizando o comando:

pip install pandas
pip install SQLAlchemy
pip install matplotlib
pip install pymysql

As dependências incluem:

- pandas

- SQLAlchemy

- matplotlib

- mysql-connector-python ou pymysql

### Configuração do Banco de Dados ###

- Certifique-se de que o MySQL está ativo.

- Execute o script SQL para criar o banco de dados e as tabelas:

- mysql -u SEU_USUARIO -p < create_database.sql

### Execução do Projeto ###

- Coloque o arquivo CSV com os dados na pasta raiz do projeto.

- Execute o arquivo principal para iniciar o processamento:

**python main.py **

### O programa irá: ###

- Limpar e processar os dados do CSV.

- Inserir os dados no banco de dados.

- Gerar análises e relatórios.

- Criar gráficos com base nos resultados.

### O que foi feito ###

- Modelagem do Banco de Dados:

- Estrutura normalizada com tabelas Clientes, Vendedores e Vendas.

- Uso de chaves primárias compostas para evitar duplicidade.

- Relacionamentos estabelecidos com chaves estrangeiras para garantir integridade.

### Processamento de Dados:### 

- Limpeza e padronização dos dados brutos para adequá-los ao banco de dados.

- Conversão de formatos de valores e datas.

- Análises e Visualizações:

- Cálculo de métricas como vendas por cliente, valores médios e totais.

- Geração de gráficos para análise visual.

### Automação e Modularidade:### 

- Separação das responsabilidades em módulos distintos para melhorar a organização e escalabilidade.

### Documentação Adicional ###

- Um arquivo PDF detalhado contendo todas as decisões de implementação e explicações sobre o projeto está incluído nesta entrega. Por favor, consulte o arquivo anexado para uma visão abrangente do sistema.

### Conclusão ###

- Este projeto foi projetado para ser robusto, escalável e fácil de manter. A estrutura modular e o uso de boas práticas em SQL e Python garantem que o sistema seja eficiente e preparado para futuros aprimoramentos