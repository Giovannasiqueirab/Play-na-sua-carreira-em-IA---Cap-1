-- Scritp para criação das tabelas e suas dependências 


-- Tabela das Regiões Brasileiras
CREATE TABLE regioes (
    id_regiao NUMBER PRIMARY KEY,
    nome VARCHAR2(50) NOT NULL
);

-- Tabela de Fazendas
CREATE TABLE fazendas (
    id_fazenda NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    id_regiao NUMBER,
    FOREIGN KEY (id_regiao) REFERENCES regioes(id_regiao)
);

-- Tabela de Plantações
CREATE TABLE Plantacoes (
    id_plantacao NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    epoca VARCHAR2(20),
    melhor_temperatura VARCHAR2(20),
    id_regiao_ideal NUMBER,
    CONSTRAINT fk_regiao_plantacao FOREIGN KEY (id_regiao_ideal) REFERENCES Regioes(id_regiao)
);

-- Tabela dos Insumos
CREATE TABLE insumos (
    id_insumo NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    preco_usd NUMBER(10, 2)
);

-- Tabela da previsão do tempo
CREATE TABLE previsoes (
    id_previsao NUMBER PRIMARY KEY,
    id_plantacao NUMBER,
    id_fazenda NUMBER,
    estacao VARCHAR2(20),
    percentual_sucesso NUMBER(5,2),
    FOREIGN KEY (id_plantacao) REFERENCES plantacoes(id_plantacao),
    FOREIGN KEY (id_fazenda) REFERENCES fazendas(id_fazenda)
);

-- Tabela de ligação Plantações x Insumo
CREATE TABLE plantacao_insumo (
    id_plantacao NUMBER,
    id_insumo NUMBER,
    PRIMARY KEY (id_plantacao, id_insumo),
    FOREIGN KEY (id_plantacao) REFERENCES plantacoes(id_plantacao),
    FOREIGN KEY (id_insumo) REFERENCES insumos(id_insumo)
);

-- Tabela de Sensores
CREATE TABLE Sensores (
    id_sensor INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('S1', 'S2', 'S3') NOT NULL,
    descricao VARCHAR(255)
);

-- Tabela de Leituras dos Sensores
CREATE TABLE Leituras_Sensores (
    id_leitura INT AUTO_INCREMENT PRIMARY KEY,
    id_sensor INT NOT NULL,
    id_plantacao INT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_lido DOUBLE,

    -- Chaves estrangeiras
    FOREIGN KEY (id_sensor) REFERENCES Sensores(id_sensor),
    FOREIGN KEY (id_plantacao) REFERENCES Plantacoes(id_plantacao)
);
