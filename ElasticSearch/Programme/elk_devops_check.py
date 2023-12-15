import requests
substring = "You Know, for Search".encode()
response = requests.get("http://127.0.0.1:9200")
if substring in response.content:
    print("Elasticsearch is up and running!")
else:
    print("Something went wrong, ensure the cluster is up!")