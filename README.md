<<<<<<< HEAD
NYC Restaurants Elasticsearch Indexer
This Python script downloads a public dataset of New York City restaurants and indexes it into Elasticsearch. The dataset includes information about the name, borough, cuisine, grade, and location of each restaurant.

Prerequisites
Python 3.x
Elasticsearch cluster (update the client configuration in the script)
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/seu-username/seu-repositorio.git
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Run the script:

bash
Copy code
python script.py
Follow the prompts to download the dataset, create an Elasticsearch index, and index the documents.

Configuration
Update the Elasticsearch client configuration in the main() function to point to your Elasticsearch cluster.

python
Copy code
client = Elasticsearch(
    # Add your cluster configuration here!
)
Dataset Source
The script uses the NYC Restaurants dataset from the City of New York's open data platform.

Elasticsearch Index Mapping
The script creates an index named "nyc-restaurants" with the following mapping:

name: Text field
borough: Keyword field
cuisine: Keyword field
grade: Keyword field
location: Geo-point field
License
This project is licensed under the MIT License - see the LICENSE file for details.
=======
# NYC Restaurants Elasticsearch Indexer

Este é um script em Python que indexa dados de restaurantes da cidade de Nova York em um cluster Elasticsearch. O script realiza o download de um conjunto de dados público sobre restaurantes da cidade de Nova York, processa os dados e os indexa em um índice no Elasticsearch.

## Requisitos

- Python 3.x
- Bibliotecas Python: `csv`, `urllib3`, `elasticsearch`, `tqdm`

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto


2. instale as dependências

   ```bash
   git pip install -r requirements.txt


##  Entendendo o Código
O script consiste em várias funções que realizam as seguintes tarefas:

### download_dataset():
  Baixa o conjunto de dados público se ainda não estiver localmente disponível e retorna o número de linhas no arquivo CSV.
  create_index(client): Cria um índice no Elasticsearch se ainda não existir.

### generate_actions():
  Lê o arquivo CSV usando csv.DictReader() e, para cada linha, gera um documento que será indexado no Elasticsearch.

### main():
  Coordena as chamadas às funções anteriores para realizar o processo de download e indexação.
 Certifique-se de substituir a configuração do cliente Elasticsearch no bloco main() com as configurações específicas do seu cluster.

# Contribuindo
Sinta-se à vontade para abrir problemas, enviar solicitações de recebimento ou contribuir com melhorias para este projeto.
>>>>>>> c35a3593c9302f513b0b3638413e10ab4bb024cf
