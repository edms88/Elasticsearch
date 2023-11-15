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