from elasticsearch import Elasticsearch, helpers
import configparser
from datetime import datetime

# Lê as configurações do arquivo acess.ini
config = configparser.ConfigParser()
config.read('acess.ini')

config = configparser.ConfigParser()
config.read('acess.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    basic_auth=(config['ELASTIC']['user'], config['ELASTIC']['password']),
    timeout = 30
)

print(es.info().body)