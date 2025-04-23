## FIAP - Faculdade de Informática e Administração Paulista

<br>

# Atividade Cap 6 - Python e além 

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

## Sistema de Gestão Agrícola 🌱
Este sistema foi desenvolvido para auxiliar agricultores no planejamento de plantios, cálculo de áreas e estimativa de custos com insumos. O diferencial do projeto é a integração automática entre o cálculo da área plantada e os gastos com insumos, proporcionando uma visão financeira precisa antes mesmo do plantio.

### Funcionalidades Principais
1. Cadastro Inteligente de Plantio

- 📐 Cálculo automático da área (em hectares) com base no formato de plantio: Quadrado, retângulo, triângulo, hexágono ou linhas paralelas

-  Registro da época ideal de plantio

-  Visualização de todos os plantios cadastrados


-  Gestão de Insumos com Cálculo de Custos: Sistema que calcula automaticamente quantidade total de insumos necessários (baseado na área), custo total por tipo de insumo e custo agregado por plantio

📊 Exemplo:
```  
#Fertilizante NPK: 30kg/ha (Área: 2.5ha) = 75kg → R$ 1.125,00
````

### 📝 Informações completas:

Cultura, região, época, formato, área, insumos associados e custos

### Diferencial Exclusivo
✨ Cálculo Integrado Área-Insumos-Custos ✨
O sistema não apenas calcula a área plantada, mas converte automaticamente essa informação em:

- Quantidade exata de cada insumo necessária

- Custo total por insumo

- Custo agregado por plantio

### Requisitos para Execução
 Banco de Dados: Oracle Database

### 📋 Scripts de criação das tabelas incluídos no projeto

### 🐍 Python e Bibliotecas
 Python 3.8+

### 📦 Bibliotecas necessárias:

```  
pip install oracledb
````

### Configuração
1- onfigure o arquivo config_db.py com suas credenciais do Oracle

2- Execute o script de criação das tabelas no banco de dados

3- Inicie o sistema com:


```  
py main.py
````

-  etapa1-v1
  - etapa2-v1 
  - etapa2-v2 (Etapa Atual - Atividade Cap 6 - Python e além)