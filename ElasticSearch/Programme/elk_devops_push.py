#pip3  uninstall elasticsearch
#pip3  install elasticsearch==7.13.4
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch([{"host": "127.0.0.1", "port": 9200}])
doc = {
    "author": "document-author",
    "text": "A text document",
    "timestamp": datetime.now()
}
res = es.index(index="sample-index-2", id=3, body=doc)
print(res['result'])