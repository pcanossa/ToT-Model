# Framework de Análise Preditiva com Árvore de Decisão

Um exemplo prático de "Tree of Thoughts" para predição de comportamento do consumidor usando Machine Learning.

Este projeto é uma implementação didática que simula um sistema especialista para prever a probabilidade de um cliente adquirir um determinado produto com base em seu perfil e contexto. O modelo utiliza uma Árvore de Decisão (DecisionTreeClassifier) da biblioteca scikit-learn para aprender padrões a partir de dados históricos e, em seguida, aplicar esse conhecimento para analisar novos clientes.

## ✨ Conceito Principal: Simulando uma "Tree of Thoughts" (Árvore de Pensamentos)

A arquitetura deste projeto foi inspirada no conceito de "Tree of Thoughts" (ToT). Em vez de um único processo monolítico, o sistema é dividido em componentes:

1. **Bases de Conhecimento:** Planilhas do Google Sheets que contêm os dados históricos sobre compras de produtos.

2. **Modelos Especialistas:** Para cada base de conhecimento ("Case"), um modelo de Machine Learning separado é treinado. Cada modelo se torna um "especialista" em prever o resultado para aquele cenário específico.

3. **O Orquestrador:** Uma função central que recebe os dados de um novo cliente e os distribui para todos os modelos especialistas. Ele coleta as "opiniões" (predições) de cada especialista.

4. **Relatório Final:** O orquestrador consolida as predições em um laudo final, fornecendo uma análise multifacetada.

Essa abordagem torna o sistema modular, fácil de entender e, principalmente, de estender com novos "Cases" ou modelos especialistas sem alterar a lógica central.

## 🚀 Começando

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- **Python 3.x**

- As seguintes bibliotecas Python:

- **``pandas``**

- **``scikit-learn``**

### Instalação

1. Clone este repositório (ou simplesmente baixe o arquivo .py).

2. Abra seu terminal ou prompt de comando.

3. Instale as bibliotecas necessárias usando `pip:` \


```bash
pip install pandas scikit-learn
```

## 🔧 Configuração

Antes de executar o script, você precisa configurar sua fonte de dados.

### 1. Preparando sua Base de Dados no Google Sheets

O modelo é alimentado por uma planilha do Google Sheets. Você pode usar a planilha de exemplo ou criar a sua.

- **Link da Planilha de Exemplo:** https://docs.google.com/spreadsheets/d/1LAJ1YkfWv6TjY-RmKj-e6X4NYdm9XB26205yc_GLHjY/edit?usp=sharing

# Estrutura da Planilha:

Sua planilha deve conter as seguintes colunas para ser compatível com o código atual:

- **HORARIO:** Período do dia (ex: MANHA, TARDE).

- **MES:** Mês da ocorrência (ex: JANEIRO, FEVEREIRO).

- **TEMPERATURA:** Condição climática (ex: FRIO, CALOR).

- **VALOR_MEDIO:** Faixa de gasto (ex: 50+, 100+, 200+).

- **IDADE:** Faixa etária (ex: 19-, 20+, 30+).

- **SEXO:** Sexo do cliente (ex: F, M).

- **PRODUTO: `A coluna alvo (label)`** que o modelo tentará prever (ex: PRODUTO_A, PRODUTO_B).

**Importante:**

Para que o script consiga acessar os dados, sua planilha precisa estar compartilhada com a permissão "Qualquer pessoa com o link".

1. Abra sua planilha.

2. Clique em "Compartilhar" (canto superior direito).

3. Em "Acesso geral", mude para "Qualquer pessoa com o link".

### 2. Inserindo a URL no Código

Copie a URL da sua planilha e cole-a no local indicado no script:

```Python
# ==============================================================================
# PARTE 1: CONFIGURAÇÃO E CARREGAMENTO DE DADOS
# ==============================================================================
# ...

# URLs das suas planilhas
                                         ▼▼▼ COLE A URL DA SUA PLANILHA AQUI ▼▼▼
url_product_cases = formatar_url_gsheets('https://docs.google.com/spreadsheets/d/SUA_CHAVE_UNICA_AQUI/edit?usp=sharing')

# ...
```

