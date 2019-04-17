from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

company = {
    'name': 'Microsoft',
    'Owner': 'Bill Gates',
    'Products' : ['Office','Windows','Outlook'],
}

res = es.index(index="companies", doc_type='company', id=1, body=company)
print(res['result'])

## Request data

request = es.get(index="companies", doc_type='company', id=1)

request = es.search(index="companies",)

print (request)


