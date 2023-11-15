#Mapping Your index first,you must be declare the shape after that we give the name

### This 2 'dict' one dict receive properties and another receive name plus type of data 
## tip01 : You must include a ignore=400 if has empy or null values inside your data

# body = {
#     "settings" : {"numeber_of_shards": 1},
#     "mappgins" : {
#         "properties": {
#                 "title": {"type": "text", "analyzer": "english"},
#                 "ethnicity": {"type": "text", "analyzer": "standard"},
#                 "director": {"type": "text", "analyzer": "standard"},
#                 "cast": {"type": "text", "analyzer": "standard"},
#                 "genre": {"type": "text", "analyzer": "standard"},
#                 "plot": {"type": "text", "analyzer": "english"},
#                 "year": {"type": "integer"},
#                 "wiki_page": {"type": "keyword"},
#         }
#     },
# },
# ignore=[400]


def create_index(client):
    client.indices.create( 
        index="NAME_OF_INDEX",
        body = {
        "settings" : {"numeber_of_shards": 1},
        "mappgins" : {
            "properties": {
                    "title": {"type": "text", "analyzer": "english"},
                    "ethnicity": {"type": "text", "analyzer": "standard"},
                    "director": {"type": "text", "analyzer": "standard"},
                    "cast": {"type": "text", "analyzer": "standard"},
                    "genre": {"type": "text", "analyzer": "standard"},
                    "plot": {"type": "text", "analyzer": "english"},
                    "year": {"type": "integer"},
                    "wiki_page": {"type": "keyword"},
            }
        },
    },
    ignore=[400]
    )