==============================================================================
## 🏃‍♀️ Executando o Projeto

Com o ambiente e a configuração prontos, execute o script a partir do seu terminal:

```Bash

python nome_do_seu_arquivo.py
```

O programa irá:

1. Carregar os dados da sua planilha.

2. Treinar o(s) modelo(s) especialista(s).

3. Solicitar que você insira os dados de um "novo cliente" interativamente no terminal.

Siga as instruções de formato para cada campo solicitado (ex: MANHA para horário, FRIO para temperatura, etc., sem acentos).

**Exemplo de Interação:**

```Python

********** INSERIR NAS PERGUNTAS A SEGUIR (NÃO UTILIZAR ACENTUAÇÕES): \
... \
*********** \
HORARIO: TARDE \
MES: JULHO \
TEMPERATURA: FRIO \
VALOR MÉDIO: 100+ \
IDADE: 30+ \
SEXO: M
```

Após inserir os dados, o sistema irá gerar e exibir o relatório final.

**Exemplo de Saída:**

``` Python
================== ANÁLISE DE POSSIBILIDADE DE AQUISIÇÃO CRIADA ================== \
-> Analise_Case_1: PRODUTO_C \
============================================================
```

## dissected Código Dissecado: Entendendo as Partes

O código é dividido em quatro partes lógicas para facilitar a compreensão.

### Parte 1: Configuração e Carregamento de Dados

Esta seção inicializa o ambiente.

- **Importações:** pandas para manipulação de dados e DecisionTreeClassifier para o modelo de ML.

- formatar_url_gsheets: Uma função auxiliar útil que converte a URL de compartilhamento padrão do Google Sheets em uma URL de download direto no formato CSV, que o pandas pode ler.

- pd.read_csv: Carrega os dados da URL formatada para um DataFrame do pandas.

### Parte 2: Pré-processamento e Treinamento do Modelo Especialista

Aqui, a "inteligência" do sistema é construída.

- treinar_modelo_especialista: Esta função centraliza o processo de treinamento.

1. ``fillna('Nao_Informado')``: Trata valores ausentes nos dados, garantindo que o modelo não encontre erros.

2. ``X = df.drop(...) e y = df[...]``: Separa os dados em *features* (características, X) e *label* (o que queremos prever, y).

3. ``pd.get_dummies(X)``: Realiza o **One-Hot Encoding**. Modelos de ML não entendem texto (MANHA, FRIO). Essa função converte cada categoria de texto em colunas numéricas (0 ou 1), tornando os dados compreensíveis para o algoritmo.

4. ``modelo.fit(X_encoded, y)``: O coração do treinamento. O algoritmo da Árvore de Decisão analisa os dados codificados (X_encoded) e "aprende" as regras que conectam as características do cliente (X) ao produto comprado (y).

5. ``return modelo, X_encoded.columns``: Retorna não apenas o modelo treinado, mas também a lista exata de colunas usadas no treino. Isso é **essencial** para garantir que os novos dados de clientes sejam processados exatamente da mesma forma.

### Parte 3: O Orquestrador

Esta é a função principal que utiliza os modelos treinados.

- analisar_possibilidade_aquisicao_produto: Recebe os dados de um novo cliente e o dicionário de modelos.

1. ``pd.DataFrame([dados_cliente])``: Converte os dados do novo cliente em um DataFrame.

2. ``pd.get_dummies(df_cliente)``: Aplica a mesma transformação de One-Hot Encoding aos dados do cliente.

3. ``df_cliente_final = df_cliente_encoded.reindex(columns=colunas_treino, fill_value=0)``: **Este é o passo mais crítico.** Garante que o DataFrame do cliente tenha exatamente as mesmas colunas (na mesma ordem) que os dados de treinamento. Se o cliente tiver uma característica que não estava nos dados originais, ela é ignorada. Se faltar alguma, ela é adicionada com valor 0. Isso evita erros e garante consistência.

