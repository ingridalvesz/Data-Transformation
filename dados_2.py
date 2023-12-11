import pandas as pd

dt_data = pd.read_json('moveis_disponiveis.json')
dt_data.head()
# ler os dados .read_json('') e observar as 5 primeiras linhas dos dados com o .head()

dt_data.info()

dt_data['data'] = pd.to_datetime(dt_data['data'])
# o .to_datetime transforma a coluna de um dataframe em datetime

dt_data.head()

dt_data['data'].dt.strftime('%Y-%m')
# para a formatação do tempo utilizamos o .strftime()

subset = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
subset
# para agrupar os dados utilizamos o .groupby() 

dt_data.info()


# %%