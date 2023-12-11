import pandas as pd
import numpy as np


dados = pd.read_json('dados_hospedagem.json')
dados.head()
# ler os dados .read_json('') e observar as 5 primeiras linhas dos dados com o .head()

dados = pd.json_normalize(dados['info_moveis'])
dados
# para normalizar a visualização dos dados usomos o .json_normalize

colunas = list(dados.columns)
colunas
# visualização dos nomes das colunas

dados = dados.explode(colunas[3:])
dados
# para não ter dados agrupados em listas usamos .explode() 

dados.reset_index(inplace=True, drop=True)
dados.head()
# aqui usamos o .reset_index() para ordenar os dados

dados.info()

dados['max_hopedes'] = dados['max_hospedes'].astype(np.int64)
# para converter colunas para um tipo específico de dado (int,float, etc...) usamos o .astype() dentro da bilioteca Numpy np.int64 mudamos o tipo do dado

col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']
# definimos as colunas as quais são numéricas

dados[col_numericas] = dados[col_numericas].astype(np.int64)
# para assim alteramos o tipo de todas incluídas no col_numericas

dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)
# para o tipo float terermos que observar se existem sinais como $ antes de gerar o comando

dados['preco'] = dados['preco'].apply(lambda x: x.replace('$','').replace(',','').strip())
dados['preco'] = dados['preco'].astype(np.float64)
# tirando o ('$', ',') com .apply e assim podendo ser aplicado o novo tipo

dados[['taxa_deposito', 'taxa_limpeza']].applymap(lambda x: x.replace('$','').replace(',','').strip())
# na conversão de um dataframe, no qual passaremos por cada elemento, é mais viável utilizarmos o método .applymap()

dados[['taxa_deposito', 'taxa_limpeza']] = dados[['taxa_deposito', 'taxa_limpeza']].applymap(lambda x: x.replace('$','').replace(',','').strip())
dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].astype(np.float64)

dados.info()

dados['descricao_local'] = dados['descricao_local'].str.lower()
# os elementos de leitura estão como strings por conta do .str e o .lower() transfoma o texto com letras minúsculas

dados['descricao_local'] = dados['descricao_local'].str.replace('[^ a-z A-Z 0-9\-\']', ' ', regex=True)
# o .str junto com o .replace() são utilizados para alterar caracteres

dados['descricao_local'] = dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', ' ', regex=True)

# %%