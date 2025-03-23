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

## 📌 Exemplo de Uso

```
--- Menu Principal ---
1. Cadastrar cultura
2. Adicionar dados de plantio
3. Ver culturas cadastradas
4. Excluir cultura
5. Sair
```

## ❓ Tem dúvidas ?  
### Entre em contato:
- giovanna.siqueirab@gmail.com
- fulano.com.br  
- beltrano.com.ve