4. ``modelo.predict(df_cliente_final)``: Usa o modelo treinado para fazer a predição com base nos dados preparados do cliente.

5. O resultado é adicionado a um relatório final.

### Parte 4: Exemplo de Uso

Esta seção demonstra como o sistema funciona na prática.

- ``input()``: Coleta as informações do novo cliente de forma interativa.

- ``novo_cliente = {...}``: Monta um dicionário Python com os dados coletados.

- ``analisar_possibilidade_aquisicao_produto(...)``: Chama o orquestrador para iniciar a análise.

- O ``print`` final formata e exibe à análise gerado, a partir dos dadosdo cliente, para o usuário.

## 💡 Como Estender o Modelo

A arquitetura do projeto facilita a adição de novas análises (novos "Cases"). Para isso, siga os passos:

1. **Crie uma nova Planilha (Base de Conhecimento):** Por exemplo, com dados sobre a aquisição de um serviço em vez de um produto.

2. **Carregue a nova tabela no código (Parte 1):** \
   
```Python \
url_service_cases = formatar_url_gsheets('URL_DA_SUA_NOVA_PLANILHA') \
df_service_cases = pd.read_csv(url_service_cases) \
```

1. **Treine um novo Modelo Especialista (Parte 2):** \
   
```Python \
# Supondo que a coluna alvo se chame 'SERVICO' \
modelo_case2, colunas_case2 = treinar_modelo_especialista(df_service_cases, 'SERVICO') \
print("- Modelo Especialista do Case 2 - Aquisição de Serviço") \
```

4. **Adicione o novo modelo ao dicionário de modelos (Parte 2):** \

```Python \
modelos_e_colunas = { \
    'Case 1': (modelo_case1, colunas_case1), \
    'Case 2': (modelo_case2, colunas_case2), # Adicione a nova linha aqui \
} \
```

Pronto! O orquestrador na Parte 3 irá automaticamente incluir este novo modelo em sua análise, e o relatório final mostrará a predição para Analise_Case_1 e Analise_Case_2.


## 🔬 Adaptando o Projeto Para Sua Própria Análise (Guia Principal)

Esta é a seção mais importante. Siga estes passos para usar o código com **sua própria tabela e para seu próprio objetivo.**

Vamos usar um exemplo prático: imagine que você tem uma planilha para **prever o Risco de Crédito** de um cliente (Alto, Medio, Baixo) com base em outras informações.

### Passo 1: Prepare Seus Dados

Sua tabela pode ser um arquivo .csv no seu computador ou uma planilha no Google Sheets. O mais importante é a estrutura:

- **Features (Características):** As colunas que você usará como entrada para a predição. No nosso exemplo: *RENDA_MENSAL*, *HISTORICO_PAGAMENTO*, *TIPO_MORADIA*.

- **Target (Alvo):** A coluna que você quer prever. No nosso exemplo: RISCO_CREDITO.

Exemplo de Tabela de Risco de Crédito (meus_dados.csv):

```
| RENDA_MENSAL | HISTORICO_PAGAMENTO | TIPO_MORADIA | RISCO_CREDITO |

| :----------- | :------------------ | :----------- | :------------ |

| 2000-4000 | Bom | Alugada | Baixo |

| ate-2000 | Ruim | Propria | Alto |

| 4000+ | Bom | Propria | Baixo |

| 2000-4000 | Regular | Alugada | Medio |
```

### Passo 2: Carregue Seus Dados no Código

Vá para a **PARTE 1** do script e altere a forma como os dados são carregados para apontar para o seu arquivo.

**Opção A: Carregar um arquivo CSV local (Recomendado)**

```Python

==============================================================================
Opção A: Carregar um arquivo CSV local

Python

df_meus_dados = pd.read_csv('C:/CAMINHO_DO_ARQUIVO_CSV/ARQUIVO.csv') \
```

