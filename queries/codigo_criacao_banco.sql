CREATE DATABASE IF NOT EXISTS ProjetoTriggoAI;

USE ProjetoTriggoAI;

CREATE TABLE IF NOT EXISTS Clientes (
    Cliente VARCHAR(255) NOT NULL,
    Regional VARCHAR(255) NOT NULL,
    PRIMARY KEY (Cliente, Regional)
);

CREATE TABLE IF NOT EXISTS Vendedores (
    Vendedor VARCHAR(255) NOT NULL,
    Equipe VARCHAR(255) NOT NULL,
    PRIMARY KEY (Vendedor, Equipe)
);

CREATE TABLE IF NOT EXISTS Vendas (
    ID BIGINT NOT NULL,
    Data_da_Venda DATE NOT NULL,
    Tipo VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Cliente VARCHAR(255) NOT NULL,
    Regional VARCHAR(255) NOT NULL,
    Vendedor VARCHAR(255) NOT NULL,
    Equipe VARCHAR(255) NOT NULL,
    Duracao_do_Contrato INT NOT NULL,
    Valor DECIMAL(18, 2) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (Cliente, Regional) REFERENCES Clientes(Cliente, Regional),
    FOREIGN KEY (Vendedor, Equipe) REFERENCES Vendedores(Vendedor, Equipe)
);
