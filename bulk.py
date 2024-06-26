import csv

from os.path import abspath, join, dirname, exists
from pathlib import Path

# Bibliotecas de terceiros
import pandas as pd
import tqdm
import urllib3
from elasticsearch import Elasticsearch, helpers
import configparser
import elasticsearch_dsl
from elasticsearch.helpers import streaming_bulk, bulk

from datetime import datetime


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
base01 = current_dir / "Braskem csc n1" / "Base chamado.csv"

# Ler o arquivo CSV com a codificação detectada
df = pd.read_csv(base01,  encoding='ISO-8859-1', sep=",").reset_index(drop=True)

df['Estado']    =  df['Estado'].fillna('-')
df['Primario']  =  df['Primario'].fillna('-')
df['Atribuido'] = df['Atribuido'].fillna('-')
df['Encerrado'] = df['Encerrado'].fillna('-')


df['Aberto'] = pd.to_datetime(df['Aberto'], errors='coerce')
df['Encerrado'] = pd.to_datetime(df['Encerrado'], errors='coerce')
df['Prazo'] = pd.to_datetime(df['Prazo'], errors='coerce')
display(df)
#df.info()


config = configparser.ConfigParser()
config.read('acess.ini')
es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    basic_auth=(config['ELASTIC']['user'], config['ELASTIC']['password']),
    request_timeout=30
)

display(es.info())



# Mapeamento do índice
mapa = {
    "properties": {
        "@timestamp": {"type": "date"},
        "Aberto": {"type": "date", "format": "dd/MM/yyyy HH:mm:ss"},
        "Atraso": {"type": "keyword"},
        "Atribuido": {"type": "keyword"},
        "Categoria": {"type": "keyword"},
        "Chamado": {"type": "keyword"},
        "Empresa": {"type": "keyword"},
        "Encerrado": {"type": "date", "format": "dd/MM/yyyy HH:mm:ss"},
        "Estado": {"type": "keyword"},
        "Grupo de atribuicao": {"type": "text"},
        "Prazo": {"type": "date", "format": "dd/MM/yyyy HH:mm:ss"},
        "Primario": {"type": "keyword"},
        "Solicitante": {"type": "keyword"},
        "Tipo de Servicos": {"type": "text"},
        "out date": {"type": "keyword"}
    }
}

# Criar índice se não existir
if not es.indices.exists(index="braskem_csc06"):
    es.indices.create(index="braskem_csc06", mappings=mapa)
    print("O índice 'braskem_csc06' com os mapeamentos especificados foi criado com sucesso.")
else:
    print("Índice 'braskem_csc06' já existe.")



# Função para converter Timestamps e NaT
def convert_dates(row):
    row['Aberto'] = row['Aberto'].isoformat() if pd.notna(row['Aberto']) else None
    row['Prazo'] = row['Prazo'].isoformat() if pd.notna(row['Prazo']) else None
    row['Encerrado'] = row['Encerrado'].isoformat() if pd.notna(row['Encerrado']) else None
    return row

# Aplicar a conversão em todas as linhas
df = df.apply(convert_dates, axis=1)


from elasticsearch import Elasticsearch, helpers
import pandas as pd



# Supondo que 'df' é o DataFrame contendo os dados
bulk_data = []
for i, row in df.iterrows():
    # Construindo a ação para a operação bulk no Elasticsearch
    action = {
        "_index": "braskem_csc06",
        "_id": i,
        "_source": {
            "@timestamp": row["Aberto"],  # Descomentado se o campo existir no DataFrame
            "Chamado": row["Chamado"],
            "Estado": row["Estado"],
            "Primario": row["Primario"],
            "Categoria": row["Categoria"],
            "Tipo de Servicos": row["Tipo de Servicos"],
            "Empresa": row["Empresa"],
            "Solicitante": row["Solicitante"],
            "Aberto": row["Aberto"],
            "Grupo de atribuicao": row["Grupo de atribuicao"],
            "Atribuido": row["Atribuido"],
            "Prazo": row["Prazo"],
            "Encerrado": row["Encerrado"],
            "Atraso": row["Atraso"],
            "out date": row["out date"]
        }
    }
    bulk_data.append(action)

# Executar a operação bulk
success, _ = helpers.bulk(es, bulk_data, ignore_status=[400])

# Verificar contagem de documentos no índice
count = es.cat.count(index="braskem_csc06")
print(count)
