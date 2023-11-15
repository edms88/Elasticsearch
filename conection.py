from elasticsearch import Elasticsearch, helpers
import configparser
from datetime import datetime
import csv
from os.path import abspath, join, dirname, exists
import tqdm
import urllib3

from elasticsearch.helpers import streaming_bulk



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