```Python

==============================================================================
Opção B: Usar uma nova Planilha Google Sheets

Se preferir, suba sua tabela para o Google Sheets, compartilhe com "Qualquer pessoa com o link" e ajuste a URL:


url_meus_dados = formatar_url_gsheets('URL_DA_SUA_NOVA_PLANILHA_AQUI') \
df_meus_dados = pd.read_csv(url_meus_dados) \
```

### Passo 3: Ajuste o Treinamento do Modelo

Na **PARTE 2**, você precisa dizer à função de treinamento qual é a sua **coluna alvo (target)**.

- **Encontre a linha:** ``modelo_case1, colunas_case1 = treinar_modelo_especialista(...)``

- **Altere os dois argumentos:**

1. O nome do seu DataFrame (que você definiu no Passo 2, ex: **df_meus_dados**).

2. O nome da sua coluna alvo, entre aspas (ex: '*RISCO_CREDITO*').

**Como editar o código (PARTE 2):**

- **Antes:** \

# Treinando um modelo para cada Case \
``modelo_case1, colunas_case1 = treinar_modelo_especialista(df_product_cases, 'PRODUTO')`` \


- **Depois (para nosso exemplo de Risco de Crédito):** \

# Treinando um modelo para os Meus Dados \

```Python
modelo_case1, colunas_case1 = treinar_modelo_especialista(df_meus_dados, 'RISCO_CREDITO') # <-- ALTERE AQUI \
print("- Modelo Especialista de Análise de Crédito treinado.") \
```


### Passo 4: Atualize a Coleta de Dados para Predição

Na **PARTE 4**, o script pede ao usuário para digitar os dados de um "novo caso". Você precisa mudar as perguntas (input()) e as chaves do dicionário para que correspondam às **colunas de features** da sua tabela.

**Como editar o código (PARTE 4):**

- **Antes:** \

```Python 
Horario = input('HORARIO: ') 
# ... etc ... 
novo_cliente = { 
    'HORARIO': Horario, 
    'MES': Mes, 
    # ... etc ... 
} \
```


- **Depois (para nosso exemplo de Risco de Crédito):** \
  
```Python \
# Mude as perguntas para refletir suas colunas 
Renda = input('RENDA_MENSAL (ex: 2000-4000, 4000+): ') 
Historico = input('HISTORICO_PAGAMENTO (ex: Bom, Ruim): ') 
Moradia = input('TIPO_MORADIA (ex: Alugada, Propria): ') 
 \
# Crie o dicionário com as CHAVES IGUAIS AOS NOMES DAS SUAS COLUNAS 
novo_caso = { 
    'RENDA_MENSAL': Renda, 
    'HISTORICO_PAGAMENTO': Historico, 
    'TIPO_MORADIA': Moradia, 
} 
 
# Chame a análise com os novos dados 
analise_final = analisar_possibilidade_aquisicao_produto(novo_caso, modelos_e_colunas) 
```


**Atenção:** Os nomes das chaves no dicionário ``('RENDA_MENSAL', etc.)`` devem ser **exatamente iguais** aos nomes das colunas no seu arquivo.

### Passo 5: Execute e Interprete

Agora, você está pronto! Execute o script no seu terminal:

```Bash

python nome_do_seu_arquivo.py
```

O programa irá:

1. Carregar **seus dados**.

2. Treinar um modelo especialista para **seu problema**.

3. Fazer as **suas perguntas** personalizadas.

4. Entregar uma predição para a **sua coluna alvo**.

**Exemplo de Interação e Saída Personalizada:**

```
RENDA_MENSAL (ex: 2000-4000, 4000+): ate-2000 \
HISTORICO_PAGAMENTO (ex: Bom, Ruim): Regular \
TIPO_MORADIA (ex: Alugada, Propria): Alugada \
 \
================== ANÁLISE DE RISCO DE CRÉDITO CRIADA ================== \
-> Analise_Case_1: Alto \
============================================================
```

O resultado **Alto** é a predição do modelo para a sua coluna *RISCO_CREDITO*.
