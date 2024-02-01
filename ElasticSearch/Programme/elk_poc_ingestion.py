import http
import json
import requests

res = requests.get('http://localhost:9200')
from elasticsearch import Elasticsearch, connection

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# print(res.content)
request_ELK = requests.get('http://localhost:9200')
r = requests.get('https://api.tfl.gov.uk/line/94/arrivals/')
# response = r
i = 1
endpoint = '/_bulk'
response_string = r.content.decode('utf-8')
# json_string = json.dumps(response_string)
json_data = json.loads(response_string)
headers = {"Content-type": "application/x-ndjson", "Accept": "text/plain"}
elastic_index = "hello"
elastic_type = "peopel"
# json_headers = json.loads(headers)
#print(len(json_data))
elastic_address = "localhost:9200"
r = requests.get('http://localhost:9200')
print(r.status_code)
i = 1
#while elastic_address.status_code =="200":
while i==1:
    for element in json_data:
        to_elastic_string = ""
        element = json.dumps(element)
        index_row = {"index": {"_index": elastic_index, "_type": elastic_type}}
        json_string = json.dumps(index_row) + "\n" + element + "\n"
        to_elastic_string += json_string
        #print(element)
        connection = http.client.HTTPConnection(elastic_address)
        connection.request('POST', url="localhost:9200/_bulk?pretty", headers=headers, body=to_elastic_string)
        response = connection.getresponse()
        body = response.read().decode('utf-8')
        response_details = json.loads(body)
        print(response_details)
i = i+1
print(i)