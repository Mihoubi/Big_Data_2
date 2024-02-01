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
elastic_index = "poc_real_time_londres"
elastic_type = "json"
# json_headers = json.loads(headers)
# print(len(json_data))
elastic_address = "localhost:9200"
r = requests.get('http://localhost:9200')
connection = http.client.HTTPConnection(elastic_address)
print(r.status_code)
i = 1
for element in json_data:
    to_elastic_string = ""
    element = json.dumps(element)
    index_row = {"index": {"_id": i, "_index": elastic_index, "_type": elastic_type}}
    json_string = json.dumps(index_row) + "\n" + element + "\n"
    to_elastic_string += json_string
    search_param = {"query": {"terms": {"_id": [1] }}}

    try:
        response = es.get(index="poc_real_time_londres", id=1)
        print ('response:', response)
    except IOError:
        print("IO problem")
    else:
        print('Problem with your code')
    # print(element)
    #connection.request('POST', url="localhost:9200/_bulk?pretty", headers=headers, body=to_elastic_string)
    #response = connection.getresponse()
    #body = response.read().decode('utf-8')
    #response_details = json.loads(body)
    #print(response_details)
    #i = i + 1
print(i)
#print ("id:"+json_data[0]['id'])
#print(r.content.decode('utf-8'))
# print ("####################################")
# headers = '{"Content-type": "application/x-ndjson", "Accept": "text/plain"}'
# json_headers = json.loads(headers)
# header = '{ "create" : { "_index" : "test2", "_type" : "_doc", "_id" : "11" } }'
# #json_string = json.dumps(r.content)
# #es.index(index='rat', doc_type='people', id=i,
# # body=r)
# elastic_address = "localhost:9200"
#
# print ("####################################")
# print ("####################################")
# #print (to_elastic_string)
# print ("####################################")
# #response_string = response_string+ "b\n"
# connection = http.client.HTTPConnection(elastic_address)
# connection.request('POST', url=endpoint, headers =json_headers, body=header)
# response = connection.getresponse()
# body = response.read().decode('utf-8')
# response_details=json.loads(body)
# print (response_details)
#

# r = requests.get('http://localhost:9200')
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/'+ str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i=i+1
# python3 csv_to_elastic.py         --elastic-address 'localhost:9200'         --csv-file CGI-1.csv        --elastic-index 'testcgi2'         --datetime-field=dateField         --json-struct '{
# "firstname":"%firstname%",
# "lastname":"%firstname%",
# "email":"%email%",
# "ProgrammationSkills":"%ProgrammationSkills%"
# "EnglishLevel":"%EnglishLevel%",
# "Education":"%Education%",
# "GraduationDate","%GraduationDate%",
# "Experience","%Experience%",
# "YearsExperience", "%YearsExperience%"
# }'




#print (es.get(index='testcgi11', id="?"))



# import json
# r = requests.get('http://localhost:9200')
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/'+ str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i=i+1
#
#print(i)
#es.get(index='yes', doc_type='people', id=3)
