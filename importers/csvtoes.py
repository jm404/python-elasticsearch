from datetime import datetime
from elasticsearch import Elasticsearch,helpers
import csv
import json

def actions_generator(elastic_instance,index_name,bulk_function, data):
    def generator():
        size = len(data)
        for i in range(size):
            yield{
                '_index': index_name,
                '_id' : i,
                '_type' : 'document',
                '_source' : (data[i]),
            }
            
    for ok, info in bulk_function(elastic_instance,generator()):
        if not ok:
            print ("Error parsing", info)
        
def rows_formatter(path):
    with open (path) as f:
        dict_reader = csv.DictReader(f)
        rows = list(dict_reader)
    return rows

def importer(elastic_instance,index_name,path,processing_method):
    if (processing_method == "parallel"):
        actions_generator(elastic_instance,index_name,helpers.parallel_bulk,rows_formatter(path))
    elif (processing_method == "single"):
        actions_generator(elastic_instance,index_name,helpers.bulk,rows_formatter(path))
    else:
        print ("Unknown bulk method")
    


