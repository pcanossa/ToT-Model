# ==============================================================================
# PARTE 1: CONFIGURAÇÃO E CARREGAMENTO DE DADOS
# ==============================================================================
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import warnings

# Ignorar avisos futuros para manter a saída limpa
warnings.simplefilter(action='ignore', category=FutureWarning)

print("--- Módulo de Análise Laboratorial Inteligente ---")
print("Passo 1: Carregando as bases de conhecimento...")

# Função para converter o link do Google Sheets para o formato de download CSV
def formatar_url_gsheets(url):
    return url.replace('/edit?usp=sharing', '/export?format=csv')

# URLs das suas planilhas
url_product_cases = formatar_url_gsheets('https://docs.google.com/spreadsheets/d/1LAJ1YkfWv6TjY-RmKj-e6X4NYdm9XB26205yc_GLHjY/edit?usp=sharing')

# Carregando os dados em DataFrames
try:
    df_product_cases = pd.read_csv(url_product_cases)
    print("Sucesso! Todas as 4 tabelas foram carregadas.\n")
except Exception as e:
    print(f"Erro ao carregar as planilhas: {e}")
    print("Verifique se os links estão corretos e compartilhados como 'Qualquer pessoa com o link'.")

# ==============================================================================
# PARTE 2: PRÉ-PROCESSAMENTO E TREINAMENTO DO MODELO ESPECIALISTA
# ==============================================================================

print("Passo 2: Treinando o modelo especialista...")

def treinar_modelo_especialista(df, nome_coluna_produto):
    """
    Função reutilizável para pré-processar e treinar um modelo de árvore de decisão.
    """
    # Tratar células vazias como 'Nao_Informado'
    df_tratado = df.fillna('Nao_Informado')

    # Separar as features (X) do label (y)
    X = df_product_cases.drop(nome_coluna_produto, axis=1)
    y = df_product_cases[nome_coluna_produto]

    # Converter colunas de texto em colunas numéricas (One-Hot Encoding - Binário)
    X_encoded = pd.get_dummies(X)

    # Treinar o modelo
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_encoded, y)

    # Retornar o modelo treinado e as colunas usadas no treino (essencial!)
    return modelo, X_encoded.columns

# Treinando um modelo para cada Case
modelo_case1, colunas_case1 = treinar_modelo_especialista(df_product_cases, 'PRODUTO')
print("- Modelo Especialista do Case 1 - Aquisição de Produto ")

modelos_e_colunas = {
    'Case 1': (modelo_case1, colunas_case1),
}
  # Retorna modelos treinados, podendo ser inserida análise de novas tabelas, como novos cases

# ==============================================================================
# PARTE 3: O ORQUESTRADOR - A FUNÇÃO PRINCIPAL DE ANÁLISE
# ==============================================================================

print("Passo 3: Construindo o orquestrador do sistema...")


def analisar_possibilidade_aquisicao_produto(dados_cliente, modelos):
  # Função solicita os dados do cliente para análise comparativa
  # e oo objeto que possui os modelos a serem analisados:
  # Cases criados a partir de cada tabela fornecida

    relatorio_final = {}

    # --- NÍVEL 2: MÓDULOS DE ANÁLISE (acionando os modelos) ---
    print("Nível 2 (Especialistas): Acionando modelos...")

    for case in modelos:
        # Recupera cada case incluído no objeto de modelos por vez para análise
        modelo, colunas_treino = modelos[case]

        # Preparar os dados do cliente para o modelo específico
        df_cliente = pd.DataFrame([dados_cliente])
        df_cliente_encoded = pd.get_dummies(df_cliente)

        # Garantir que o df do cliente tenha exatamente as mesmas colunas do treino
        df_cliente_final = df_cliente_encoded.reindex(columns=colunas_treino, fill_value=0)

        # Fazer a predição
        predicao = modelo.predict(df_cliente_final)

        # Adicionar ao relatório
        nome_analise = f"Analise_{case.replace(' ', '_')}"
        relatorio_final[nome_analise] = predicao[0]

    return relatorio_final

print("Sucesso! Sistema pronto para receber dados do cliente.\n")

# ==============================================================================
# PARTE 4: EXEMPLO DE USO
# ==============================================================================

# Vamos simular um novo cliente.

print ('********** INSERIR NAS PERGUNTAS A SEGUIR (NÃO UTILIZAR ACENTUAÇÕES):\nHORARIO: MANHA OU TARDE\nMES: NOME DO MES (JANEIRO, FEVEREIRO, ETC ...)\nTEMPERATURA: FRIO OU CALOR\nVALOR MÉDIO: 50+ (PARA GASTOS DE 50 A 100), 100+ (100 A 200) OU 200+ (ACIMA DE 200)\nIDADE: 19- (ATÉ 19 ANOS), 20+ (20 A 30 ANOS), 30+ (30 A 40 ANOS)...,\nSEXO: F (PARA FEMININO) OU M (PARA MASCULINO)\n***********')
Horario = input('HORARIO: ')
Mes = input('MES: ')
Temperatura = input('TEMPERATURA: ')
Valor_Medio = input('VALOR MÉDIO: ')
Idade = input('IDADE: ')
Sexo = input('SEXO: ')


novo_cliente = {
    'HORARIO': Horario,
    'MES': Mes,
    'TEMPERATURA': Temperatura,
    'VALOR_MEDIO': Valor_Medio,
    'IDADE': Idade,
    'SEXO': Sexo
}

# Executa a análise completa
analise_final = analisar_possibilidade_aquisicao_produto(novo_cliente, modelos_e_colunas)

# Imprime o laudo final de forma organizada
print("\n================== ANÁLISE DE POSSIBILIDADE DE AQUISIÇÃO CRIADA ==================")
if analise_final:
    for chave, valor in analise_final.items():
        print(f"-> {chave}: {valor}")
else:
    print("Não foi possível gerar uma análise.")
print("============================================================")