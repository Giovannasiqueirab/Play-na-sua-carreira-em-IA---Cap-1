# 🌱 Gerenciador de Culturas Agrícolas

Este é um projeto simples para **cadastrar culturas agrícolas**, calcular a **área de plantio** e estimar a **quantidade de insumos necessários** para diferentes tipos de plantação. O sistema foi desenvolvido em **Python** e pode ser executado no terminal.

## 🙋 Funcionalidades

### 1- Cadastrar novas culturas agrícolas
Levamos em consideração a cana-de-açúcar, pois São Paulo lidera a produção nacional, sendo referência na fabricação de etanol e açúcar, e o algodão, já que o Piauí tem se destacado no cultivo da fibra, especialmente nas regiões de chapada, onde as condições são favoráveis para o desenvolvimento da cultura. Além disso, incluímos a abóbora e a cenoura para testar a viabilidade de mais de duas culturas no sistema.
### 2- Calcular área de plantio com diferentes formatos (quadrado, retângulo, triângulo, hexágono)
As áreas de plantio foram escolhidas com base em informações amplamente utilizadas no mercado, servindo como um bom ponto de partida para o programa. O formato quadrado é ideal para a abóbora, garantindo espaçamento adequado e circulação de ar. O retângulo facilita o cultivo da batata em linhas paralelas, favorecendo a mecanização. O triângulo equilátero otimiza o espaço para a cenoura, permitindo um melhor desenvolvimento das raízes. O hexágono melhora a distribuição da luz e ventilação para a alface. Já as linhas paralelas são ideais para o milho, facilitando o manejo e o uso de maquinário agrícola. Com o tempo, o programa poderá ser expandido para incluir mais opções e variações.


### 3- Estimar a quantidade de insumos necessários para algumas culturas específicas  
A estimativa de insumos foi baseada em práticas comuns do mercado para cada cultura selecionada, garantindo um ponto de partida confiável para o programa. Para a cana-de-açúcar, são considerados fertilizantes ricos em nitrogênio, fósforo e potássio, além de corretivos de solo. No cultivo da abóbora, a adubação orgânica e o controle de pragas são essenciais para um bom desenvolvimento. A cenoura demanda fertilizantes específicos para estimular o crescimento das raízes e um manejo adequado do solo. Já o algodão exige uma nutrição equilibrada e defensivos agrícolas para garantir produtividade e resistência a pragas. Com a evolução do programa, novas culturas e insumos poderão ser incluídos para ampliar sua precisão e aplicabilidade.
### 4- Listar e excluir culturas cadastradas  
É de suma importância que um programa tenha a opção de excluir dados já cadastrados, permitindo a correção de informações inseridas incorretamente e garantindo maior flexibilidade no gerenciamento das culturas. Além disso, essa funcionalidade atende a um dos requisitos da atividade, assegurando que o sistema seja dinâmico e adaptável conforme necessário.


## 📦 Estrutura do Projeto
📂 gerenciador-culturas:  

─ 📄 cadastro.py = Funções para cadastrar culturas  

─ 📄 cultura.py = Classe Cultura e cálculos de área/insumos  

─ 📄 plantio.py = Função para adicionar dados de plantio  

─ 📄 menu.py = Menu principal do programa  

─ 📄 mediaDesvio.R = Calculo da media e desvio em R  

─ 📄 README.md = Documentação do projeto 



## 📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o **Python 3** instalado na sua máquina.  

Você pode verificar a versão instalada com o comando:
```  
python --version
````
## ▶️ Como Executar
1 - Clone este repositório:


```
git clone https://github.com/seu-usuario/gerenciador-culturas.git
```
2 - Acesse a pasta do projeto:
```
cd gerenciador-culturas
```

3- Execute o main do projeto:
```
python main.py
```
ou
```
py main.py
```

## 📌 Exemplo de Uso

```
--- Menu Principal ---
1. Cadastrar cultura
2. Adicionar dados de plantio
3. Ver culturas cadastradas
4. Excluir cultura
5. Sair
```
## 🖥️ Calculo em R 
### média
 Este código tem como objetivo calcular a média de consumo de fertilizantes (Nitrogênio, NPK 4-14-8 e Potássio) em diferentes formatos de plantio. Os valores utilizados para os cálculos foram definidos com base em referências do mercado agrícola e nas dimensões das áreas selecionadas, garantindo um cenário realista para a análise.

As áreas consideradas incluem quadrado, retângulo, triângulo, hexágono e linhas paralelas, cada uma com um espaçamento específico entre plantas e fileiras. Com isso, foi possível estimar a quantidade de fertilizante necessária para cada tipo de plantio e calcular a média de uso por metro quadrado.

### Desvio

Além da média de consumo, também foi feito o calculo de desvio padrão do uso de fertilizantes (Nitrogênio, NPK 4-14-8 e Potássio) para diferentes tipos de plantio. O desvio padrão é uma medida de dispersão que indica o grau de variação ou incerteza nos valores de consumo em relação à média calculada.

Com base nas áreas de plantio e nos espaçamentos definidos, o desvio padrão ajuda a entender o quão consistentes ou variáveis são os dados de consumo de fertilizantes entre as diferentes áreas. Dessa forma, o cálculo do desvio padrão complementa a análise, oferecendo uma visão mais detalhada sobre a distribuição dos fertilizantes.

## ▶️ Como Executar
### Passo 1: Instalar o R
Certifique-se de ter o R instalado em seu computador. Você pode baixá-lo aqui: https://www.r-project.org/

### Passo 2: Instalar o RStudio (Opcional)  
você conseguirá rodar o código em uma IDE, desde que tenha as extensões necessárias para isso. Você pode baixar o RStudio aqui: https://posit.co/downloads/

### Passo 3: Rodar o Código
Abra o RStudio ou qualquer IDE que você esteja usando para R.

Crie um novo script (.R) e cole o código fornecido.

Execute o código pressionando o botão Run (ou utilizando o atalho correspondente, geralmente Ctrl + Enter no RStudio).

Os resultados da média e do desvio padrão serão exibidos no console.

### ⭕ Observação
Certifique-se de que todas as variáveis e bibliotecas necessárias estão corretamente definidas antes de rodar o código. Caso contrário, o código pode não funcionar como esperado.


##  Tem dúvidas ❓ 
### Entre em contato:
- giovannasiqueirab@gmail.com
- ia3f@icloud.com 

