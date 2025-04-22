## FIAP - Faculdade de Informática e Administração Paulista

<br>

# Atividade Cap 1 - Um mapa do tesouro

## Grupo 41

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Giovanna Siqueira Batista</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Ednilton Lucio de Souza Lordes</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Carlos Alberto Valério dos Santos</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Arthur Augustus Barreira Dias</a> 



## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 🎯 Objetivo


Desenvolver um Modelo Entidade-Relacionamento (MER) e um Diagrama Entidade-Relacionamento (DER) para um banco de dados relacional, utilizando o Oracle SQL Developer Data Modeler.


## 🧱 Estrutura (MER)
Este projeto representa uma base de dados voltada para a gestão agrícola, considerando informações de plantações, fazendas, insumos, sensores e previsões do tempo. Abaixo estão descritas as entidades e seus relacionamentos:

### 📍 Regiões (regioes)
Armazena as regiões brasileiras onde as fazendas estão localizadas.

id_regiao (PK): Identificador único da região.

nome: Nome da região.

### 🌾 Fazendas (fazendas)
Contém as fazendas cadastradas no sistema.

id_fazenda (PK): Identificador único da fazenda.

nome: Nome da fazenda.

id_regiao (FK): Região onde a fazenda está localizada (regioes).

### 🌱 Plantações (plantacoes)
Representa as plantações disponíveis e suas características ideais.

id_plantacao (PK): Identificador da plantação.

nome: Nome da plantação.

epoca: Época ideal para o cultivo.

melhor_temperatura: Temperatura ideal para o cultivo.

id_regiao_ideal (FK): Região ideal para essa plantação (regioes).

### 🧪 Insumos (insumos)
Armazena os insumos agrícolas utilizados nas plantações.

id_insumo (PK): Identificador do insumo.

nome: Nome do insumo.

preco_usd: Preço do insumo em dólar.

### ☁️ Previsões do Tempo (previsoes)
Relaciona as condições climáticas previstas com as plantações e fazendas.

id_previsao (PK): Identificador da previsão.

id_plantacao (FK): Plantação associada à previsão (plantacoes).

id_fazenda (FK): Fazenda associada à previsão (fazendas).

estacao: Estação do ano (ex: Verão, Inverno).

percentual_sucesso: Porcentagem de sucesso esperada com base na previsão.

### 🧬 Plantação x Insumo (plantacao_insumo)
Tabela associativa de muitos-para-muitos entre plantações e insumos.

id_plantacao (PK, FK): Plantação associada.

id_insumo (PK, FK): Insumo associado.

### 📟 Sensores (sensores)
Sensores usados para monitoramento em plantações.

id_sensor (PK): Identificador do sensor.

tipo: Tipo do sensor (S1, S2, S3).

descricao: Descrição do sensor e sua função.

### 📈 Leituras dos Sensores (leituras_sensores)
Registra as medições feitas por sensores nas plantações.

id_leitura (PK): Identificador da leitura.

id_sensor (FK): Sensor responsável pela leitura (sensores).

id_plantacao (FK): Plantação monitorada (plantacoes).

data_hora: Data e hora da medição.

valor_lido: Valor captado pelo sensor (ex: temperatura, umidade, etc).

## 📦 Estrutura do Projeto
📂 etapa2:  

 
- 📂 Diagrama
  
  ─ 📄 DiagramaAtividade1.pdf = Arquivo visual. 

─ 📄 scriptCriacaoTabela.sql = Script que cria as tabelas.

─ 📄 README.md = Documentação do projeto 


## 📌 Pré-requisitos

Não há pré-requisitos para esta atividade. No entanto, caso o usuário deseje rodar o script de criação de tabela, será necessário baixar o SQL Developer e o Oracle Database Express Edition, além de realizar a conexão conforme as instruções disponíveis na página oficial da Oracle.

Abaixo seguem os links para download:
 - https://www.oracle.com/br/database/technologies/appdev/xe.html
 
 - https://www.oracle.com/br/database/sqldeveloper/


## 🗃 Histórico de lançamentos

  - etapa1-v1
  - etapa2-v1 (Etapa atual - Atividade Cap 1 - Um mapa do tesouro)

