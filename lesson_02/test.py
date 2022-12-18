import requests

headers = {"Content-Type": "application/json"}


resp_1 = requests.get(url="http://127.0.0.1:5000/hi/3")
print(resp_1.json())


resp_2 = requests.post(url="http://127.0.0.1:5000/hi/5", headers=headers, json={"text": "Hello", "lang": "en"})
print(resp_2.json())


resp_3 = requests.put(url="http://127.0.0.1:5000/hi/7", json={"text": "Hello", "lang": "en"})
print(resp_3.json())