from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import csvtoes
es = Elasticsearch()

#csvtoes.importer(es,"testing_import","importers/data_samples/TechCrunchcontinentalUSA.csv","parallel")

s = Search(using=es,index="testing_import").query("match", category="web")
response = s.execute()
for hit in s:
 print ("Category: ",hit.category,"-- Employees: ", hit.numEmps)


